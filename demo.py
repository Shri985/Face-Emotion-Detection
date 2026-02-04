import pyautogui as gui
import time

msg = "Jai Mata Di !!!"
time.sleep(5)
for i in range(100):
    gui.typewrite(msg)
    gui.press('Enter')