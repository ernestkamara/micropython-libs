import pin_definitions as pd
from machine import Pin
import time

import controller_box

c = controller_box.ControllerBox()

time.sleep_ms(300)

if c.joystick_sw.value() ==  0:
    # Test all components
    import component_test
    component_test.all_test(c)
else:
    # Arkanoid game
    import arkanoid
    arkanoid.main(c)