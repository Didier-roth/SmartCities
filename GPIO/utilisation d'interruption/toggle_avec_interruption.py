from machine import Pin

BUTTON = machine.Pin(16,machine.Pin.IN)
LED = machine.Pin(18,machine.Pin.OUT)

val = False


def callback(BUTTON):
    global val
    val = not val
    LED.value(val)


BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=callback)


while True:
    pass
