from flask import Flask, request, jsonify, send_from_directory
from flask_socketio import SocketIO, emit
import pyautogui
import subprocess
import ctypes
import pyperclip
import os

pyautogui.FAILSAFE = False

app = Flask(__name__)
app.config['SECRET_KEY'] = 'codemyst2025'
socketio = SocketIO(app, cors_allowed_origins="*")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'codemyst_control.html')

# ── HTTP Commands (System/Media/Tools) ──
@app.route('/command', methods=['POST'])
def command():
    data = request.get_json()
    cmd = data.get('cmd', '')

    if cmd == 'L':
        ctypes.windll.user32.LockWorkStation()
        msg = '🔒 PC Locked'
    elif cmd == 'SL':
        subprocess.run(['rundll32.exe', 'powrprof.dll,SetSuspendState', '0,1,0'])
        msg = '💤 Sleeping'
    elif cmd == 'SD':
        subprocess.run(['shutdown', '/s', '/t', '5'])
        msg = '⏻ Shutting down in 5s'
    elif cmd == 'VU':
        pyautogui.press('volumeup')
        msg = '🔊 Volume Up'
    elif cmd == 'VD':
        pyautogui.press('volumedown')
        msg = '🔉 Volume Down'
    elif cmd == 'M':
        pyautogui.press('volumemute')
        msg = '🔇 Muted'
    elif cmd == 'PP':
        pyautogui.press('playpause')
        msg = '⏯ Play/Pause'
    elif cmd == 'NEXT':
        pyautogui.press('nexttrack')
        msg = '⏭ Next Track'
    elif cmd == 'PREV':
        pyautogui.press('prevtrack')
        msg = '⏮ Previous Track'
    elif cmd == 'SS':
        pyautogui.hotkey('win', 'prtsc')
        msg = '📸 Screenshot Taken'
    elif cmd == 'TASKMAN':
        pyautogui.hotkey('ctrl', 'shift', 'esc')
        msg = '📊 Task Manager'
    else:
        msg = '❓ Unknown'

    print(f"[CMD] {cmd} → {msg}")
    return jsonify({'message': msg})

# ── HTTP Clipboard ──
@app.route('/clipboard', methods=['POST'])
def clipboard():
    data = request.get_json()
    text = data.get('text', '')
    pyperclip.copy(text)
    print(f"[CLIP] {text[:40]}")
    return jsonify({'message': '📋 Copied to clipboard'})

# ── WebSocket: Real-time keyboard ──
@socketio.on('connect')
def on_connect():
    print("[WS] Phone connected!")
    emit('status', {'msg': 'connected'})

@socketio.on('disconnect')
def on_disconnect():
    print("[WS] Phone disconnected")

@socketio.on('key')
def on_key(data):
    keys = data.get('keys', [])
    if not keys:
        return
    try:
        if len(keys) == 1:
            pyautogui.press(keys[0])
        else:
            pyautogui.hotkey(*keys)
        print(f"[KEY] {'+'.join(keys).upper()}")
    except Exception as e:
        print(f"[KEY ERROR] {e}")

@socketio.on('type')
def on_type(data):
    text = data.get('text', '')
    if not text:
        return
    try:
        old = pyperclip.paste()
        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy(old)
        print(f"[TYPE] {text}")
    except Exception as e:
        print(f"[TYPE ERROR] {e}")

if __name__ == '__main__':
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print("=" * 45)
    print("   CODEMYST PC CONTROL SERVER")
    print("=" * 45)
    print(f"   Local:   http://localhost:5000")
    print(f"   Phone:   http://{local_ip}:5000")
    print("=" * 45)
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)
