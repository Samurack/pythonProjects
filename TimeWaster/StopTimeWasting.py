import os
from pynput.keyboard import Key, Listener
from win10toast import ToastNotifier
######################################################################################################
# code references used
# https://www.geeksforgeeks.org/how-to-use-pynput-to-make-a-keylogger/
# https://stackoverflow.com/questions/34514644/in-python-3-how-can-i-tell-if-windows-is-locked
# https://www.devdungeon.com/content/windows-desktop-notifications-python
######################################################################################################

compare_keywords = []
keys = ""
mistakes = 0

# One-time initialization
toaster = ToastNotifier()

def kill_browser_task():
    """find any open browser for the given browser type
       and kill it using task manager
    """
    print("kill_browser_task")
    # Show notification whenever needed
    toaster.show_toast("We've detected a keyword",
                       "Sorry to have to kill your browsers",
                       threaded=True, icon_path=None, duration=30)  # 30 seconds
    os.system("taskkill /im brave.exe /f")

def compare_typing():
    """compare what the user is typing to a list of 
       key words. If a specific word is detected 
       call the kill_browser_task
    """
    print("compare_typing")
    global keys
    keys = keys.replace("'", "")
    keys = keys.upper()
    i = 0
    length = len(compare_keywords) - 1
    print(keys)
    while i<=length:
        if compare_keywords[i] in keys:
            kill_browser_task()
        i += 1
    keys = ''

def on_press(key):
    """record key strokes then call compare_typing
       when specific cases are met

    Parameters
    ----------
    key : str
        the keystrokes a user typed
    """
    print("on_press")
    global keys
    if key == Key.enter:
        compare_typing()
    elif key == Key.space:
        compare_typing()
    elif key == Key.esc: #End the program
        return False
    elif len(keys) > 50:
        compare_typing()
    else:
        keys += str(key)

with Listener(on_press = on_press) as listener:
    """listens for keystrokes during all computer processes
    """
    compare_keywords = open("keywords.log", "r").read().split('\n')
    listener.join()
