import uasyncio as asyncio

from car_webstep import CarWebstep


def main_async():
    car = CarWebstep()

    # I'm alive
    car.honk(50)

    loop = asyncio.get_event_loop()
    loop.create_task(car.start_engine())
    loop.run_forever()

if __name__ == "__main__":
    main_async()