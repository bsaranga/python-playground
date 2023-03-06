import wintitle as wt
import execpath as exe

init_title = exe.get_active_window_executable()

while 1 == 1:
    if (init_title != exe.get_active_window_executable()):
        exe.image2(exe.get_active_window_executable())