import time
import pyautogui as auto
time.sleep(10)
with open('theText.txt', 'r') as theFile:
    auto.FAILSAFE = False
    for line in theFile:
        for _ in range(500):
            auto.typewrite(line)
            auto.press('enter')

