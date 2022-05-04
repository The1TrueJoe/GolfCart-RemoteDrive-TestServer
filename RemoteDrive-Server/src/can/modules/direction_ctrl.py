import can_util as util
import cart_module as m
import logging

# Drive Computer Core Library
# Direction Controller Module
#
# This module controls both steering and braking
#
# Hardware definition class to store messages for this module
#
# Part of the GSSM Autonomous Golf Cart
# Written by Joseph Telaak, class of 2022

class Direction_Controller:

    def __int__(self, can_address = 1):
        # CAN Address
        self.can_address = can_address

        # Setup the message logging
        self.logger = logging.getLogger("direction_controller")
        file_handler = logging.FileHandler("logs/direction_ctrl.log")
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        self.logger.addHandler(file_handler)

        # Components
        self.steering_motor = self.Steering_Motor(can_address=self.can_address, logger=self.logger)
        self.steering_mode = self.Steering_Mode(can_address=self.can_address, logger=self.logger)
        self.wheel_input = self.Wheel(can_address=self.can_address, logger=self.logger)
        self.brake_motor = self.Brake_Motor(can_address=self.can_address, logger=self.logger)

    # Check if the ready message is received
    def isReady(self, message):
        if util.removeID(message) == m.ready_message:
            self.logger.info("Module is Ready")
            return True

        else:
            return False

    # Send the Module Enable Message
    def enable(self):
        self.logger.info("Sending Module Enable Message")
        return f"({self.can_address}) {m.enable_message}"

    
    # ----------------------------
    # Steering Motor Controller
    # ----------------------------

    class Steering_Motor:

        def __init__(self, can_address, logger):
            self.can_address = can_address
            self.logger = logger

        # Disable Steering Motor
        def disable(self):
            self.logger.debug("Disabling Steering Motor")
            return f"({self.can_address}) {m.set} 1 10 1 {m.fill(4)}"

        # Enable Steering Motor
        def enable(self):
            self.logger.debug("Enabling Steering Motor")
            return f"({self.can_address}) {m.set} 1 10 2 {m.fill(4)}"

        def reqStatus(self):
            self.logger.debug("Requesting the Steering Motor Status")
            return f"({self.can_address}) {m.get} 1 10 {m.fill(5)}"

        def checkStatusResponse(self, message):
            pass
    
        def readStatus(self, message):
            pass

        # Run Motor Forwards
        def forwards(self, power = 255):
            self.logger.debug(f"Running Steering Motor Forwards, Power: {power}")
            return f"({self.can_address}) {m.set} 1 12 1 {power} {m.fill(3)}"

        # Run Motor Backwards
        def backwards(self, power = 255):
            self.logger.debug(f"Running Steering Motor Backwards, Power: {power}")
            return f"({self.can_address}) {m.set} 1 12 2 {power} {m.fill(3)}"

        # Run the motor to the position
        def setPos(self, pos):
            self.logger.debug(f"Running Steering Motor to Position, Pos: {pos}")
            return f"({self.can_address}) {m.op} 1 {util.sixteentoeight(pos)[0]} {util.sixteentoeight(pos)[1]} {m.fill(3)}"

        # Request the steering motor position
        def reqPos(self):
            self.logger.debug("Requesting to Current Steering Motor Position")
            return f"({self.can_address}) {m.get} 1 16 {m.fill(5)}"
    
    # ----------------------------
    # Steering Mode
    # ----------------------------

    class Steering_Mode:

        def __init__(self, can_address, logger):
            self.can_address = can_address
            self.logger = logger

        # Set to computer controlled steering
        def setControlledSteering(self):
            self.logger.debug("Set to Controlled Steering")
            return f"({self.can_address}) {m.set} 1 13 2 {m.fill(4)}"

        # Set to wheel input steering
        def setWheelInputSteering(self):
            self.logger.debug("Set to Wheel Input Steering")
            return f"({self.can_address}) {m.set} 1 13 1 {m.fill(4)}"

        # Requesting steering mode
        def reqSteeringMode(self):
            self.logger.debug("Requesting Steering Mode")
            return f"({self.can_address}) {m.get} 1 13 {m.fill(5)}"

    # ----------------------------
    # Steering Wheel Input
    # ----------------------------

    class Wheel:

        def __init__(self, can_address, logger):
            self.can_address = can_address
            self.logger = logger

        def getPos(self):
            pass

        def setSpeed(self, power = 128):
            pass

    class Brake_Motor:

        def __init__(self, can_address, logger):
            self.can_address = can_address
            self.logger = logger

        def disable(self):
            pass

        def enable(self):
            pass

        def reqStatus(self):
            pass

        def checkStatusResponse(self, message):
            pass
    
        def readStatus(self, message):
            pass

        def forwards(self, power = 255):
            pass

        def backwards(self, power = 255):
            pass

        def resetEncoder(self):
            pass

        def reqEncoderTicks(self):
            pass

        def checkTicksResponse(self, message):
            pass
    
        def readTicks(self, message):
            pass