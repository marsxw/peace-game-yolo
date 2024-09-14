# %%
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

def draw_rectangle(hwnd, left, top, right, bottom, color):
    hdc = user32.GetDC(hwnd)
    pen = gdi32.CreatePen(0, 3, color)
    brush = gdi32.CreateSolidBrush(color)
    gdi32.SelectObject(hdc, pen)
    gdi32.SelectObject(hdc, brush)
    gdi32.Rectangle(hdc, left, top, right, bottom)
    gdi32.DeleteObject(pen)
    gdi32.DeleteObject(brush)
    user32.ReleaseDC(hwnd, hdc)

shared_array = Array(ctypes.c_uint8, range(1440*2560*4), lock=False)
#%%
hwnd, window_title = get_hwnd(target_window='SK助手')
 
#%%
while 1:
    start = time.time()
    img = screen.grabWindow(hwnd).toImage()
    img_h,img_w = img.height(), img.width()

    main_nparray = np.frombuffer(shared_array,  dtype=ctypes.c_uint8, count=img_h*img_w*4)
    main_nparray[:] = img.constBits()
    end = time.time()
    
    cv2.imshow("ScreenShot", main_nparray.reshape(img_h, img_w, 4)[:, :, :-1])
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord(' '):
        cv2.waitKey(0)
    print(end-start)
cv2.destroyAllWindows()

# window = MainWindow()
# window.show()
# sys.exit(app.exec())
# %%

import win32gui
import win32ui
from win32api import GetSystemMetrics

# 获取上下文
dc = win32gui.GetDC(0)
# 创建绘制器 类似于pen
dcObj = win32ui.CreateDCFromHandle(dc)
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
#%%
def draw_rect(hwnd, left, top, right, bottom):
    hdc = win32gui.GetWindowDC(hwnd)
    win32gui.DrawFocusRect(hdc, (left, top, right, bottom))
    win32gui.ReleaseDC(hwnd, hdc)

# while True:
#     # 获取hwnd窗口位置
#     left, top, right, bottom = win32gui.GetWindowRect(hwnd)


#     # 转换为屏幕坐标
#     left, top = win32gui.ClientToScreen(hwnd, (left, top))
#     right, bottom = win32gui.ClientToScreen(hwnd, (right, bottom))
#     left -= 50
#     top -= 50
#     right -= 50
#     bottom -= 50

#     draw_rect(hwnd, left, top, right, bottom)
    # draw_rectangle(hwnd, left, top, right, bottom, 0xffffff)
 

 

# %%
import ctypes, time
import win32gui, win32api
from pywinauto.win32functions import *
from pywinauto.win32structures import RECT, POINT
import win32con
from utils import *
hwnd, window_title = get_hwnd(target_window='SK助手')
montion_show_window_hwnd, _ = get_hwnd(target_window='MontionShowWindow')

dc = win32gui.GetDC(0)
rect=RECT()
brush=win32gui.CreateSolidBrush(win32api.RGB(0, 255, 0))
pen = win32gui.CreatePen(win32con.PS_SOLID, 30, win32api.RGB(0, 255, 0))

i = 0
while 1: 
    if  win32gui.GetForegroundWindow() not in [hwnd ,montion_show_window_hwnd]:
        continue
    
    # i += 10
    if i>200:
        i =0 
    start  = time.time()
    GetWindowRect(hwnd, rect)
    delta= 100
    l=rect.left + delta
    t=rect.top + delta
    r=rect.right  - delta
    b=rect.bottom   - delta  

    # win32gui.FrameRect(dc,(l+i, t+i,l+i+100, t+i+100),brush)
    win32gui.FrameRect(dc,(0,0,200,200),brush)
    print(time.time()- start)

 
#%%
 
#%%
import time
import win32gui
import win32api
import win32con
from pywinauto.win32functions import GetWindowRect
from pywinauto.win32structures import RECT
from utils import get_hwnd
# 获取窗口句柄
hwnd, window_title = get_hwnd(target_window='SK助手')
montion_show_window_hwnd, _ = get_hwnd(target_window='MontionShowWindow')


def create_pen(width, color):
    return 
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
def draw_rect(dc, l, t, r, b): 
    win32gui.Polyline(dc, [(l, t), (r, t), (r, b), (l, b), (l, t)]) 
    # win32gui.Rectangle(dc, l, t, r, b)
    win32gui.FrameRect(dc, (l, t, r, b), win32gui.GetStockObject(win32con.DC_BRUSH))
    # dcObj.Rectangle(( l, t, r, b))
    win32gui.DrawText(dc, str(i), -1, (l, t, r, b),   win32con.DT_CENTER | win32con.DT_VCENTER | win32con.DT_SINGLELINE)
    win32gui.InvalidateRect(hwnd, monitor, True)


# 获取设备上下文
dc = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dc)

win32gui.SelectObject(dc, win32gui.CreatePen(win32con.PS_SOLID, 1, win32api.RGB( 0, 0, 0)))
rect = RECT()
i = 0

try:
    while True:
        if win32gui.GetForegroundWindow() not in [hwnd, montion_show_window_hwnd]:
            continue
        
        # 增加 i 的值
        i += 50
        if i > 600:
            i = 0

        # 开始计时
        start = time.time()

        # 获取窗口矩形
        GetWindowRect(hwnd, rect)
        delta = 100
        l = rect.left + delta
        t = rect.top + delta
        r = rect.right - delta
        b = rect.bottom - delta

        # 绘制矩形框
        draw_rect(dc, l + i, t + i, l + i + 150, t + i + 150)
        # draw_rect(dc, l + 530, t +  310 , l + 530 + 100, t + 310 + 100)

        # 输出时间
        print(time.time() - start)
        time.sleep(0.01)

finally:
    # 释放资源
    # win32gui.DeleteObject(pen)
    win32gui.ReleaseDC(0, dc)

# %%
# 读取图片 使用Yolo识别
import cv2
import numpy as np
import torch
from ultralytics import YOLO


image = cv2.imread("D:/game_yolov8/video/dataset_yolo/test/images/06-05-11-44-51_150.jpg") 
#%%
# Load a model
model = YOLO("D:/game_yolov8/train/runs/detect/train/weights/best.pt")  
#%%
result = model(image)[0]  
boxes = result.boxes  # Boxes object for bounding box outputs
cls = boxes.cls.type(torch.int8).tolist()
conf = boxes.conf.tolist() 
xyxy = boxes.xyxy


# %%
# 绘制矩形框
image_  = image
for i in range(len(cls)):
    cv2.rectangle(image_, (int(xyxy[i][0]), int(xyxy[i][1])), (int(xyxy[i][2]), int(xyxy[i][3])), (0, 255, 0), 1)
    cv2.putText(image, f"{conf[i]:.2f}", (int(xyxy[i][0]), int(xyxy[i][1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
cv2.imshow("image", image_)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
