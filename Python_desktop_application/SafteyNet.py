import pynput 
import ctypes
import os
import time
from win32gui import GetWindowText, GetForegroundWindow
from pynput.keyboard import Key, Listener
from win10toast import ToastNotifier

#########https://www.geeksforgeeks.org/how-to-use-pynput-to-make-a-keylogger/
#########https://stackoverflow.com/questions/34514644/in-python-3-how-can-i-tell-if-windows-is-locked
#########https://www.devdungeon.com/content/windows-desktop-notifications-python
compare_keywords = []
keys = ""
mistakes = 0
# One-time initialization
toaster = ToastNotifier()

def is_pc_locked():
    print("is_pc_locked")
    global mistakes
    mistakes += 1
    if mistakes >= 2:
        print("Mistakes: ", mistakes)
        for x in range(5):
          time.sleep(5)
          print("is the pc locked?")
          if(GetWindowText(GetForegroundWindow()) == "Windows Default Lock Screen"):
              print("PC is Locked")
          else:
              print("PC is Not Locked Locking PC")
              lock_pc()
        print("Time is up no longer locking PC")
        mistakes = 1  
    else:
        print("Mistakes: ", mistakes)
        lock_pc()

def lock_pc():
    print("lock_pc")
    # Show notification whenever needed
    toaster.show_toast("We've detected a keyword",
                       "First time detection will give you a second chance after that you will have to wait 5 minutes.",
                       threaded=True, icon_path=None, duration=30)  # 30 seconds
    os.system("taskkill /im chrome.exe /f")
    if mistakes >= 2:
        ctypes.windll.user32.LockWorkStation()

def compare_typing():
    print("compare_typing")    
    global keys
    keys = keys.replace("'", "")
    keys = keys.upper()
    i = 0
    length = len(compare_keywords) - 1
    while i<=length:
        if compare_keywords[i] in keys:
            is_pc_locked()
        i += 1
    keys = ''

def on_press(key):
    print("on_press")
    global keys
    if key == Key.enter:
        compare_typing()
    elif key == Key.space:    
        compare_typing()
    elif key == Key.esc: 
        return False
    elif len(keys) > 50:
        compare_typing()
    else:
        keys += str(key)

with Listener(on_press = on_press) as listener: 
    compare_keywords = open("keywords.log", "r").read().split('\n')
    listener.join()
