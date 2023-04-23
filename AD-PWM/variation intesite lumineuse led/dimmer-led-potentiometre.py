from machine import ADC,PWM,Pin
RAS = ADC(0)
LED = PWM(Pin(18))
LED.freq(500)
while True:
    LED.duty_u16(RAS.read_u16())