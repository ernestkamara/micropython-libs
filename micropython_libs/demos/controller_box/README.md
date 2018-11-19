## ESP32:

pins 34~39 do not have pull-up or pull-down circuitry

https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/adc

ADC1 (8 channels, attached to GPIOs 32 - 39)
ADC2 (10 channels, attached to GPIOs 0, 2, 4, 12 - 15 and 25 - 27).

ADC1 should be used since ADC2 is used by WiFi driver

## Components

- [Microphone MAX9814](https://www.aliexpress.com/item/MAX9814-Microphone-AGC-Amplifier-Board-Module-Auto-Gain-Control-for-Arduino-Programmable-Attack-and-Release-Ratio/32811696553.html?spm=a2g0s.9042311.0.0.27424c4dsZHGny)
- [Micro SD (SPI)](https://www.aliexpress.com/item/2PCS-TF-Micro-SD-Card-Module-Mini-SD-Card-Module-Memory-Module-for-Arduino-ARM-AVR/32673631024.html?spm=a2g0s.9042311.0.0.27424c4dM6UCj3)
- 2x push buttons
- [Rotary encoder](https://www.aliexpress.com/item/Free-Shipping-360-rotary-encoder-FOR-Module-Electronic-Component/1000001872933.html?spm=a2g0s.9042311.0.0.27424c4dVGzKP5)
- [Joystick (ADC)](https://www.aliexpress.com/snapshot/0.html?spm=a2g0s.9042311.0.0.27424c4dppu12E&orderId=95219895774301&productId=32280675550)
- [OLED display SSD1351 (3.3V)](https://www.aliexpress.com/item/1-5-inch-7PIN-Full-Color-OLED-module-Display-Screen-SSD1351-Drive-IC-128-RGB-128/32793875682.html?spm=a2g0s.9042311.0.0.27424c4dhZ6eLa)
- [9-axis GY-9250](https://www.aliexpress.com/item/SPI-IIC-MPU9250-MPU-9250-MPU-9250-9-Axis-Attitude-Gyro-Accelerator-Magnetometer-Sensor-Module-MPU9250/32216818498.html?spm=a2g0s.9042311.0.0.27424c4dT28mRX)
- [Buzzer (PWM)](https://www.aliexpress.com/item/New-Arrival-Durable-3-24V-Piezo-Electronic-Buzzer-Alarm-95DB-Continuous-Sound-Beeper-For-Arduino-Car/32666789405.html?spm=a2g0s.9042311.0.0.27424c4dqq7VPG)
- [Temperature, humidity, pressure - BME280](https://www.aliexpress.com/item/3In1-BME280-GY-BME280-Digital-Sensor-SPI-I2C-Humidity-Temperature-and-Barometric-Pressure-Sensor-Module-1/32847825408.html?spm=a2g0s.9042311.0.0.27424c4da3Cahb)

## Files

### Internal

- boot.py
- main.py
- pin_definitions.py
- components.py
- controller_box.py
- component_tests.py
- examples/

### External

- [sdcard.py](https://github.com/micropython/micropython/blob/master/drivers/sdcard/sdcard.py)
- [ssd1351.py](https://github.com/rdagger/micropython-ssd1351)
- [mpu9250.py](https://github.com/tuupola/micropython-mpu9250)
- mpu6500.py
- ak8963.py
- [bme280.py](https://github.com/catdog2/mpy_bme280_esp8266)

## Demos

[arkanoid.py](https://github.com/rdagger/micropython-ssd1351/blob/master/arkanoid.py)

### Tasks

1. Connect to wifi and install a package from `upip`
- 