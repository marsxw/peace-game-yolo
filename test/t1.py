import pyautogui
import win32gui
import win32con
import ctypes
import time

# 获取鼠标当前所在的窗口句柄
def get_mouse_window():
    pos = pyautogui.position()  # 获取鼠标当前位置
    hwnd = win32gui.WindowFromPoint(pos)  # 获取鼠标位置的窗口句柄
    return hwnd
 
# 检查鼠标是否在指定窗口内
def is_mouse_in_window(target_hwnd):
    current_hwnd = get_mouse_window()
    return current_hwnd == target_hwnd

# 检查鼠标是否可见
def is_mouse_visible():
    class CURSORINFO(ctypes.Structure):
        _fields_ = [('cbSize', ctypes.c_uint),
                    ('flags', ctypes.c_uint),
                    ('hCursor', ctypes.c_void_p),
                    ('ptScreenPos', ctypes.wintypes.POINT)]

    cursor_info = CURSORINFO()
    cursor_info.cbSize = ctypes.sizeof(CURSORINFO)
    ctypes.windll.user32.GetCursorInfo(ctypes.byref(cursor_info))

    cursor_visible = cursor_info.flags == 1  # 1 表示光标可见
    return cursor_visible

def get_hwnd(target_window):
    hwnd_title = dict()

    def get_all_hwnd(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
    win32gui.EnumWindows(get_all_hwnd, 0)

    is_find = False
    for hwnd, t in hwnd_title.items():
        print(hwnd, t)
        if target_window in t:
            is_find = True
            break

    assert is_find, f"can't find the target window: {target_window}"
    return hwnd, t

# 目标窗口标题
target_window_name = 'MontionShowWindow'  # 替换为你的游戏窗口标题

hwnd, window_title = get_hwnd(target_window_name)
print(f"Monitoring mouse status for window: {window_title}")

while True:
    start = time.time()
    in_window = is_mouse_in_window(hwnd)
    mouse_visible = is_mouse_visible()

    if in_window:
        if not mouse_visible:
            print("hide") 
 
    print(time.time()-start)
    # time.sleep(0.1)
 