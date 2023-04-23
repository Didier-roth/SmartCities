import machine
import utime
BUTTON = machine.Pin(16,machine.Pin.IN)
LED = machine.Pin(18,machine.Pin.OUT)
val = False
while True:
    if(BUTTON.value()):
        val = not val
        LED.value(val)
        utime.sleep(1)
       