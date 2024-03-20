from lcd1602 import LCD1602
from machine import Pin, ADC, I2C
from utime import sleep

i2c = I2C(1,scl=Pin(7),sda=Pin(6),freq=400000)
d = LCD1602(i2c,2,16)

degree =[
    0b01100, 
    0b10010,
    0b10010,
    0b01100, 
    0b00000, 
    0b00000, 
    0b00000, 
    0b00000,]
d.clear()
d.create_char(0,degree)
d.display()

RAS = ADC(0)

        
while True:
    sleep(1)
    d.clear()
    deg = ((360-0)/(65535-160))*(RAS.read_u16()-160)+0
    d.print(str(deg))
    d.write(0)
    

