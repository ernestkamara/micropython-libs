import mpu9250
from machine import I2C, Pin
import pin_definitions as pd

i2c = I2C(scl=Pin(pd.I2C_SCL), sda=Pin(pd.I2C_SDA))
mpu = mpu9250.MPU9250(i2c)


import utime
from ssd1351 import color565
import controller_box
from xglcd_font import XglcdFont
font = XglcdFont('fonts/Bally7x9.c', 7, 9)

c = controller_box.ControllerBox()
while True:
    (x, y, z) = mpu.magnetic
    print(x, y, z)
    #c.display.clear()

    c.display.draw_text(0, 0, '{} x'.format(x), font, color565(255,0,0))
    c.display.draw_text(0, 20, '{} y'.format(y), font, color565(0,255,0))
    c.display.draw_text(0, 40, '{} z'.format(z), font, color565(0,0,255))
    utime.sleep_ms(100)