import machine
BUTTON = machine.Pin(16,machine.Pin.IN)
LED = machine.Pin(18,machine.Pin.OUT)
while True:
    val = BUTTON.value()
    if val == 1:
        LED.value(True)
    else:
        LED.value(False)