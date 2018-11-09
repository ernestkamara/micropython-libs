from machine import Timer, Pin, PWM
from utime import sleep_ms, ticks_ms, ticks_diff, ticks_add
import micropython
micropython.alloc_emergency_exception_buf(100)


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

    # def cb(self, timer):
    #     self.update_wheels()
    #
    # def start_engine(self, update_freq_ms=100):
    #     t = Timer(2)
    #     t.init(period=update_freq_ms, mode=t.PERIODIC, callback=lambda t: self.update_wheels)
    #     self.t = t
