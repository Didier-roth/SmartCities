from machine import ADC
from utime import sleep
RAS = ADC(0)
while True:
    print(RAS.read_u16())
    sleep(1)