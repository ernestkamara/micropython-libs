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

SPI_SCK = 18
SPI_MOSI = 23
SPI_MISO = 19

BUTTON_LEFT = mappings['TMS']
BUTTON_RIGHT = 5#mappings['TMS']

JOYSTICK_X = 35
JOYSTICK_Y = mappings['SVN']
JOYSTICK_SW = 33

MIC = 36

ENCODER_CLK = 17 #mappings['SVP'] #36
ENCODER_DT = 16
ENCODER_SW = 21

SSD1351_RST = mappings['TDI']
SSD1351_DC = 4
SSD1351_CS = 32

I2C_SCL = 27
I2C_SDA = 25

BUZZER = mappings['TCK']
MICRO_SD_CS = 2
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
