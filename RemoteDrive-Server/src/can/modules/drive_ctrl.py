import can_util as util
import cart_module as m
import logging

# Drive Computer Core Library
# Speed Controller Module
#
# This module controls the cart's built-in speed controller.
# Controls:
#   Acceleration
#   Fwd/Rev
#   Motor Control Enable
#
# Hardware definition class to store messages for this module
#
# Part of the GSSM Autonomous Golf Cart
# Written by Joseph Telaak, class of 2022

class Drive_Controller:

    def __int__(self, can_address = 3):
        # CAN Address
        self.can_address = can_address

        # Components
        self.digital_accelerator = self.Digital_Accelerator(can_address=self.can_address)
        self.direction_controller = self.Direction_Controller(can_address=self.can_address)
        self.input_mode_controller = self.Input_Mode(can_address=self.can_address)
        self.enabler = self.Enable(can_address=self.can_address)
        self.auto_buzzer_mode = self.Auto_Buzzer(can_address=self.can_address)

        # Setup the message logging
        self.logger = logging.getLogger("drive_controller")
        file_handler = logging.FileHandler("logs/drive_ctrl.log")
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        self.logger.addHandler(file_handler)


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

    class Digital_Accelerator:
        
        def __init__(self, can_address):
            self.can_address = can_address

        def setPotPos(self, pos):
            pass

        def increment(self):
            pass

        def decrement(self):
            pass

        def reqPos(self):
            pass

        def checkPosResponse(self, message):
            pass

        def readPosResponse(self, message):
            pass

    class Direction_Controller:

        def __init__(self, can_address):
            self.can_address = can_address

        def reverse(self):
                pass

        def forwards(self):
            pass

        def reqDirection(self):
            pass

        def checkDirectionResponse(self, message):
            pass

        def isForwards(self, message):
            pass

        def isReverse(self, message):
            pass

    class Input_Mode:

        def __init__(self, can_address):
            self.can_address = can_address

        def manual(self):
            pass

        def computer(self):
            pass

        def reqMode(self):
            pass

        def checkModeResponse(self, message):
            pass

        def isManual(self, message):
            pass

        def isComputer(self, message):
            pass

    class Enable:

        def __init__(self, can_address):
            self.can_address = can_address

        def enable(self):
            pass

        def disable(self):
            pass

        def reqStatus(self):
            pass

        def checkStatusResponse(self, message):
            pass

        def isEnabled(self, message):
            pass

    class Auto_Buzzer:

        def __init__(self, can_address):
            self.can_address = can_address

        def enable(self):
            pass

        def disable(self):
            pass

        def reqStatus(self):
            pass

        def checkStatusResponse(self, message):
            pass

        def isEnabled(self, message):
            pass
