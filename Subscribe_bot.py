import pyautogui
import time
while 1:
    if pyautogui.locateOnScreen('SUBSCRIBE.PNG'):
        print("I can see it")
        pyautogui.click('SUBSCRIBE.PNG')
        time.sleep(5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
