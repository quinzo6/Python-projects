# Discord status changer, dont bully me

import pyautogui
import time
import keyboard

status = input('What do you want to change your status to? ')

if status == 'dnd':
    pyautogui.click(610, 1059)
    pyautogui.click(92, 1010)
    time.sleep(.5)
    pyautogui.click(171, 806)
    print('Your status was changed to ' + status + '!')
    exit()

if status == 'idle':
    pyautogui.click(610, 1059)
    pyautogui.click(92, 1010)
    time.sleep(.5)
    pyautogui.click(152, 759)
    print('Your status was changed to ' + status + '!')
    exit()

if status == 'online':
    pyautogui.click(610, 1059)
    pyautogui.click(92, 1010)
    time.sleep(.5)
    pyautogui.click(150, 719)
    print('Your status was changed to ' + status + '!')
    exit()

if status == 'invis':
    pyautogui.click(610, 1059)
    pyautogui.click(92, 1010)
    time.sleep(.5)
    pyautogui.click(167, 883)
    print('Your status was changed to ' + status + '!')
    exit()

if status == 'custom':
    pyautogui.click(610, 1059)
    pyautogui.click(92, 1010)
    time.sleep(.5)
    pyautogui.click(165, 951)
    time.sleep(.5)
    pyautogui.click(1143, 489)
    pyautogui.click(760, 1056)
    custom_status = input('What  do you want your custom status to be? ')
    time.sleep(.5)
    pyautogui.click(606, 1057)
    time.sleep(.5)
    pyautogui.click(1037, 497)
    pyautogui.typewrite(custom_status)
    pyautogui.click(757, 1058)
    clear_after = input('When do you want to clear your status? (today, in 4h, in 1h, in 30m, or dont) ')


    if clear_after == 'today':
        pyautogui.click(614, 1062)
        time.sleep(.5)
        pyautogui.click(1031, 584)
        time.sleep(.5)
        pyautogui.click(1106, 615)
        time.sleep(.5)
        pyautogui.click(1014, 616)
        time.sleep(.5)
        pyautogui.click(1111, 655)
        time.sleep(.5)
        pyautogui.click(756, 1061)
        print('Your custom status was changed to ' + status + ' and will be cleared after ' + clear_after + '!')
        exit()

    if clear_after == '4h':
        pyautogui.click(614, 1062)
        time.sleep(.5)
        pyautogui.click(1031, 584)
        time.sleep(.5)
        pyautogui.click(895, 653)
        time.sleep(.5)
        pyautogui.click(1106, 650)
        time.sleep(.5)
        pyautogui.click(1111, 655)
        time.sleep(.5)
        pyautogui.click(756, 1061)
        print('Your custom status was changed to ' + status + ' and will be cleared after ' + clear_after + '!')
        exit()

    if clear_after == '1h':
        pyautogui.click(614, 1062)
        time.sleep(.5)
        pyautogui.click(1031, 584)
        time.sleep(.5)
        pyautogui.click(944, 687)
        time.sleep(.5)
        pyautogui.click(1106, 650)
        time.sleep(.5)
        pyautogui.click(978, 695)
        time.sleep(.5)
        pyautogui.click(756, 1061)
        print('Your custom status was changed to ' + status + ' and will be cleared after ' + clear_after + '!')
        exit()

    if clear_after == '30m':
        pyautogui.click(614, 1062)
        time.sleep(.5)
        pyautogui.click(1031, 584)
        time.sleep(.5)
        pyautogui.click(1106, 733)
        time.sleep(.5)
        pyautogui.click(1111, 655)
        time.sleep(.5)
        pyautogui.click(756, 1061)
        print('Your custom status was changed to ' + status + ' and will be cleared after ' + clear_after + '!')
        exit()

    if clear_after == 'dont':
        pyautogui.click(614, 1062)
        time.sleep(.5)
        pyautogui.click(1031, 584)
        time.sleep(.5)
        pyautogui.click(1106, 772)
        time.sleep(.5)
        pyautogui.click(1111, 655)
        time.sleep(.5)
        pyautogui.click(756, 1061)
        print('Your custom status was changed to ' + status + ' and will not be cleared!')
        exit()