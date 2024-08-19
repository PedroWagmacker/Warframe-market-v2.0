import pyautogui
import time
from PIL import Image
import numpy as np
import cv2
import keyboard
import pytesseract
from pushbullet import PushBullet

key= input("insert api key:")


pb= PushBullet(api_key=f'{key}')
iconWin= 'icons/2.PNG'
iconCross= 'icons/3.PNG'
iconTrade = 'icons/1.PNG'
iconChat= 'icons/4.PNG'
start= 'k'

def inicialize(key):
    print(f"press {key} to start")
    keyboard.wait(key)
    print("starting")

def search_chat_itens(ChatIcon,TradeIcon):
 while True:
  try:
    chat =pyautogui.locateCenterOnScreen(iconChat, confidence=0.8)
    trade =pyautogui.locateCenterOnScreen(iconTrade,confidence=0.95)
    if iconChat is not None and iconTrade is not None:
       return chat, trade
  except:
     print("chat not found, press K to restart")
     keyboard.wait('k')

def send(title,body):
    pb.push_note(title,body)

def txt_to_img(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    txt = str(pytesseract.image_to_string(screenshot))
    return txt

def search_icons(icon):
 while True:
    try:
        localization = pyautogui.locateCenterOnScreen(icon,region=areatrade,confidence=0.8)
        if localization:
            pyautogui.moveTo(localization)
            time.sleep(1)
            pyautogui.mouseDown();pyautogui.mouseUp()
            time.sleep(0.25)
            notif_txt = txt_to_img(chatbase)
            send("platininha",notif_txt)
            time.sleep(0.25) 
            pyautogui.typewrite('sure, 1 sec')
            keyboard.press_and_release('enter')
                
            inicialize(start)                        
    except Exception as e:    
        return False


inicialize(start)  

chat, trade = search_chat_itens(iconChat,iconTrade)
chatbase= (int(chat[0]-20), int(chat[1]-20),500,500)
areatrade= (trade[0]-20, trade[1]-16,370,32)

while True:
  search_icons(iconWin) or search_icons(iconCross)
  time.sleep(2)



      
      
