import win32gui
import win32process
import win32api
import win32con
import win32ui
import psutil
from PIL import Image

def image2(path):
    path = path.replace("\\", "/")
    icoX = win32api.GetSystemMetrics(win32con.SM_CXICON)
    icoY = win32api.GetSystemMetrics(win32con.SM_CXICON)

    large, small = win32gui.ExtractIconEx(path, 0)
    win32gui.DestroyIcon(small[0])

    hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap(hdc, icoX, icoX)
    hdc = hdc.CreateCompatibleDC()

    hdc.SelectObject(hbmp)
    hdc.DrawIcon((0,0), large[0])

    bmpstr = hbmp.GetBitmapBits(True)
    img = Image.frombuffer(
    'RGBA',
    (32,32),
    bmpstr, 'raw', 'BGRA', 0, 1
    )

    img.show()

def get_active_window_executable():
    window = win32gui.GetForegroundWindow()
    pid = win32process.GetWindowThreadProcessId(window)[1]
    process = psutil.Process(pid)
    return process.exe()