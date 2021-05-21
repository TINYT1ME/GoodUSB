import os
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# download all needed libraries
install("pyWinhook-1.6.2-cp39-cp39-win_amd64.whl")
install("pythoncom")
install("keyboard")

# move main and config to startup folder
os.rename(
    "main.py",
    "C:/ProgramData/Microsoft/" "Windows/Start Menu/Programs/StartUp/main.pyw",
)

os.mkdir("C:/Program Files/GoodUSB/", mode=0o777, dir_fd=None)
os.rename(
    "config.json",
    "C:/Program Files/GoodUSB/config.json",
)
