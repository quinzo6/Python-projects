import pyautogui
import keyboard

while True:
     if pyautogui.locateOnScreen(r"images\hotdog.png", confidence=0.9) != None:
        print("HotDog Found!")
