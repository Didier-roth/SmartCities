import machine
import utime
BUTTON = machine.Pin(16,machine.Pin.IN)
LED = machine.Pin(18,machine.Pin.OUT)
val = False
while True:
    while(BUTTON.value()):
        LED.value(True)
    LED.value(False)    
