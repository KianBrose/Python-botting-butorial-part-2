import keyboard
import pyautogui
import win32api, win32con


while 1:
    keyboard.wait('esc')
    mystring = "My name is jeff"
    keyboard.write(mystring)
    keyboard.press_and_release('enter')
