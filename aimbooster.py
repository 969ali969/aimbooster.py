from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32con, win32api

#the color = (255, 219, 195)

time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("s") == False:
    pic = pyautogui.screenshot(region=(550,330,800,660))
    
    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r,g,b = pic.getpixel((x,y))
            if b == 195:
                click(x+550,y+330)
                time.sleep(0.09)
                break