import controller_box
from ssd1351 import color565
import gc
import time
from xglcd_font import XglcdFont
font = XglcdFont('fonts/Bally7x9.c', 7, 9)


def mic_test(c):
    display = c.display
    mic = c.mic

    display.clear()

    while True:
        if c.interrupt():
            display.clear()
            break
        for i in range(127):
            val = int(mic.read())
            display.draw_vline(i%127, 0, min(max(int(val/15)-44,10),127), color565((i*2%255), 255-(i*2%255), 255-int(((i*2%255)/2))))
            time.sleep(0.01)
        display.clear()
        gc.collect()
    display.fill_circle(64, 64, 10, color565(255, 255, 255))
    time.sleep(2)


def front_test(c):
    display = c.display
    enc = c.encoder
    enc_sw = c.encoder_sw
    joy = c.joystick
    joy_sw = c.joystick_sw

    colors = [
        color565(255, 0, 0),
        color565(0, 255, 0),
        color565(0, 0, 255)
        ]


    while True:
        color = colors[enc.value % len(colors)]
        if c.interrupt():
            display.clear()
            break
        x = 127 - (max(6, min(120, int(joy.x.read() / 32))))
        y = max(6, min(120, int(joy.y.read() / 32)))
        display.clear()

        display.fill_circle(x, y, 6, color)

        display.draw_text(0, 64, "joystick: {}".format(joy_sw.value()), font, color565(255, 0, 0))

        if not c.button_left.value():
            display.fill_circle(30, 10, 10, color565(0, 255, 0))
        if not c.button_right.value():
            display.fill_circle(50, 10, 10, color565(0, 0, 255))
            c.beeper.duty(10)
        else:
            c.beeper.duty(0)

    display.fill_circle(64, 64, 10, color565(255, 255, 255))
    time.sleep(2)


def bme280_test(c):
    import bme280
    from ssd1351 import color565
    from xglcd_font import XglcdFont
    font = XglcdFont('fonts/Bally7x9.c', 7, 9)

    try:
        bme = bme280.BME280(i2c=c.i2c)
        c.display.clear()
        (t, p, h) = bme.read_compensated_data()
        c.display.draw_text(0, 0, bme.values[0], font, color565(255, 0, 0))
        c.display.draw_text(0, 20, bme.values[1], font, color565(0, 255, 0))
        c.display.draw_text(0, 40, bme.values[2], font, color565(0, 0, 255))
        c.display.draw_hline(0, 50, (h // 1024) * 128 // 100, color565(0, 0, 255))
        print(bme.values)
        time.sleep(3)
        c.display.fill_circle(64, 64, 10, color565(255, 255, 255))
    except Exception as e:
        c.display.clear()
        c.display.draw_text(0, 40, str(e), font, color565(0, 0, 255))
    finally:
        time.sleep(2)



def mpu9250_test(c):
    import mpu6500

    try:
        mpu = mpu6500.MPU6500(c.i2c)

        print(mpu.acceleration)

        print(mpu.gyro)
        print(mpu.whoami)  # <- 113

        while True:
            if c.interrupt():
                c.display.clear()
                break
            (x, y, z) = mpu.acceleration
            print(x, y)
            print(abs(int(y * 3)))
            print(abs(int(x * 3)))
            c.display.draw_vline(64, 64, abs(int(y * 3)), color565(255, 0, 0))
            c.display.draw_hline(64, 64, abs(int(x * 3)), color565(0, 0, 255))
            c.display.clear()

        c.display.fill_circle(64, 64, 10, color565(255, 255, 255))
        time.sleep(2)
    except Exception as e:
        c.display.clear()
        c.display.draw_text(0, 40, str(e), font, color565(0, 0, 255))
    finally:
        time.sleep(2)


def all_test(c):

    tests = [
        mic_test,
        front_test,
        bme280_test,
        mpu9250_test,
    ]
    for test_func in tests:
        test_func(c)
    c.display.clear()
    c.display.fill_circle(64, 64, 20, color565(0, 255, 0))
