import pyautogui
import keyboard
import colorama
from colorama import Fore,Style
import time
import os
# pip install opencv_python
# pip install keyboard
# pip install pyautogui
# pip install colorama
colorama.init(autoreset=True)

os.system('cls||clear')
banner = '''
▀▄    ▄ ▄█    ▄   
  █  █  ██     █  
   ▀█   ██ ██   █ 
   █    ▐█ █ █  █ 
 ▄▀      ▐ █  █ █ 
           █   ██ 
                  
'''


print(Fore.LIGHTMAGENTA_EX + banner)
print()
print()
print('Press <s> to Start // Press <x> to Stop')
os.system('title yin')
print()
print()


def accept():
    y = True
    while y:
        if keyboard.is_pressed('s'):  
            run = True
            os.system('title detective#0001')
            print(Fore.WHITE + '[' + Fore.GREEN + '+' + Fore.WHITE + ']' + Fore.GREEN + ' Auto Accept started')
            while run:
                location = pyautogui.locateOnScreen('accept.png', grayscale=True, confidence=.5)
                #print(location)
                if location != None:
                    pyautogui.click(location)
                    print(Fore.GREEN + '~ Match Accepted!')
                if keyboard.is_pressed('x'):
                    run = False
                    print(Fore.WHITE + '[' + Fore.RED + '-' + Fore.WHITE + ']' + Fore.RED + ' Auto Accept stopped')
                    os.system('title detective#0001')
                    y = False
                    time.sleep(4)
                    os.system('cls||clear')
                    again = input(Fore.WHITE + 'Again?(y/n)')
                    if again == 'n':
                        y = False
                    elif again == 'y':
                        y = True
                    elif again == '':
                        exit()
accept()