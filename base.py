import pyautogui
import os
import sys
import time
import numpy as np
import cv2
import keyboard
import pytesseract
from pushbullet import PushBullet

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

key = input("Insert API key: ")
pb = PushBullet(api_key=key)

iconWin = resource_path('icons/2.PNG')
iconCross = resource_path('icons/3.PNG')
iconTrade = resource_path('icons/1.PNG')
iconChat = resource_path('icons/4.PNG')
start = 'k'

def initialize(key):
    print(f"Press '{key}' to start")
    keyboard.wait(key)
    print("Starting...")

def search_chat_items(iconChat, iconTrade):
    while True:
        try:
            chat = pyautogui.locateCenterOnScreen(iconChat, confidence=0.8)
            trade = pyautogui.locateCenterOnScreen(iconTrade, confidence=0.8)
            if chat is not None and trade is not None:
                return chat, trade
        except:
            print("Chat not found, press 'K' to restart")
            keyboard.wait('k')
            print('restarting...')

def send_notification(title, body):
    pb.push_note(title, body)

def txt_to_img(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    txt = str(pytesseract.image_to_string(screenshot))
    return txt

def search_icons(icon):
    while True:
        try:
            localization = pyautogui.locateCenterOnScreen(icon, region=areatrade, confidence=0.92)
            if localization:
                pyautogui.moveTo(localization)
                time.sleep(0.25)
                pyautogui.click()
                time.sleep(1)
                pyautogui.mouseDown(); pyautogui.mouseUp()
                time.sleep(0.25)
                notif_txt = txt_to_img(chatbase)
                send_notification("Notification Title", notif_txt)
                time.sleep(0.25) 
            
                pyautogui.typewrite('Sure, 1 sec')
                keyboard.press_and_release('enter')
               
                print("press k to restart")
                keyboard.wait('k')
                print('restarting...')
        except Exception as e:    
            return False

initialize(start)  

chat, trade = search_chat_items(iconChat, iconTrade)
chatbase = (int(chat[0]-20), int(chat[1]-20), 500, 500)
areatrade = (trade[0]-20, trade[1]-16, 370, 32)

while True:
    search_icons(iconWin) or search_icons(iconCross)
    time.sleep(2)
