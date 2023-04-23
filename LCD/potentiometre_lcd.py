from lcd1602 import LCD1602
from machine import Pin, ADC, I2C
from utime import sleep

i2c = I2C(1,scl = Pin(7), sda = Pin(6),freq = 400000)
d = LCD1602(i2c,2,16)
RAS = ADC(0)
d.display()

while True:
    sleep(1)
    d.clear()
    d.print(str(RAS.read_u16()))
    
