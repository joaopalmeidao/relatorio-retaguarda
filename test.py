import pyautogui
import pygetwindow
import time
from datetime import datetime
import keyring
from module.telegram import TelegramBot

data = datetime.today().strftime('%d-%m-%Y')
TelegramBot.load_config()

pyautogui.screenshot('teste.png')
time.sleep(1)
TelegramBot.send_message_with_image('teste.png','teste') 


