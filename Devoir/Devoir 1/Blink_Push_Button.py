from machine import Pin
from utime import sleep

BUTTON = machine.Pin(16,machine.Pin.IN)
LED = machine.Pin(18,machine.Pin.OUT)
selector = 0

def callback(BUTTON):
    global selector
    selector = selector + 1
    if(selector > 2):
        selector = 0
    print(selector)


BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=callback)


while True:
    if selector == 0:
        LED.value(0)
    elif selector == 1:
        frequency = 0.5
        period = 1/frequency
        LED.value(0)
        sleep(period/2)
        LED.value(1)
        sleep(period/2)
    elif selector == 2:
        frequency = 2
        period = 1 / frequency
        LED.value(0)
        sleep(period/2)
        LED.value(1)
        sleep(period/2)
