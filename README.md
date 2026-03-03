# 🖥️ Codemyst PC Control

> Control your PC from your phone using Python, Flask & WebSocket — built as a better alternative to Microsoft's Link to Windows.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?style=flat-square&logo=flask)
![WebSocket](https://img.shields.io/badge/WebSocket-Real--time-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## ✨ Features

| Feature | Link to Windows | Codemyst PC Control |
|---|---|---|
| 🔒 Lock PC | ✅ | ✅ |
| 🔊 Volume Control | ❌ | ✅ |
| 🎵 Media Control | ❌ | ✅ |
| ⌨️ Wireless Keyboard | ❌ | ✅ |
| 📋 Clipboard Share | ❌ | ✅ |
| 📸 Screenshot | ❌ | ✅ |
| 📊 Task Manager | ❌ | ✅ |
| 💤 Sleep / Shutdown | ❌ | ✅ |

---

## 📋 Requirements

```bash
pip install flask flask-socketio pyautogui pyperclip
```

---

## 🚀 How to Run

**Step 1** — Clone this repository:
```bash
git clone https://github.com/ibn-munir/codemyst-pc-control.git
cd codemyst-pc-control
```

**Step 2** — Install dependencies:
```bash
pip install flask flask-socketio pyautogui pyperclip
```

**Step 3** — Run the server:
```bash
python server.py
```

**Step 4** — Open your phone browser and go to:
```
http://YOUR_PC_IP:5000
```
> Your PC IP will be shown in the terminal when you run the server.

**Step 5** — Make sure your phone and PC are on the **same WiFi network**.

---

## 📱 How to Use

### System Tab
- **Lock** — Locks your PC instantly
- **Sleep** — Puts PC to sleep
- **Shutdown** — Shuts down PC after 5 seconds

### Media Tab
- Control volume, play/pause, next/previous track

### Keyboard Tab
- **Modifier keys** — Ctrl, Shift, Alt, Win (supports combos like Ctrl+C, Win+V)
- **Special keys** — Esc, Tab, Caps Lock, Enter, Backspace, Delete, Home, End, F1-F12
- **QWERTY keyboard** — Real-time typing on PC from phone (no Send button needed!)
- **Arrow keys** — Navigate with ↑↓←→

### Clipboard Tab
- Type or paste text on your phone → instantly copied to PC clipboard → Ctrl+V to paste

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-SocketIO
- **Frontend:** HTML, CSS, JavaScript
- **Real-time:** WebSocket (Socket.IO)
- **PC Control:** PyAutoGUI, PyPerclip, ctypes

---

## ⚠️ Notes

- Works on **Windows only** (uses Windows API for locking)
- Phone and PC must be on the **same WiFi network**
- Run as **administrator** if some keys don't work

---

## 👨‍💻 Made by

**Rakibul Haque** — [Codemyst](https://github.com/ibn-munir)

> *"Built this because Microsoft's Link to Windows can only lock your screen. Mine does much more."*

---

## ⭐ If this helped you, give it a star!
