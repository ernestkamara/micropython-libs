from machine import Pin, ADC, DAC, SPI
from array import array
import cmath
import uasyncio as asyncio
import utime

import max7219
import pin_definitions as p


class Display(max7219.Matrix8x8):
    def __init__(self, pin_display_cs):
        self.spi = SPI(spihost=1, sck=p.PIN_SPI_SCK, mosi=p.PIN_SPI_MOSI, miso=p.PIN_SPI_MISO)
        super().__init__(self.spi, Pin(pin_display_cs), 4)
        self.max_idx = 0

    def draw_matrix(self, buf):
        for i in range(len(buf)):
            for j in range(8):
                self.pixel(i, 8-j-1, 1 - (j >= buf[i]))
        self.show()

    async def startup_art(self):
        lst = [abs(8 - (i % 16)) for i in range(32)]
        for i in range(100):
            self.draw_matrix(lst[(i % 32):] + lst[:(i % 32)])
            await asyncio.sleep_ms(3)
        self.fill(0)
        self.show()


class Microphone(ADC):
    def __init__(self, pin):
        super().__init__(Pin(pin))
        self.atten(ADC.ATTN_11DB)


class Speaker(DAC):
    def play_song(self, filepath='/'):
        self.dac.write_timed(filepath)


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
        await display.startup_art()
        while True:
            mic.collect(freq, data=buf)
            inp = [min(max(int(round(r / 15.0)) - 44, 0), 127) for r in buf]
            mat = [(abs(f)/140.0) for f in fft(inp)][1:32+1]
            display.draw_matrix(mat)
            await asyncio.sleep_ms(0)


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


def get_system():
    display = Display(p.PIN_DISPLAY_CS)
    mic = Microphone(p.PIN_MICROPHONE)
    ent = EntertainmentSystem(display, mic)
    return ent


def main():
    display = Display(p.PIN_DISPLAY_CS)
    mic = Microphone(p.PIN_MICROPHONE)
    ent = EntertainmentSystem(display, mic)
    # ent.play_demo()

    loop = asyncio.get_event_loop()
    loop.create_task(ent.play_demo())
    loop.run_forever()
