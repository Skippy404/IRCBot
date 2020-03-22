# Debugging utilities
#
# As soon as this is imported (which means that
# Python will run the script) the environment
# variable "RR_DEBUG" will be checked and if set to
# 1 then debugging will be enabled meaning that
# the dprint function will output to fd 0.

import os

isDebuggingEnabled = False

def dprint(text):
    if globals()["isDebuggingEnabled"]: print("[Debug]: " + str(text))

def initialize():
    # Check for the environment variable
    if os.getenv("RR_DEBUG") == "1":
        globals()["isDebuggingEnabled"] = True
        dprint("Debugging enabled")

initialize()