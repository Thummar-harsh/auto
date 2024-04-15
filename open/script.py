import pyautogui
import subprocess
import time


pyautogui.hotkey('win')
time.sleep(0.1)
pyautogui.typewrite('Anaconda Prompt')
pyautogui.hotkey('enter')
time.sleep(5)
pyautogui.hotkey('enter')
time.sleep(2)
pyautogui.typewrite('D:')
pyautogui.hotkey('enter')
time.sleep(0.2)
pyautogui.typewrite('cd D:\std')
pyautogui.hotkey('enter')
time.sleep(0.2)
pyautogui.typewrite('jupyter notebook')
pyautogui.hotkey('enter')
time.sleep(0.2)