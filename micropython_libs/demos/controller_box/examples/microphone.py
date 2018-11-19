from ssd1351 import color565
import gc
from time import sleep



def mic_test(c):
    display = c.display
    mic = c.mic

    display.clear()

    try:
        while True:
            for i in range(127):
                val = int(mic.read())
                display.draw_vline(i%127, 0, min(max(int(val/15)-44,10),127), color565((i*2%255), 255-(i*2%255), 255-int(((i*2%255)/2))))
                sleep(0.01)
            display.clear(color565(0, 0, 0))
            gc.collect()
    finally:
        display.clear(color565(0, 0, 0))
        gc.collect()