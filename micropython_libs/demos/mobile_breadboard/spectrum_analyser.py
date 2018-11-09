import time
from cmath import exp, pi
import max7219
from machine import Pin, SPI, ADC

import pin_definitions as p
### 8x8 MATRIX

MISO = Pin(p.PIN_SPI_MISO)  # not in use -- master in slave out
MOSI = Pin(p.PIN_SPI_MOSI)  # master out slave in
SCK  = Pin(p.PIN_SPI_SCK)  # clock
CS   = Pin(p.PIN_DISPLAY_CS)  # cable select

spi  = SPI(spihost=1, sck=SCK, mosi=MOSI, miso=MISO)
display = max7219.Matrix8x8(spi, CS, 4)
display.brightness(15)
display.fill(0)

def draw_matrix(lst):
    for i in range(len(lst)):
        for j in range(8):
            display.pixel(i, 8-j-1, 1 - (j >= lst[i]))
    display.show()

# some startup-art
lst = [ abs(8 - (i%16)) for i in range(32) ]
for i in range(100):
    draw_matrix(lst[(i%32):] + lst[:(i%32)])
    time.sleep(0.01)
display.fill(0)
display.show()
# end startup-art

### END 8x8 MATRIX





### FFT
from cmath import exp, pi

def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    T= [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]
### END FFT



### MICROPHONE
OUT = 34  # Connect it to OUT on microphone

mic = ADC(Pin(OUT))
mic.atten(ADC.ATTN_11DB)

def read_mic():
    return min(max(int(round(mic.read()/15.0)) - 44, 0), 127)

### END MICROPHONE

prev = time.ticks_ms()

vals = [0 for _ in range(64)]

while True:
    for i in range(64):
        time.sleep(0.001)
        vals[i] = read_mic()

    #now = time.ticks_ms()
    #print(time.ticks_diff(now, prev), 'ms')
    #prev = now
    draw_matrix(
        [(abs(f)/140.0) for f in fft(vals)][1:32+1]
    )