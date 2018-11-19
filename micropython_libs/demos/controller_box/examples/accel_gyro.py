import mpu6500
from machine import I2C, Pin
import pin_definitions as pd

i2c = I2C(scl=Pin(pd.I2C_SCL), sda=Pin(pd.I2C_SDA))
mpu = mpu6500.MPU6500(i2c)

print(mpu.acceleration)

print(mpu.gyro)
print(mpu.whoami) # <- 113

from ssd1351 import color565
import controller_box
import utime
c = controller_box.ControllerBox()
while True:
    (x, y, z) = mpu.acceleration
    print(x, y)
    print(abs(int(y*3)))
    print(abs(int(x*3)))
    c.display.draw_vline(64, 64, abs(int(y*3)), color565(255,0,0))
    c.display.draw_hline(64, 64, abs(int(x*3)), color565(0,0,255))
    #utime.sleep_ms(100)
    c.display.clear()
