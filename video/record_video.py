# %%
import os, sys
sys.path.append( os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import numpy as np
import cv2
import ctypes
from PySide6.QtWidgets import QApplication 
from multiprocessing import  Array 
from  utils import *
import ctypes
import cv2
os.chdir(os.path.dirname(__file__))
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()

shared_array = Array(ctypes.c_uint8, range(1440*2560*4), lock=False)
hwnd, window_title = get_hwnd(target_window='SK助手')
 
#%%
is_recording = False 
video_file =    time.strftime("%m-%d-%H-%M-%S") + ".mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_file, fourcc, 30.0, (1280, 720))
while 1:
    img = screen.grabWindow(hwnd).toImage()
    img_h,img_w = img.height(), img.width()
    if img_h <720 or  img_w<1280:
        continue

    main_nparray = np.frombuffer(shared_array,  dtype=ctypes.c_uint8, count=img_h*img_w*4)
    main_nparray[:] = img.constBits()
    img_array = main_nparray.reshape(img_h, img_w, 4)[-720:, :1280, :-1]
    end = time.time()
    cv2.imshow("ScreenShot", img_array)
    
    if is_recording:
        out.write(img_array)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord(' '):
        is_recording = not is_recording
        print("Recording:", is_recording)

out.release()
cv2.destroyAllWindows()
# %%
 