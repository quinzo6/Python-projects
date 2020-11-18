import pyautogui
import keyboard
import time

time.sleep(5)

while True:
    time.sleep(1)
    keyboard.press('/')
    pyautogui.typewrite('e')
    time.sleep(1)
    keyboard.press('enter')
