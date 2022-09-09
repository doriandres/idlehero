import win32api, win32con # pip install pypiwin32
from threading import Timer
import math

def points_in_circumference(radius_len_px, number_of_points_to_generate = 100):
    pi = math.pi
    return [(math.cos(2*pi/number_of_points_to_generate*x)*radius_len_px, math.sin(2*pi/number_of_points_to_generate*x)*radius_len_px) for x in range(0,number_of_points_to_generate+1)]

# set your resolution here
screen_width_px = 1080
screen_height_px = 720

def mouse_move_to(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def change_loop(points, index=0):
    if index >= len(points):
        index = 0
    (x, y) = points[index]    
    mouse_move_to(int(x + (screen_width_px / 2)), int(y + (screen_height_px /2)))
    timer = Timer(0.5, change_loop, (points, index + 1))
    timer.start()

change_loop(points_in_circumference(200, 50))
