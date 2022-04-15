import datetime

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_module = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file_name = f"{time_module}.mp4"

fourcc = cv2.VideoWriter_fourcc("m","p","4","v")
capture_video  = cv2.VideoWriter(file_name,fourcc,20.0,(width,height))


while True:
    img = ImageGrab.grab(bbox= (0, 0, width, height))
    img_np = np.array(img)
    final_img  = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    cv2.imshow("Smooth Capture", final_img)
    capture_video.write(final_img)
    if cv2.waitKey(10) == ord("q"):
        break
