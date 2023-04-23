from machine import ADC,PWM,Pin
led = PWM(Pin(18))
led.freq(500)
while True:
    i=0
    while(i<65535)
        led.duty_u16(i)
        i++
    while (i>0)
        led.duty_u16(i)
        i--
