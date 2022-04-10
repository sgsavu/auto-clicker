from ast import arg
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

IMAGES = ["picture1.png","picture2.png","picture3.png"]
CONFIDENCE = 0.8  # percentage
PAUSE = 2  # seconds
HOTKEYS = {}
keys = ["q", "w", "e", "r"]

KEY_FOR_IMAGE_RECOGNITION = 'q'
KEY_FOR_REGISTERING_POSITION = 'w'
KEY_FOR_AUTOMATED_CLICKING = 'e'

REGISTERED_POSITIONS = []
NR_OF_CLICKS = 1
DELAY_1 = 0.1
DELAY_2 = 1
DELAY_3 = 1
DELAY_A = 0.5
DELAY_B = 2


def toggleHotkey(key):
    global HOTKEYS
    if key in HOTKEYS:
        del HOTKEYS[key]
    else:
        HOTKEYS[key] = True


for key in keys:
    keyboard.add_hotkey(key, toggleHotkey, args=(key))


def position_and_click(x, y):
    position(x, y)
    click()


def position(x, y):
    win32api.SetCursorPos((x, y))


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def getCursorPosition():
    position = win32api.GetCursorPos()
    return position[0], position[1]


def getCenter(box):
    return pyautogui.center(box)


def image_based_recognition():
    for image in IMAGES:
        box = pyautogui.locateOnScreen(image, confidence=CONFIDENCE)
        if box != None:
            print("I can see ", image)
            center = getCenter(box)
            position_and_click(center.x, center.y)
        time.sleep (DELAY_A)
    time.sleep(DELAY_B)


while 1:

    while KEY_FOR_AUTOMATED_CLICKING in HOTKEYS:
        print("CLICKING...")
        if not REGISTERED_POSITIONS:
            print("NO REGISTERED CLICKS. PLEASE REGISTER CLICKS USING 'W'")
            toggleHotkey(KEY_FOR_AUTOMATED_CLICKING)

        for point in REGISTERED_POSITIONS:
            for number in range(NR_OF_CLICKS):
                position_and_click(point[0], point[1])
                time.sleep(DELAY_1)
            time.sleep(DELAY_2)
        time.sleep(DELAY_3)

    while KEY_FOR_REGISTERING_POSITION in HOTKEYS:
        a = win32api.GetKeyState(0x01)
        if a < 0:
            (x, y) = getCursorPosition()
            REGISTERED_POSITIONS.append((x, y))
            toggleHotkey(KEY_FOR_REGISTERING_POSITION)
            print(REGISTERED_POSITIONS)
    while KEY_FOR_IMAGE_RECOGNITION in HOTKEYS:
        image_based_recognition()
