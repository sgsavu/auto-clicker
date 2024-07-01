import pyautogui

KEY_FOR_REGISTERING_POSITION = '1'
KEY_FOR_AUTOMATED_CLICKING = '2'

NR_OF_CLICKS = 1
DELAY_BETWEEN_NR_CLICKS = 0.1
DELAY_BETWEEN_POINTS = 1
DELAY_BETWEEN_CLICKS = 1

REGISTERED_POSITIONS = []

def position_and_click(x, y):
    position(x, y)
    click()


def position(x, y):
    pyautogui.moveTo(x, y)


def click():
    pyautogui.click()


def getCursorPosition():
    position = pyautogui.position()
    return position[0], position[1]

def init_main_loop():
    while 1:
        mode = input('Please choose an action:\n{0} - Register click position\n{1} - Start clicking\n'.format(KEY_FOR_REGISTERING_POSITION, KEY_FOR_AUTOMATED_CLICKING))

        while mode == KEY_FOR_AUTOMATED_CLICKING:
            if not REGISTERED_POSITIONS:
                print("NO REGISTERED CLICKS. PLEASE REGISTER AT LEAST 1 CLICK POSITION")
                mode = None
                break

            print("CLICKING...")
            for (x,y) in REGISTERED_POSITIONS:
                for _ in range(NR_OF_CLICKS):
                    position_and_click(x, y)
                    pyautogui.sleep(DELAY_BETWEEN_NR_CLICKS)
                pyautogui.sleep(DELAY_BETWEEN_POINTS)
            pyautogui.sleep(DELAY_BETWEEN_CLICKS)

        while mode == KEY_FOR_REGISTERING_POSITION:
            print('REGISTERING POSITION...')
            (x, y) = getCursorPosition()
            REGISTERED_POSITIONS.append((x, y))
            print(REGISTERED_POSITIONS)
            mode = None

init_main_loop()