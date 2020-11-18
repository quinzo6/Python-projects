# Test code, replace images with custom image files

import pyautogui
import keyboard
import time
import winsound

while True:
    if pyautogui.locateOnScreen(r"images\Was_Filled.png", confidence=0.6) != None:
        winsound.PlaySound("Ding Sound Effect.wav", winsound.SND_FILENAME)