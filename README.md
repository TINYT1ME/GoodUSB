<h1 align="center">
  <a href="https://github.com/TINYT1ME/GoodUSB/"><img src="https://i.postimg.cc/T30VtMdW/goodusb.png" width="400" title="goodusb"></a>
</h1>

[![GitHub's Super Linter](https://github.com/TINYT1ME/GoodUSB/workflows/GitHub's%20Super%20Linter/badge.svg)](https://github.com/TINYT1ME/GoodUSB/actions) [![platforms](https://img.shields.io/badge/platforms-Windows-success.svg)](https://github.com/TINYT1ME/GoodUSB/actions)
<br>
**GoodUSB** is a program that prevents attacks from badUSB's such as: [usb-rubber-ducky](https://shop.hak5.org/products/usb-rubber-ducky-deluxe), [malduino](https://maltronics.com/products/malduino), and many more.

---

## :page_with_curl: Table of Content

- [Table of Content](#page_with_curl-Table-of-Content)
- [Features](#green_circle-Features)
  - [Modes](#gear-Modes)
- [Installation](#package-Installation)
  - [Requirements](#point_down-Requirements)
- [Future](#alien-Future)

---

## :green_circle: Features

- :keyboard: Detects keyboard input
- :stop_sign: If keyboard is typing too fast, act upon information
- :mechanical_arm: Has ability to:
  - lock keyboard
  - shutdown PC
  - log attack
  - sabatoge attack

---

### :gear: Modes

| Mode                              | Description                              |
| --------------------------------- | ---------------------------------------- |
| :lock: **Standard**               | Lock keyboard for **x** seconds          |
| :closed_lock_with_key: **Secure** | Shutdown PC                              |
| :sound: **Quiet**                 | Sneak key every random(**x**) key inputs |
| :detective: **Interested**        | Log attack into **logfile**              |

---

## :package: Installation

- 🔴 MAKE SURE TO OPEN CMD IN ADMINISTRATOR
- 1️⃣ `git clone https://github.com/TINYT1ME/GoodUSB`
- 2️⃣ `cd GoodUSB & python setup.py`

---

### :point_down: Requirements

- [PyWinhook](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pywinhook)
- [pythoncom](https://pypi.org/project/pythoncom/)
- [keyboard](https://pypi.org/project/keyboard/)

---

### :alien: Future

- Compatibility: Mac, Linux
- Include more modes
- Include custom mode

---

### :link: Similar open source projects

- [BadUSB-Kill-Switch](https://github.com/ONLYA/BadUSB-Kill-Switch) by ONLYA
- [duckhunt](https://github.com/pmsosa/duckhunt) by pmsosa
- [BadUSB-Detection](https://github.com/armoured-ape/BadUSB-Detection) by armoured-ape

---
