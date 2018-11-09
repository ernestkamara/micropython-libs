from machine import Pin, ADC, DAC, SPI
from array import array
import cmath
import uasyncio as asyncio
from utime import sleep_ms

import max7219
import pin_definitions as p

import utime
def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = utime.ticks_us()
        result = f(*args, **kwargs)
        delta = utime.ticks_diff(utime.ticks_us(), t)
        print('Function {} Time = {:6.3f}ms'.format(myname, delta/1000))
        return result
    return new_func

class Display(max7219.Matrix8x8):
    def __init__(self, pin_display_cs):
        self.spi = SPI(spihost=1, sck=p.PIN_SPI_SCK, mosi=p.PIN_SPI_MOSI, miso=p.PIN_SPI_MISO)
        super().__init__(self.spi, Pin(pin_display_cs), 4)

    def draw_matrix(self, buf):
        for i in range(len(buf)):
            for j in range(8):
                self.pixel(i, 8-j-1, 1 - (j >= buf[i]))
        self.show()


class Microphone(ADC):
    def __init__(self, pin):
        super().__init__(Pin(pin))
        self.atten(ADC.ATTN_11DB)


class Speaker:
    def __init__(self, pin_dac):
        self.dac = DAC(pin_dac)

    def play_song(self, filepath=''):
        self.dac.write_timed(filepath)

    def beep(self):
        self.dac.beep(400, 500)


class EntertainmentSystem:
    def __init__(self, display, microphone, speaker=None):
        self.speaker = speaker
        self.display = display
        self.microphone = microphone
        self.mic_buffer = array('H', 64)

    async def play_demo(self):
        buf = self.mic_buffer
        if self.speaker:
            self.speaker.play_song()
        freq = 1000
        mic = self.microphone
        display = self.display
        while True:
            mic.collect(freq, data=buf)
            inp = [min(max(int(round(r / 15.0)) - 44, 0), 127) for r in buf]
            mat = abc(inp)
            display.draw_matrix(mat)
            await asyncio.sleep_ms(0)


@timed_function
def abc(x):
    return [(abs(f)/140.0) for f in fft(x)][1:32+1]


def fft(x):
    exp = cmath.exp
    pi = cmath.pi
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]


def main():
    display = Display(p.PIN_DISPLAY_CS)
    mic = Microphone(p.PIN_MICROPHONE)
    ent = EntertainmentSystem(display, mic)
    # ent.play_demo()

    loop = asyncio.get_event_loop()
    loop.create_task(ent.play_demo())
    loop.run_forever()

main()