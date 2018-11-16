from machine import Timer, Pin, PWM
from utime import sleep_ms, ticks_ms, ticks_diff, ticks_add
import pin_definitions as p
from machine import Timer

class Car:
    STOP = 0
    FORWARD = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, pin_left_wheel, pin_right_wheel):
        self.left_wheel = PWM(Pin(pin_left_wheel), freq=50, duty=0)
        self.right_wheel = PWM(Pin(pin_right_wheel), freq=50, duty=0)

        self.speed = 70 # 0-100%
        self._mode = self.STOP
        self.mode_duration_ms = 500
        self.mode_until = ticks_ms()

    def update_wheels(self):

        if ticks_diff(self.mode_until, ticks_ms()) < 0:
            self._mode = self.STOP
        if self._mode == self.STOP:
            self.brake()
        elif self._mode == self.FORWARD:
            self.left_wheel.duty(self.speed)
            self.right_wheel.duty(self.speed)
        elif self._mode == self.LEFT:
            self.left_wheel.duty(0)
            self.right_wheel.duty(self.speed)
        elif self._mode == self.RIGHT:
            self.left_wheel.duty(self.speed)
            self.right_wheel.duty(0)

    def brake(self):
        self.left_wheel.duty(0)
        self.right_wheel.duty(0)

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if value in (self.STOP, self.FORWARD, self.LEFT, self.RIGHT):
            self._mode = value
            self.mode_until = ticks_add(ticks_ms(), self.mode_duration_ms)
            self.update_wheels()
        else:
            raise Exception("Invalid value for 'mode'")


if __name__ == "__main__":
    c = Car(p.PIN_WHEEL_LEFT, p.PIN_WHEEL_RIGHT)
    t = Timer(2)

    def update_car(timer):
        global c
        c.update_wheels()

    t.init(period=100, mode=t.PERIODIC, callback=update_car)
