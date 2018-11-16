from time import sleep_ms
from controller_box import controller as c

from ssd1351 import color565
from xglcd_font import XglcdFont
font = XglcdFont('fonts/Bally7x9.c', 7, 9)

maxduty = const(122)
minduty = const(30)

def polygon_select():
    e = c.encoder
    display = c.display

    colors = [
        (255,0,0),
        (153, 50, 0),
        (0, 255, 0),
        (0, 0, 255),
        (0, 0, 0),
        (255, 255, 0),
        (0, 255, 255),
    ]

    names = [
        'Victor',
        'Olav',
        'Ina',
        'Dagfinn',
        'Sebastian',
        'Anna',
        'Christine',
    ]


    numcolors = len(colors)

    val = e.value
    try:
        while True:
            if c.interrupt():
                display.clear(color565(0, 0, 0))
                break
            if e.value != val:
                val = e.value
                i = val % numcolors
                color = colors[i]
                display.clear(color565(*color))
                display.fill_polygon(sides=i+3, x0=64, y0=64, r=35, color=color565(255, 255, 255))
                display.draw_text(50, 60, names[i], font, color565(255, 255, 255))
            sleep_ms(100)
    finally:
        display.clear()

polygon_select()