import pyautogui
import time
from PIL import Image
import cv2
import keyboard
import pytesseract
from pushbullet import PushBullet

icon1= 'icons/2.PNG'
icon2= 'icons/3.PNG'
start= 'f1'

time.sleep(5)
base= pyautogui.locateCenterOnScreen('icons/1.PNG',confidence=0.97)
areabase= (base[0]-20, base[1]-16,500,32)



def inicialize(key):
    print(f"press {key} to start")
    keyboard.wait(key)
    print("starting")

def search_icons(icon):
    try:
        localization = pyautogui.locateCenterOnScreen(icon,region=areabase,confidence=0.9)
        if localization:
            pyautogui.moveTo(localization)
            time.sleep(1)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            print("press f1 to restart")
            keyboard.wait(start)

    except Exception:
        pass
         

inicialize(start)
    
while True:
  
  search_icons(icon1) or search_icons(icon2)
  time.sleep(3)
