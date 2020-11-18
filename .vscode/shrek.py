import pyautogui
import time

time.sleep(3)

Text = open("text\Shrek.txt", "r")

for word in Text:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(2)