import time
from controller_box import controller as c
from cmath import exp, pi
from array import array

def sound_analyser():

    w = 128
    h = 128
    display = c.display
    mic = c.mic

    def draw_lines(lst):
        display.clear(0x000000)
        for i, v in enumerate(lst):
            display.draw_vline(i, 0, v, 0xFFFFFF)


    def fft(x):
        N = len(x)
        if N <= 1: return x
        even = fft(list(x)[0::2])
        odd =  fft(list(x)[1::2])
        T= [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
        return [even[k] + T[k] for k in range(N//2)] + \
               [even[k] - T[k] for k in range(N//2)]
    ### END FFT


    def read_mic():
        return min(max(int(round(mic.read()/15.0)) - 44, 0), 127)

    ar = array('H', [0]*(2*w))

    while True:
        for i in range(2*w):
            time.sleep(0.001)
            ar[i] = read_mic()
        # mic.collect(1000, ar)

        draw_lines(
            [(int(abs(f)//12)) for f in fft(ar)][1:w+1]
        )

sound_analyser()