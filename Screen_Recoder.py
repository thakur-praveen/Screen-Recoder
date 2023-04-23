from ast import Div
from email.mime import image
from turtle import width
import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time


width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width, height)

f = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("Kadu.mp4", f, 20.0, dim)

now_start_time = time.time()
dur = 60+4
end_time = now_start_time+dur

while True:
    image = pyautogui.screenshot()
    frame__1 = np.array(image)
    frame = cv2.cvtColor(frame__1,cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()
    if c_time > end_time:
        break
output.release()
print("---END---")
