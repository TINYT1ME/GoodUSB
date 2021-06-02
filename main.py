import os
import winreg as reg1


# put main.pyw into startup reg
def add_to_registry():
    address1 = "C:\\Program Files\\GoodUSB\\goodUSB.pyw"
    key1 = reg1.HKEY_CURRENT_USER
    key_value1 = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    open_temp = reg1.OpenKey(key1, key_value1, 0, reg1.KEY_ALL_ACCESS)
    reg1.SetValueEx(open_temp, "GoodUSB", 0, reg1.REG_SZ, address1)
    reg1.CloseKey(open_temp)


# rename goodUSB.py to main.pyw
os.rename(
    "GoodUSB/goodUSB.py",
    "GoodUSB/goodUSB.pyw",
)

# make Program Files directory
os.mkdir("C:\\Program Files\\GoodUSB\\", mode=0o777, dir_fd=None)

# move config and main into directory
os.rename(
    "config.json",
    "C:\\Program Files\\GoodUSB\\config.json",
)
os.rename(
    "GoodUSB/goodUSB.pyw",
    "C:\\Program Files\\GoodUSB\\goodUSB.pyw",
)

add_to_registry()
