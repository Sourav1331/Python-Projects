import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import keyboard

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimension = (width, height)

f = cv2.VideoWriter_fourcc(*"XVID")
result = cv2.VideoWriter("result.mp4", f, 30.0, dimension)
print("Recording..... Press s to stop!.")
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    color_set = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result.write(color_set)
    if keyboard.is_pressed("s"):
        print("User has stopped the recording...")
        break

result.release()
print("---  Video has been created  ---")