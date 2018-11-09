from machine import Pin, PWM
import uasyncio as asyncio

import pin_definitions as p
from car import Car


class CarWebstep(Car):
    def __init__(self, pin_left_wheel, pin_right_wheel, pin_horn, entertainment_system=None):
        super().__init__(pin_left_wheel, pin_right_wheel)
        self.horn = PWM(Pin(pin_horn), freq=300, duty=0)
        self.entertainment_system = entertainment_system

    async def honk(self, duration_ms=500):
        horn = self.horn
        horn.duty(100)
        await asyncio.sleep_ms(duration_ms)
        horn.duty(0)

    async def start_engine(self):
        ent = self.entertainment_system
        if ent:
            await self.entertainment_system.play_demo()


def main():
    c = Car(p.PIN_WHEEL_LEFT, p.PIN_WHEEL_RIGHT, p.PIN_HORN)

    loop = asyncio.get_event_loop()
    loop.create_task(c.start_engine())
    loop.run_forever()