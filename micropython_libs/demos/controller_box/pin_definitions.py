'''
Pin mapping

TTGO mini has 23 available GPIO pins
'''

mappings = {
    'TCK': 13,
    'SVP': 36,
    'SVN': 39,
    'TMS': 14,
    'TDO': 15,
    'TDI': 12,
}

SPI_SCK =
SPI_MOSI =
SPI_MISO =

BUTTON_LEFT =
BUTTON_RIGHT =

JOYSTICK_X =
JOYSTICK_Y =
JOYSTIC_SW =

MIC =

ENCODER_CLK =
ENCODER_DT =
ENCODER_SW =

SSD1351_DC =
SSD1351_RST =
SSD1351_CS =

I2C_SCL =
I2C_SDA =

BUZZER =
MICRO_SD_CS =
GY_9250 _CS =




pins_l = [
    mappings['SVP'],
    mappings['SVN'],
    26,
    35,
    18,
    33,
    19,
    34,
    23,
    mappings['TMS'],
    5,
    mappings['TCK'],
]

pins_r = [
    27,
    22,
    25,
    21,
    32,
    16,
    mappings['TDI'],
    17,
    4,
    2,
    mappings['TDO'],
]

from machine import Pin
def check(pin):
    b = Pin(pin, Pin.IN)
    print(b.value(), pin)


