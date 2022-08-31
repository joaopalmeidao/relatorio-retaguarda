import pyautogui
import pygetwindow
import time
from datetime import datetime
import keyring
from module.telegram import TelegramBot

# JANELAS:
windows = pygetwindow.getWindowsWithTitle('Gestão Empresarial | DB Ware Company')
windows_login = pygetwindow.getWindowsWithTitle('Login do Sistema | DB Ware Company')
windows_vendas = pygetwindow.getWindowsWithTitle('Vendas Detalhadas do PDV')
# DATA:
data = datetime.today().strftime('%d-%m-%Y')
# USER AND PASSWORD:
user = 'R'
password = keyring.get_password('dbvenda','R')

def Pesquisar():
    pyautogui.hotkey('win','r')
    pyautogui.write('C:\DBVenda\Binarios\DBVenda.exe')
    pyautogui.press('enter')
    time.sleep(5)


def Login():

    time.sleep(4)
    pyautogui.write(user)
    pyautogui.write(password)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter') 
    pyautogui.press('right')
    pyautogui.press('enter') 
    time.sleep(4)
    # pyautogui.press('enter')
    # pyautogui.press('right')
    # pyautogui.press('enter')


def RelatorioVendas():
    time.sleep(1)
    # pyautogui.moveTo(38,94)   
    pyautogui.click(38,94)
    time.sleep(20)

def ImprimirRelatorioTotal():
    pyautogui.screenshot('Venda Guara Total {}.png'.format(data))
    time.sleep(1)
    TelegramBot.send_message_with_image('Venda Guara Total {}.png'.format(data),'Vendas Guará Total {}'.format(data))    

def ImprimirRelatorio(operador:str):
    # PARAMETROS PRINTSCREEN:
    # left = 540; top = 200; width = 840; height = 635
    pyautogui.click(331,165,clicks=2)
    pyautogui.write(operador)
    pyautogui.click(459,159)
    # pyautogui.press('enter')
    time.sleep(15)
    pyautogui.screenshot('Vendas Guara Caixa {}--{}.png'.format(operador,data))
    time.sleep(2)
    TelegramBot.send_message_with_image('Vendas Guara Caixa {}--{}.png'.format(operador,data),'Vendas Guará Caixa {}'.format(operador))

def Sair():
    pyautogui.hotkey('alt','f4') 
    pyautogui.hotkey('alt','f4')

def main():
    TelegramBot.load_config()

    Pesquisar()
    Login()

    
    RelatorioVendas()
    ImprimirRelatorioTotal()
    pyautogui.press('tab')
    ImprimirRelatorio('1')
    ImprimirRelatorio('2')
    ImprimirRelatorio('3')
    time.sleep(1)
    Sair()

    for window in windows:
        window.activate()
        pyautogui.hotkey('alt','f4')

    pyautogui.press("esc")
    pyautogui.press("esc")
    exit()

if __name__=='__main__':
    main()


