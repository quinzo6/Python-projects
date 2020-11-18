import keyboard
import pyautogui
import time

time.sleep(3)

while True:
        if keyboard.is_pressed('r'):
            time.sleep(1)
            pyautogui.typewrite("/")
            time.sleep(0.2)
            pyautogui.typewrite("/r")
            keyboard.press("enter")