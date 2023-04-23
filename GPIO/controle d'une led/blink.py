from machine import Pin
from utime import sleep
LED = machine.Pin(16,machine.Pin.OUT)

while True:
    LED.value(True)
    sleep(1)
    LED.value(False)
    sleep(1)
