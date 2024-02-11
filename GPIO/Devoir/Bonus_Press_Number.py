from machine import Pin
from utime import sleep
import time

BUTTON = machine.Pin(16,machine.Pin.IN)
LED = machine.Pin(18,machine.Pin.OUT)
selector = 0
change = False
last_press = 0
press = 0
def callback(BUTTON):
    global selector
    global change
    global last_press
    global press

    last_press = press
    press = time.ticks_ms()    
    if((press - last_press <= 500) and (press - last_press > 100)):
        last_press = 0
        change = True
        selector = selector + 1
        if(selector > 2):
            selector = 0
        print(selector)

   


BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=callback)


while True:
    if (change):
        change = False
        for i in range(0, 5):
            LED.value(1)
            sleep(i / 10)
            LED.value(0)
            sleep(i / 10)
            LED.value(1)

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
