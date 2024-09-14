#%%
import yaml
import os
import time
import numpy as np
from PyQt5.QtWidgets import QApplication
import cv2
import ctypes
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread
from main_ui import Ui_Form
from pynput import keyboard, mouse
from pynput.keyboard import Controller
import win32api
import win32con
from PySide6.QtCore import QTimer
import torch
from ultralytics import YOLO
from utils import *
from multiprocessing import Process,  Array,  Manager
import ctypes
import time
import pygetwindow as gw

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
shared_array = Array(ctypes.c_uint8, range(1440*2560*4), lock=False)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.checkBox_enableYoloAuxiliary.stateChanged.connect(self.r0) 
        self.ui.checkBox_showGunBox.stateChanged.connect(self.r1) 

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tick)
        self.timer.start()

    def tick(self):
        print("tick running")

    def r0(self):
        print( self.ui.checkBox_enableYoloAuxiliary.isChecked())

    def r1(self):
        print( self.ui.checkBox_showGunBox.isChecked())
 
#%%
hwnd, window_title = get_hwnd(target_window='SK助手')
model = YOLO("D:/game_yolov8/train/runs/detect/train/weights/best.pt")  
while 1:
    start = time.time()
    img = screen.grabWindow(hwnd).toImage()
    img_h,img_w = img.height(), img.width()

    main_nparray = np.frombuffer(shared_array,  dtype=ctypes.c_uint8, count=img_h*img_w*4)
    main_nparray[:] = img.constBits()
    img_array = main_nparray.reshape(img_h, img_w, 4)[-720:, :1280, :-1]
    
    result = model(img_array)[0]
    boxes = result.boxes   
    cls = boxes.cls.type(torch.int8).tolist()
    conf = boxes.conf.tolist() 
    xyxy = boxes.xyxy
    # 绘制矩形框
    img_array_ = img_array.copy()
    for i in range(len(cls)):
        cv2.rectangle(img_array_, (int(xyxy[i][0]), int(xyxy[i][1])), (int(xyxy[i][2]), int(xyxy[i][3])), (0, 255, 0), 1)
        cv2.putText(img_array_, f"{conf[i]:.2f}", (int(xyxy[i][0]), int(xyxy[i][1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

    cv2.imshow("ScreenShot",img_array_)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord(' '):
        cv2.waitKey(0)
    end = time.time()
    print(end-start)
cv2.destroyAllWindows()

