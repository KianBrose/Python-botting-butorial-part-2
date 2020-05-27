import time
import keyboard
import win32api, win32con

time.sleep(2)

win32api.SetCursorPos((500,500))
time.sleep(0.1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
time.sleep(0.1)
win32api.SetCursorPos((500,300))
time.sleep(0.1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
