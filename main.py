import json
import keyboard
import os
import time
from random import randint

import pyWinhook
import pythoncom

# Getting configuration
with open('config.json', 'r') as f:
    config = json.load(f)
mode = config["mode"]
history = config[mode]["history"]
threshold = config[mode]["threshold"]
timeout = config[mode]["timeout"]
shutdown = config[mode]["shutdown"]
sneak = config[mode]["sneak"]
logfile = config[mode]["logfile"]

# Defining variables
last_key = time.time()
history_array = []
caught = False
timing = None
pick = None
current = 0


# Gets called for each keystroke
def KeyDown(event):
    global last_key, mode, history, threshold, timeout, history_array
    global caught, hm

    # getting time diff
    time_diff = -1 * (last_key - time.time())
    history_array.append(time_diff)

    # check if caught
    if caught:
        return found(event)
    elif len(history_array) > history and not caught:
        history_array.pop(0)
        time_total = sum(history_array) / history

        if time_total < threshold:
            last_key = time.time()
            return found(event)
        else:
            last_key = time.time()
            return True
    else:
        last_key = time.time()
        return True


def found(event):
    global mode, timeout, caught, timing, sneak, pick
    global current
    caught = True

    # if mode is standard, timeout for x seconds
    if mode == "standard":
        if not timing:
            timing = time.time()
        elif (time.time() - timing) >= timeout:
            caught = False
            return True
    # if mode is secure, shutdown pc
    elif mode == "secure":
        if shutdown:
            os.system("shutdown /s /t 0")
    # if mode is quiet, sneak keys in
    elif mode == "quiet":
        current += 1
        if not timing:
            timing = time.time()
        elif (time.time() - timing) >= timeout:
            caught = False
            return True
        # send keys randomly depending on sneak value
        if not pick:
            pick = randint(round(sneak/2), sneak)
        elif current == pick:
            keyboard.send('\b')
            pick = randint(round(sneak/2), sneak)
            current = 0
        return True
    # if mode is interested, send keys to logfile
    elif mode == "interested":
        if not timing:
            timing = time.time()
        elif (time.time() - timing) >= timeout:
            caught = False
            return True
        log(event)

    # block keyboard input
    return False


# log input
def log(event):
    global logfile

    with open(logfile, 'a+') as file:
        if event.Key == "Space":
            file.write(" ")
        else:
            file.write(event.Key)
        file.close()


# Declaring hook manager
hm = pyWinhook.HookManager()
# To block keyboard
hm.KeyDown = KeyDown
# Set the hook
hm.HookKeyboard()
# Wait forever
pythoncom.PumpMessages()
