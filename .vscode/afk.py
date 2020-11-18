import keyboard
import pyautogui
import time

Time_input = input('How long will you be afk for? (Please enter a integer): ')
print('Ok, Starting the script!')

time.sleep(5)

pyautogui.click(563, 1057)

while True:
    if pyautogui.locateOnScreen(r"images\afk.png", confidence=0.3) != None:
        time.sleep(1)
        pyautogui.click(1660, 975)
        time.sleep(1)
        pyautogui.typewrite('Hello, I am afk right now. I will respond to you in around ' + Time_input + ' minutes!')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(563, 1057)