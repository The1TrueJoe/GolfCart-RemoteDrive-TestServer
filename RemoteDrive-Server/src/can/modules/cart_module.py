# Drive Computer Core Library
# Module Utilites
#
# Utilites in building the hex codes for the can messages
#
# Part of the GSSM Autonomous Golf Cart
# Written by Joseph Telaak, class of 2022

# Set operation
set = "10"

# Operation
op = "11"

# Get request
get = "12"

# Data Length
dlc = 8

# Enable Message
enable_message = "170 171 172 173 174 160 161 162"
ready_message = "170 170 170 170 170 170 170 170"

# Fill the rest of the message with zeroes
def fill(count):
    filled = ""
    
    for i in range(count + 1):
        filled += "0 "

    return filled.substring(0, len(filled) - 1)

# Splits the message into its components
def splitMessage(message):
    return message.split(" ")

# Checks if the message is a response
def isResponseMessage(split_message):
    if len(split_message) != 8:
        return False

    else:
        if split_message[0] == get and split_message[1] == get:
            return True

        else:
            return False

# Checks if the message is a response
def isResponseMessage(incoming_message, expected_message):
    expected_message = splitMessage(expected_message)
    incoming_message = splitMessage(incoming_message)

    for i in expected_message:
        if expected_message[i] != incoming_message[i]:
            return False

    return True

# Interprets message if the byte is a boolean condition
def getAsBoolean(message_byte):
    if (message_byte == 1):
        return True

    else:
        return False