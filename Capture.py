from PIL import ImageGrab
import cv2
import numpy as np
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
capture_video = cv2.VideoWriter('capture.mp4', fourcc, 20.0,(width,height),True)

while True:
    capture = ImageGrab.grab(bbox=(0, 0, width, height))
    capture_np = np.array(capture)
    capture_final = cv2.cvtColor(capture_np, cv2.COLOR_BGR2RGBA)
    cv2.imshow("c",capture_final)
    capture_video.write(capture_final)
    if cv2.waitKey(10) == ord('q'):
        break
capture_video.release()

