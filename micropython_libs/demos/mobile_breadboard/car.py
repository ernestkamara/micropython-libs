from utime import ticks_ms, ticks_diff


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
        self.mode_until = ticks_ms()

    def update_wheels(self):
        if ticks_diff(self.mode_until, ticks_ms) < 0:
            self.mode = self.STOP

        if self.mode == self.STOP:
            self.left_wheel.duty(0)
            self.right_wheel.duty(0)
        elif self.mode == self.FORWARD:
            self.left_wheel.duty(self.speed)
            self.right_wheel.duty(self.speed)
        elif self.mode == self.LEFT:
            self.left_wheel.duty(0)
            self.right_wheel.duty(self.speed)
        elif self.mode == self.RIGHT:
            self.left_wheel.duty(self.speed)
            self.right_wheel.duty(0)

    def brake(self):
        self.left_wheel.duty(0)
        self.right_wheel.duty(0)