from machine import Pin, PWM
import uasyncio as asyncio
import network
import utime

import pin_definitions as p
from car import Car
from entertainment_system import get_system


class CarWebstep(Car):
    def __init__(self, pin_left_wheel, pin_right_wheel, pin_horn, entertainment=None):
        super().__init__(pin_left_wheel, pin_right_wheel)
        self.horn = PWM(Pin(pin_horn), freq=300, duty=0)
        self.entertainment = entertainment

    async def honk(self, duration_ms=500):
        horn = self.horn
        horn.duty(100)
        await asyncio.sleep_ms(duration_ms)
        horn.duty(0)

    async def start_engine(self):
        await self.honk()
        while True:
            self.mqtt.subscribe('TDC2018/car/#')
            await asyncio.sleep_ms(500)

    def datacb(self, msg):
        (msg_id, topic, message) = msg
        print(topic, message)
        if message == "LEFT":
            self.mode = self.LEFT
        elif message == "RIGHT":
            self.mode = self.RIGHT
        elif message == "FORWARD":
            self.mode = self.FORWARD
        elif message == "STOP":
            self.mode = self.STOP

    def connect_mqtt(self):
        mqtt = network.mqtt("mosq-pub", "mqtt://test.mosquitto.org", cleansession=True, data_cb=self.datacb)

        # Connect to MQTT
        mqtt.start()

        tmo = 0
        while mqtt.status()[0] != 2:
            utime.sleep_ms(100)
            tmo += 1
            if tmo > 80:
                print("Not connected")
                break

        # Subscribe
        self.honk(100)
        utime.sleep_ms(100)
        self.honk(100)
        self.mqtt = mqtt


def main():
    ent_system = get_system()

    c = CarWebstep(p.PIN_WHEEL_LEFT, p.PIN_WHEEL_RIGHT, p.PIN_HORN, ent_system)
    wifi(ssid='Choice-guest')
    c.connect_mqtt()
    # c.subscribe_mqtt()
    loop = asyncio.get_event_loop()
    loop.create_task(c.start_engine())
    loop.create_task(ent_system.play_demo())
    loop.run_forever()

main()