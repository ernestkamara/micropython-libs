from machine import Pin, PWM, ADC


class Microphone(ADC):
    def __init__(self, pin):
        super().__init__(Pin(pin))
        self.atten(ADC.ATTN_11DB)


class Joystick:
    def __init__(self, pin_x, pin_y):
        self.x = ADC(Pin(pin_x))
        self.x.atten(ADC.ATTN_11DB)  # change attentuation level 0-3.3V
        self.y = ADC(Pin(pin_y))
        self.y.atten(ADC.ATTN_11DB)
