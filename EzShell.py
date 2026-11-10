import requests, os, time, ctypes, subprocess
from ctypes import wintypes
from wakepy import keep

# the idle detector:
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [('cbSize', wintypes.UINT), ('dwTime', wintypes.DWORD)]
def get_idle_ms():
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(lii)
    user32.GetLastInputInfo(ctypes.byref(lii))
    return kernel32.GetTickCount64() - lii.dwTime

API_URL = ''
KEY = '' 

def get():
    try:
        response = requests.get(API_URL, headers={'api-key': KEY}, timeout=5)
        return response.json()
    except requests.RequestException as e:
        return {}

def update(change: str, new):
    try:
        requests.patch(API_URL, headers={'api-key': KEY, 'Content-Type': 'application/json'}, json={change: new}, timeout=5)
    except requests.RequestException as e:
        return

while True:
    with keep.running():
        currData = get()
        

