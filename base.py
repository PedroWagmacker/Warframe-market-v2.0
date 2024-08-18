import pyautogui
import time
from PIL import Image
import numpy as np
import cv2
import keyboard
import pytesseract
from pushbullet import PushBullet

pb= PushBullet(api_key="your api key")
icon1= 'icons/2.PNG'
icon2= 'icons/3.PNG'
start= 'f1'

def inicialize(key):
    print(f"press {key} to start")
    keyboard.wait(key)
    print("starting")

inicialize(start)

chat= pyautogui.locateCenterOnScreen('icons/chat.PNG', confidence=0.8)
base= pyautogui.locateCenterOnScreen('icons/1.PNG',confidence=0.95)
chatbase= (int(chat[0]-20), int(chat[1]-20),500,500)
areabase= (base[0]-20, base[1]-16,300,32)





def send(title,body):
    pb.push_note(title,body)


def txt_to_img(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    txt = str(pytesseract.image_to_string(screenshot))
    return txt



def search_icons(icon):
    try:
        localization = pyautogui.locateCenterOnScreen(icon,region=areabase,confidence=0.9)
        if localization:
            pyautogui.moveTo(localization)
            time.sleep(1)
            pyautogui.mouseDown();pyautogui.mouseUp()
            time.sleep(0.25)
            textin = txt_to_img(chatbase)
            send("platininha",textin)
            time.sleep(0.25) 
            pyautogui.typewrite("sure, 1 sec")
            keyboard.press_and_release('enter')                    

            print("press f1 to restart")
            keyboard.wait(start)
            print("restarting")
                    

    except Exception:
        pass

    
while True:
  
  search_icons(icon1) or search_icons(icon2)
      
  time.sleep(3)
