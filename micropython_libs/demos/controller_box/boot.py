import os, sdcard
from machine import Pin
import network
import utime

def mount_sdcard(spi, cs_sdcard):
    sd = sdcard.SDCard(spi, Pin(cs_sdcard))
    os.mount(sd, '/sd')


def wifi(ssid, pwd=""):
    sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
    sta_if.connect(ssid, pwd)

    tmo = 50
    while not sta_if.isconnected():
        utime.sleep_ms(100)
        tmo -= 1
        if tmo == 0:
            break
    if tmo > 0:
        ifcfg = sta_if.ifconfig()
        print("WiFi started, IP:", ifcfg[0])
        utime.sleep_ms(500)
