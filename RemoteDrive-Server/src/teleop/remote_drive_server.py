import logging
import threading
import time
import socket

from drive.teleop.controller import Gamepad

# Drive Computer
# Teleop Server
#
# Part of the GSSM Autonomous Golf Cart
# Written by: Joseph Telaak, class of 2022

class Remote_Drive_Server:

    def __init__(self, gamepad=Gamepad(), establish_port=42070, command_port=70, log_port=421, response_port=778):
        # Kill
        self.kill = False
        self.connection_established = False

        # Setup the message logging
        self.logger = logging.getLogger("teleop_server")
        file_handler = logging.FileHandler("logs/teleop_server.log")
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(threadName)s - %(message)s"))
        self.logger.addHandler(file_handler)

        # Current IP
        self.connected_ip = "127.0.0.1"

        # Ports
        self.establish_port = establish_port
        self.command_port = command_port
        self.log_port = log_port
        self.response_port = response_port

        # Threads
        self.control_listener = threading.Thread(target=self.establishListen, name="control_listener", daemon=True)
        self.command_listener = threading.Thread(target=self.commandListener, name="command_listener", daemon=True)
        self.response_server = threading.Thread(target=self.responseUpdater, name="response_updater", daemon=True)
        self.log_server = threading.Thread(target=self.logUpdater, name="log_server", daemon=True)

        # Messages
        self.current_log_message = "Initializing"
        self.current_response_message = "Initializing"

        # Gamepad
        self.gamepad = gamepad

    # Initialize the connection
    def intialize(self):
        self.logger.info("Initializing Teleop Client")
        self.control_listener.start()
    
    # Listen for an establish message 
    def establishListen(self):
        # Accept Connections
        self.logger.debug("Opening Connection Listener")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", self.establish_port))
        s.listen()
        self.logger.info("Waiting to open connection")

        # Main loop
        while not self.kill and not self.connection_established:
            # Get Connection
            (clientConnected, clientAddress) = s.accept()
            data = clientConnected.recv(1024).decode()

            # If message received
            if data == "Bruh, lemme control you with dis joystick!":
                # Set current connection
                self.listener.info(f"Connection Established with {clientAddress}")
                self.connection_established = True
                self.connected_ip = clientAddress
                s.close()

                # Initialize Other Threads
                self.logger.info("Enabling Teleop Server")
                self.command_listener.start()
                self.response_server.start()
                self.log_server.start()

                # Start exit listener in current thread
                self.exitListen()

            # If incorrect message
            else:
                self.logger.info("Invalid/No Connection Request Detected")

        # Close
        self.logger.info("Establish Listener Closed")

    # Listen for a command to kill the connection
    def exitListen(self):
        # Accept Connections
        self.logger.debug("Opening Kill Message Socket")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", self.establish_port))
        s.listen()
        self.logger.info("Waiting for Kill Message")

        # Main Loop
        while self.connection_established and not self.kill:
            # Get Connection
            (clientConnected, clientAddress) = s.accept()
            data = clientConnected.recv(1024).decode()

            # Process message
            if clientAddress == self.connected_ip:
                if data == "I think we need to talk":
                    # Start kill process
                    self.logger.info(f"{self.connected_ip} wants to kill the connection")
                    self.kill(remotely_executed=True)
                
                # Invalid Kill Message
                else:
                    self.logger.info("Invalid Kill Message")

            # Message from external client
            else:
                self.logger.warn(f"{clientAddress} Attempted to Kill {self.connected_ip}'s Connection")

        # Close Socket
        s.close()

    # Kill the server
    def kill(self, remotely_executed = False):
        # Kill
        self.logger.info("Killing Threads")
        self.kill = True

        # Measyre time
        start_time = time.time()

        # Join alive threads
        if not remotely_executed:
            if self.control_listener.is_alive():
                self.logger.info("Control Listener is Still Alive")
                self.control_listener.join()

        if self.command_listener.is_alive():
            self.logger.info("Command Listener is Still Alive")
            self.command_listener.join()

        if self.log_server.is_alive():
            self.logger.info("Log Server is Still Alive")
            self.log_server.join()

        if self.response_server.is_alive():
            self.logger.info("Response Server is Still Alive")
            self.response_server.join()

        # Close
        self.logger.info(f"Threads Killed in {time.time() - start_time}s")
        self.logger.info("Teleop Server Closed")

    # Listens for commands from the drive server
    def commandListener(self):
        self.logger.info("Starting Gamepad Command Listener")

        # Accept Connections
        self.logger.debug("Opening Command Message Socket")
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("", self.command_port))
        s.listen()
        self.logger.info("Waiting for Commands")

        # Main loop
        while self.connection_established and not self.kill:
            # Get Connection
            (clientConnected, clientAddress) = s.accept()
            data = clientConnected.recv(1024).decode()

            # If correct client
            if clientAddress == self.connected_ip:
                # Gamepad Buttons
                if data in self.gamepad.buttons.keys():
                    self.logger.debug(f"Button Pressed: {data}")
                    self.gamepad.buttons[data] = True

                elif ":" in data:
                    # Parse Message
                    action = data[0:data.index(":")]
                    setting = data[data.index(":")+2:len(data)]

                    # Gamepad sticks
                    if action in self.gamepad.sticks.keys():
                        self.logger.debug(f"Stick Changed: {action} to {setting}")
                        self.gamepad.sticks[action] = setting

                    # Gamepad Triggers
                    elif action in self.gamepad.triggers.keys():
                        self.logger.debug(f"Trigger Changed: {action} to {setting}")
                        self.gamepad.triggers[action] = setting

                    # Invalid command
                    else:
                        self.logger.debug(f"Invalid Command: {data}")

                # Invalid command
                else:
                    self.logger.debug(f"Invalid Command: {data}")

            # External client
            else:
                self.logger.warn(f"Command Attempt from {clientAddress}")
        
        # Close
        self.logger.info("Command Listener Closed")

    # Sends log messages
    def logUpdater(self):
        past_message = "No Message"

        # Create Connection
        self.logger.info("Starting Log Updater")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.connected_ip, self.log_port))

        # Main loop
        while self.connection_established and not self.kill:
            # If message changed
            if past_message != self.current_log_message:
                # Set message
                past_message = self.current_log_message

                # Send Message
                s.send(past_message)

        # Close
        self.logger.info("Log Updater Closed")

    # Sends response messages
    def responseUpdater(self):
        past_message = "No Message"

        # Create Connection
        self.logger.info("Starting Reponse Updater")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.connected_ip, self.log_port))

        # Main loop
        while self.connection_established and not self.kill:
            # If message changed
            if past_message != self.current_response_message:
                # Set message
                past_message = self.current_response_message

                # Send Message
                s.send(past_message)

        # Close
        self.logger.info("Response Updater Closed")