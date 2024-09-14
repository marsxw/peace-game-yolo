import win32gui
import time
 
def m_sleep(t):
    now = time.time()
    while time.time() - now < t:
        pass

def get_hwnd(target_window='SK助手'):
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

 

 