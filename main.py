import time
import json
import os

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
delete = config[mode]["delete"]
logfile = config[mode]["logfile"]

# Defining variables
last_key = time.time()
history_array = []
caught = False
timing = None


# Gets called for each keystroke
def KeyDown(event):
    global last_key, mode, history, threshold, timeout, history_array
    global caught, hm

    time_diff = -1 * (last_key - time.time())
    history_array.append(time_diff)

    if caught:
        return found(event)
    elif len(history_array) > history and not caught:
        history_array.pop(0)
        time_total = sum(history_array) / history

        if time_total < threshold:
            last_key = time.time()
            print("CAUGHT!!!")
            return found(event)
        else:
            last_key = time.time()
            return True
    else:
        last_key = time.time()
        return True


def found(event):
    global mode, timeout, caught, timing
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
    elif mode == "interested":
        if not timing:
            timing = time.time()
        elif (time.time() - timing) >= timeout:
            caught = False
            return True
        log(event)

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
