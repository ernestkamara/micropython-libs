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

SPI_SCK = 5
SPI_MOSI = 18
SPI_MISO = 19

BUTTON_LEFT = mappings['TCK']
BUTTON_RIGHT = mappings['TMS']

JOYSTICK_X = 32
JOYSTICK_Y = 39
JOYSTIC_SW = mappings['SVN']

MIC = 33

ENCODER_CLK = mappings['SVP'] #36
ENCODER_DT = 15
ENCODER_SW = 27

SSD1351_DC = 25
SSD1351_RST = 26
SSD1351_CS = 4

I2C_SCL = 0
I2C_SDA = 0

BUZZER = 0
MICRO_SD_CS = 14
GY_9250_CS = 0


# pins_l = [
#     mappings['SVP'],
#     mappings['SVN'],
#     26,
#     35,
#     18,
#     33,
#     19,
#     34,
#     23,
#     mappings['TMS'],
#     5,
#     mappings['TCK'],
# ]
#
# pins_r = [
#     27,
#     22,
#     25,
#     21,
#     32,
#     16,
#     mappings['TDI'],
#     17,
#     4,
#     2,
#     mappings['TDO'],
# ]
