import pyautogui
import keyboard
import time
import winsound

while True:
    if pyautogui.locateOnScreen(r"images\OKLOL.png", r"images\YES.png", confidence=0.95) != None:
        winsound.PlaySound("Ding Sound Effect.wav", winsound.SND_FILENAME)