from machine import Timer
from utime import ticks_ms, ticks_diff
import micropython
micropython.alloc_emergency_exception_buf(100)


class Car:
    STOP = 0
    FORWARD = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, left_wheel, right_wheel):
        self.left_wheel = left_wheel
        self.right_wheel = right_wheel

        self.speed = 0
        self.mode = self.STOP
        self.mode_duration_ms = 500
        self.mode_until = ticks_ms()

    def update_wheels(self):
        if ticks_diff(self.mode_until, ticks_ms) < 0:
            self.mode = self.STOP

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
            self.mode_until = ticks_diff(ticks_ms(), self.mode_duration_ms)
            self.update_wheels()
        else:
            raise Exception("Invalid value for 'mode'")

    def start_engine(self, update_freq_ms=100):
        timer = Timer(-1)
        timer.init(period=update_freq_ms, mode=Timer.PERIODIC, callback=lambda t: self.update_wheels)

