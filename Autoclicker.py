import keyboard
import pyautogui
import os
from time import sleep

mouseButton = 'right' # mousebutton 'left', 'middle', 'right'
delay = 0 # in milliseconds
hotkey = 'f8' # keyboard key to activate with
exitkey = 'f7' # keyboard key to exit program with

clicking = False
running = True

def hotkeypress(event):
	global clicking
	if event.name == hotkey and clicking == False:
		clicking = True
	elif event.name == hotkey and clicking == True:
		clicking = False
	if event.name == exitkey:
		os._exit('*errorcode*')

keyboard.on_press(hotkeypress)

while running:

	keyboard.wait(hotkey)

	while clicking:

		pyautogui.click(button=mouseButton)

		sleep(delay/1000)