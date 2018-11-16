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
        self.speed = 100

    async def honk(self, duration_ms=500):
        horn = self.horn
        horn.duty(3)
        dur = duration_ms//10
        for i in range(10):
            horn.freq(100+ i*40)
            await asyncio.sleep_ms(dur)
        horn.freq(300)
        horn.duty(0)

    async def start_engine(self):
        await self.honk()
        while True:
            self.mqtt.subscribe('TDC2018/car/#')
            await asyncio.sleep_ms(1000)

    async def async_update_wheels(self):
        while True:
            self.update_wheels()
            await asyncio.sleep_ms(200)

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
        free_brokers = [
            'iot.eclipse.org',
            "mqtt://test.mosquitto.org",
        ]
        mqtt = network.mqtt("mosq-pub", free_brokers[1], cleansession=True, data_cb=self.datacb)

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


def get_car():
    ent_system = get_system()

    c = CarWebstep(p.PIN_WHEEL_LEFT, p.PIN_WHEEL_RIGHT, p.PIN_HORN, ent_system)
    d = ent_system.display

    d.fill(0)
    d.text('MQTT', 0, 0, 1)
    d.show()
    return c

def start_car(c):
    c.connect_mqtt()

    loop = asyncio.get_event_loop()
    loop.create_task(c.start_engine())
    loop.create_task(c.async_update_wheels())
    loop.create_task(c.entertainment.play_demo())
    loop.run_forever()


if __name__ == "__main__":
    c = get_car()

    c.horn.duty(100)
    print('horn on')
    utime.sleep(0.1)
    c.horn.duty(0)

    wifi(ssid='Work-Work by ITsjefen', pwd='')
    print('horn off')
    start_car(c)