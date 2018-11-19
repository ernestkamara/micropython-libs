import controller_box
import time

from ssd1351 import color565


def display_dot():
    c = controller_box.ControllerBox()
    color = color565(255, 0, 0)
    black = color565(0, 0, 0)

    display = c.display
    joy_x = c.joystick.x
    joy_y = c.joystick.y

    w = 40
    h = 64
    # buf = display.load_sprite('gdg_small.raw', 40, 64)

    prev = (0, 0)
    while True:
        if c.interrupt():
            display.clear(black)
            break
        x = 127 - (max(6, min(120, int(joy_x.read()/32))))
        y = max(6, min(120, int(joy_y.read()/32)))
        display.clear(black)
        display.fill_circle(x, y, 6, color)

        # xr = joy_x.read()
        # x = min(int(128 - xr/32), 128-w)
        # yr = joy_y.read()
        # y = min(int(yr/32), 128-h)
        #
        # display.fill_rectangle(prev[0], prev[1], w, h, 0x000000)
        # display.draw_sprite(buf, x, y, w, h)
        # prev = (x,y)
        # time.sleep(0.01)

display_dot()


