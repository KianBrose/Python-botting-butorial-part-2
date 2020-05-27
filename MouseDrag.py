import time
import keyboard
import win32api, win32con

time.sleep(2)

win32api.SetCursorPos((847,605))
time.sleep(0.1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
time.sleep(0.1)
win32api.SetCursorPos((847,405))
time.sleep(0.1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
