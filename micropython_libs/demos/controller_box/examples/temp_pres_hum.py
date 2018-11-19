
import controller_box
c = controller_box.ControllerBox()
import bme280
from ssd1351 import color565
bme = bme280.BME280(i2c=c.i2c)
from xglcd_font import XglcdFont
font = XglcdFont('fonts/Bally7x9.c', 7, 9)

c.display.clear()
(t, p, h) = bme.read_compensated_data()
c.display.draw_text(0, 0, bme.values[0], font, color565(255,0,0))
c.display.draw_text(0, 20, bme.values[1], font, color565(0,255,0))
c.display.draw_text(0, 40, bme.values[2], font, color565(0,0,255))
c.display.draw_hline(0, 50, (h//1024)*128//100, color565(0,0,255))
print(bme.values)
