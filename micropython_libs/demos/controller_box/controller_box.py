from machine import Pin, ADC, SPI, PWM, I2C
import pin_definitions as pd
import components
from encoder import Encoder
from ssd1351 import Display, color565


class ControllerBox:
    def __init__(self):
        self.button_left = Pin(pd.BUTTON_LEFT, Pin.IN, Pin.PULL_UP)
        self.button_right= Pin(pd.BUTTON_RIGHT, Pin.IN, Pin.PULL_UP)

        self.mic = components.Microphone(pd.MIC)

        self.joystick = components.Joystick(pd.JOYSTICK_X, pd.JOYSTICK_Y)
        self.joystick_sw = Pin(pd.JOYSTICK_SW, Pin.IN, Pin.PULL_UP)

        self.encoder = Encoder(pin_clk=pd.ENCODER_CLK, pin_dt=pd.ENCODER_DT, clicks=4)
        self.encoder_sw = Pin(pd.ENCODER_SW,  Pin.IN, Pin.PULL_UP)

        # self.spi = SPI(2, 2000000, miso=Pin(pd.SPI_MISO), mosi=Pin(pd.SPI_MOSI), sck=Pin(pd.SPI_SCK))
        self.spi = SPI(2, baudrate=14500000, miso=Pin(pd.SPI_MISO), mosi=Pin(pd.SPI_MOSI), sck=Pin(pd.SPI_SCK))

        self.display = Display(self.spi, rst=Pin(pd.SSD1351_RST), dc=Pin(pd.SSD1351_DC), cs=Pin(pd.SSD1351_CS))

        self.beeper = PWM(Pin(pd.BUZZER), freq=300, duty=0)

        self.i2c = I2C(scl=Pin(pd.I2C_SCL), sda=Pin(pd.I2C_SDA))

    def interrupt(self):
        return self.encoder_sw.value() == 0
