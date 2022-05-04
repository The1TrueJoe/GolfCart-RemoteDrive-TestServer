# Drive Computer
# Control Definition
#
# Part of the GSSM Autonomous Golf Cart
# Written by:
#   Benjamin Chauhan, class of 2022
#   Joseph Telaak, class of 2022

class Gamepad:
    # Controller Buttons
    buttons = {
        'BTN_TL': False,
        'BTN_TR': False,
        'BTN_NORTH': False,
        'BTN_EAST': False,
        'BTN_SOUTH': False,
        'BTN_WEST': False,
        'BTN_THUMBL': False,
        'BTN_THUMBR': False,
        'BTN_START': False,
        'BTN_SELECT': False,
        'DPAD_NORTH': False,
        'DPAD_SOUTH': False,
        'DPAD_EAST': False,
        'DPAD_WEST': False
    }

    # Controller Sticks
    sticks = {
        'LSTICK_X': 0.0,
        'LSTICK_Y': 0.0,
        'RSTICK_X': 0.0,
        'RSTICK_Y': 0.0
    }

    # Controller Triggers
    triggers = {
        'ABS_Z': 0.0,
        'ABS_RZ': 0.0
    }