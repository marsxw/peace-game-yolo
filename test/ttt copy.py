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
#%%
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
montion_show_window_hwnd, _ = get_hwnd(target_window='MontionShowWindow')
 
#%%
while 1:
    img = screen.grabWindow(hwnd).toImage()
    img_h,img_w = img.height(), img.width()

    start = time.time()
    main_nparray = np.frombuffer(shared_array,  dtype=ctypes.c_uint8, count=img_h*img_w*4)
    main_nparray[:] = img.constBits()
    end = time.time()
    print(end-start)
    

    cv2.imshow("ScreenShot", main_nparray.reshape(img_h, img_w, 4)[58:, :, :-1])
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord(' '):
        cv2.waitKey(0)
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
    return win32gui.CreatePen(win32con.PS_SOLID, width, color)

def draw_rect(dc, l, t, r, b, pen):
    old_mode = win32gui.SetBkMode(dc, win32con.TRANSPARENT)
    old_poly_fill_mode = win32gui.SetPolyFillMode(dc, win32con.ALTERNATE)
    old_pen = win32gui.SelectObject(dc, pen)
    
    # 使用路径绘制一次性绘制矩形框
    win32gui.BeginPath(dc)
    win32gui.MoveToEx(dc, l, t)
    win32gui.LineTo(dc, r, t)
    win32gui.LineTo(dc, r, b)
    win32gui.LineTo(dc, l, b)
    win32gui.LineTo(dc, l, t)
    win32gui.EndPath(dc)
    win32gui.StrokePath(dc)
    
    win32gui.SelectObject(dc, old_pen)
    win32gui.SetPolyFillMode(dc, old_poly_fill_mode)
    win32gui.SetBkMode(dc, old_mode)

 
# 获取设备上下文
dc = win32gui.GetDC(0)

# 预先创建资源
pen_width = 1  # 设置笔的宽度
pen_color = win32api.RGB(255, 0, 0)  # 设置笔的颜色
pen = create_pen(pen_width, pen_color)

rect = RECT()
i = 0

try:
    while True:
        if win32gui.GetForegroundWindow() not in [hwnd, montion_show_window_hwnd]:
            continue
        
        # 增加 i 的值
        i += 10
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
        draw_rect(dc, l + i, t + i, l + i + 10, t + i + 10, pen)

        # 输出时间
        print(time.time() - start)
        time.sleep(0.01)

finally:
    # 释放资源
    win32gui.DeleteObject(pen)
    win32gui.ReleaseDC(0, dc)

# %%
import pyautogui
import win32api
import win32gui
import win32con
import time

# 获取鼠标当前所在的窗口句柄
def get_mouse_window():
    pos = pyautogui.position()  # 获取鼠标当前位置
    hwnd = win32gui.WindowFromPoint(pos)  # 获取鼠标位置的窗口句柄
    return hwnd

# 获取指定窗口的标题
def get_window_title(hwnd):
    length = win32gui.GetWindowTextLength(hwnd)
    return win32gui.GetWindowText(hwnd, length)

# 检查鼠标是否在指定窗口内
def is_mouse_in_window(target_hwnd):
    current_hwnd = get_mouse_window()
    return current_hwnd == target_hwnd

# 主函数
def main():
    target_window_name = "YourGameWindowTitle"  # 替换为你要监测的窗口标题
    target_hwnd = None

    # 查找目标窗口句柄
    def enum_windows_proc(hwnd, lParam):
        global target_hwnd
        if win32gui.IsWindowVisible(hwnd) and target_window_name in get_window_title(hwnd):
            target_hwnd = hwnd
            return False  # 停止枚举
        return True  # 继续枚举

    win32gui.EnumWindows(enum_windows_proc, None)

    if target_hwnd is None:
        print(f"Could not find window with title: {target_window_name}")
        return

    print(f"Monitoring mouse status for window: {target_window_name}")

    while True:
        if is_mouse_in_window(target_hwnd):
            print("Mouse is within the target window.")
        else:
            print("Mouse is outside the target window.")

        time.sleep(1)

if __name__ == "__main__":
    main()
