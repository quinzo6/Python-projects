import pyautogui 
import keyboard 
import time 

time.sleep(5)

text = open("text\shrek.txt", "r")

for word in text:
    keyboard.press('/') 
    time.sleep(.3)
    pyautogui.typewrite(word)
    keyboard.press('enter')
    time.sleep(2)