from lcd1602 import LCD1602
from machine import Pin, ADC, I2C,PWM
from utime import sleep,ticks_ms
import dht


def DO(octave=6, vol=1000):
    buzzer.freq(int(32.7 * octave))
    buzzer.duty_u16(vol)

def N():
    buzzer.duty_u16(0)

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
sensor = dht.DHT11(Pin(18))
RAS = ADC(0)
LED = PWM(Pin(16))
LED.freq(500)
buzzer = PWM(Pin(27))



degree = [
    0b01100,
    0b10010,
    0b10010,
    0b01100,
    0b00000,
    0b00000,
    0b00000,
    0b00000, ]
d.clear()
d.create_char(0, degree)
d.display()


Refresh_freq = 1
last_temp = Refresh_freq + 100

blink_freq = 0.5
blink_period = 1 / blink_freq
last_blink = 0

Buzzer_freq = 1
Buzzer_period = 1 / Buzzer_freq
last_buzzer = 0


temp = 0.0
SetTemp = 0
LedState = False
LedValue = 0
BuzzerState = False

while True:
    #sleep for getting temp
    if (ticks_ms() - last_temp) > (Refresh_freq * 1000):
        sensor.measure()
        temp = sensor.temperature()# temp:  humid:
        d.setCursor(0, 1)
        d.print("Ambient: " + str(temp))
        d.write(0)
        last_temp = ticks_ms()
        

    SetTemp = int(((35 - 15) / (65535 - 160)) * (RAS.read_u16() - 160) + 15)
    d.setCursor(0, 0)
    d.print("Set: " + "{:.0f}".format(SetTemp))
    d.write(0)

    # sleep for alarm
    if (temp > SetTemp +3):
       d.setCursor(11, 0)
       d.print("Alarm")

       if (ticks_ms() - last_buzzer) > ((Buzzer_period * 1000)/2):
           if BuzzerState:
               N()
               BuzzerState = False
           else:
               DO(6,500)
               BuzzerState = True
           last_buzzer = ticks_ms()
    else:
         d.setCursor(11, 0)
         d.print("     ")
         N()

# sleep for led
    if (temp > SetTemp):
       if (ticks_ms() - last_blink) > ((blink_period * 1000)/2):
           if LedState:
               LED.duty_u16(0)
               LedState = False
           else:
               LedState = True
           last_blink = ticks_ms()

       if(LedState):
           if(LedValue+300<35565):
               LedValue = LedValue + 300
               LED.duty_u16(LedValue)
               print(LedValue)
       else:
           if(LedValue>0):
               LedValue = LedValue - 300
               LED.duty_u16(LedValue)
               print(LedValue)

    else:
        LED.duty_u16(0)
        LedState = False





