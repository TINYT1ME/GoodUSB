import time

import pyWinhook
import pythoncom

last_key = time.time()


def keyboard_event(event):
    global last_key
    time_diff = -1 * (last_key - time.time())
    if time_diff < 0.003:
        last_key = time.time()
        return False
    else:
        last_key = time.time()
        return True


# create a hook manager object
hm = pyWinhook.HookManager()
# to block keyboard
hm.KeyDown = keyboard_event

# set the hook
hm.KeyAll = keyboard_event
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
