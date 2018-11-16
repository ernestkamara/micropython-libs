from controller_box import controller as c
import time

from ssd1351 import color565


def display_dot():
    color = color565(255, 0, 0)
    black = color565(0, 0, 0)

    display = c.display
    joy_x = c.joystick.x
    joy_y = c.joystick.y

    while True:
        if c.interrupt():
            display.clear(black)
            break
        x = 127 - (max(6, min(120, int(joy_x.read()/32))))
        y = max(6, min(120, int(joy_y.read()/32)))
        display.clear(black)
        print(x, y)
        display.fill_circle(x, y, 6, color)
        time.sleep(0.01)

display_dot()