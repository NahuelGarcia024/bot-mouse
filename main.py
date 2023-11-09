import pyautogui as botMouse
import webbrowser as wb
import random
import time


wb.open('https://www.youtube.com/watch?v=QH2-TGUlwu4&list=RDQH2-TGUlwu4&start_radio=1')
while True:
    #print(botMouse.position()) # Print the current mouse position
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    
    botMouse.moveTo(x, y, 0.5) # Move the mouse to a random position
    time.sleep(0.5)
    
    #botMouse.click() # Click the mouse 