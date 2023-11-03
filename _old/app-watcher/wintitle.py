import win32gui

def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    return title

'''
init_title = get_active_window_title()

while 1 == 1:
    if (init_title != get_active_window_title()):
        init_title = get_active_window_title()
        print(init_title)
'''