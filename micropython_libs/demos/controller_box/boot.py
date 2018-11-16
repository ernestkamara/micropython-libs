import os, sdcard
from machine import Pin


def mount_sdcard(spi, cs_sdcard):
    sd = sdcard.SDCard(spi, Pin(cs_sdcard))
    os.mount(sd, '/sd')