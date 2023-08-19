import pyautogui
import keyboard
import random
import time
import win32api
import win32con

IMAGES = ["picture1.png","picture2.png","picture3.png"]
CONFIDENCE = 0.8  # percentage
PAUSE = 2  # seconds
HOTKEYS = {}

KEY_FOR_REGISTERING_POSITION = '1'
KEY_FOR_AUTOMATED_CLICKING = '2'
KEY_FOR_IMAGE_RECOGNITION = '3'

keys = [
    KEY_FOR_REGISTERING_POSITION, 
    KEY_FOR_AUTOMATED_CLICKING,
    KEY_FOR_IMAGE_RECOGNITION 
]

REGISTERED_POSITIONS = []
NR_OF_CLICKS = 1
DELAY_BETWEEN_CLICKS = 0.1
DELAY_BETWEEN_POINTS = 1
DELAY_3 = 1
DELAY_A = 0.5
DELAY_B = 2


def toggleHotkey(key):
    global HOTKEYS
    if key in HOTKEYS:
        del HOTKEYS[key]
    else:
        HOTKEYS[key] = True


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


def init_keyboard_hotkeys():
    for key in keys:
        keyboard.add_hotkey(key, toggleHotkey, args=(key))


def init_main_loop():
    while 1:
        while KEY_FOR_AUTOMATED_CLICKING in HOTKEYS:
            if not REGISTERED_POSITIONS:
                print("NO REGISTERED CLICKS. PLEASE REGISTER CLICKS USING 'W'")
                toggleHotkey(KEY_FOR_AUTOMATED_CLICKING)

            print("CLICKING...")
            for (x,y) in REGISTERED_POSITIONS:
                for _ in range(NR_OF_CLICKS):
                    position_and_click(x, y)
                    time.sleep(DELAY_BETWEEN_CLICKS)
                time.sleep(DELAY_BETWEEN_POINTS)
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

init_keyboard_hotkeys()
init_main_loop()