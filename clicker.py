from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

IMAGE = "picture.png"
CONFIDENCE = 0.8  # percentage
PAUSE = 2  # seconds
HOTKEY_TOGGLE = False
HOTKEY = "q"

keyboard.add_hotkey(HOTKEY, lambda: toggleHotkey())

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def getCenter(box):
    return pyautogui.center(box)

def toggleHotkey():
    global HOTKEY_TOGGLE
    HOTKEY_TOGGLE = not HOTKEY_TOGGLE
    print(HOTKEY_TOGGLE)

def image_based_recognition():
    box = pyautogui.locateOnScreen(IMAGE, confidence=CONFIDENCE)
    if box != None:
        print("I can see it")
        center = getCenter(box)
        click(center.x, center.y)
        time.sleep(PAUSE)
    else:
        print("I am unable to see it")
        time.sleep(0.5)

while 1:
    while HOTKEY_TOGGLE:
        image_based_recognition()
