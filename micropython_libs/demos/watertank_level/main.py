from machine import Pin, RTC, deepsleep
import utime
import urequests
import ujson

import settings

floater = Pin(settings.PIN_FLOATER, Pin.IN, Pin.PULL_UP)

headers = {
    'Content-Type': 'application/json'
}
data = {"api_key": settings.SERIVET_API_KEY, "content": settings.MESSAGE_TEXT, "to_number": settings.RECIPIENT_NUMBER}


if floater.value() == 0:
    print("Water level warning!")

    if wifi(settings.WIFI_SSID, settings.WIFI_PWD):
        utime.sleep(2)
        print("Sending SMS")
        try:
            response = urequests.post(settings.SERIVET_URL, data=ujson.dumps(data), headers=headers)
        except:
            print("try again")
            response = urequests.post(settings.SERIVET_URL, data=ujson.dumps(data), headers=headers)

        print(response.json())
    else:
        print("Failed to connect to WiFi")

else:
    print("Water level is OK. Going to sleep..")
    # https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/rtc
    rtc = RTC()
    rtc.ntp_sync(server="hr.pool.ntp.org", tz="CET-1CEST")
    rtc.synced()
    rtc.wake_on_ext0(floater, 0)

    # https://forum.micropython.org/viewtopic.php?t=3900
    deepsleep(0)
