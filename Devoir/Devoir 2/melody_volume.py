from machine import Pin, PWM, ADC
from utime import sleep, ticks_ms

buzzer = PWM(Pin(27))
RAS = ADC(0)

temps = 0.4
croche = temps / 2
noir = temps
blanche = 2 * temps
rond = 4 * temps


def DO(octave=6, vol=1000):
    buzzer.freq(int(32.7 * octave))
    buzzer.duty_u16(vol)


def DOd(octave=6, vol=1000):
    buzzer.freq(int(34.65 * octave))
    buzzer.duty_u16(vol)


def RE(octave=6, vol=1000):
    buzzer.freq(int(36.71 * octave))
    buzzer.duty_u16(vol)


def REd(octave=6, vol=1000):
    buzzer.freq(int(38.89 * octave))
    buzzer.duty_u16(vol)


def MI(octave=6, vol=1000):
    buzzer.freq(int(41.20 * octave))
    buzzer.duty_u16(vol)


def FA(octave=6, vol=1000):
    buzzer.freq(int(43.65 * octave))
    buzzer.duty_u16(vol)


def FAd(octave=6, vol=1000):
    buzzer.freq(int(46.25 * octave))
    buzzer.duty_u16(vol)


def SOL(octave=6, vol=1000):
    buzzer.freq(int(49.00 * octave))
    buzzer.duty_u16(vol)


def SOLd(octave=6, vol=1000):
    buzzer.freq(int(51.91 * octave))
    buzzer.duty_u16(vol)


def LA(octave=6, vol=1000):
    buzzer.freq(int(55.00 * octave))
    buzzer.duty_u16(vol)


def LAd(octave=6, vol=1000):
    buzzer.freq(int(58.27 * octave))
    buzzer.duty_u16(vol)


def SI(octave=6, vol=1000):
    buzzer.freq(int(61.74 * octave))
    buzzer.duty_u16(vol)


def N():
    buzzer.duty_u16(0)


def check_volume():
    val = RAS.read_u16()
    return int(val / 65535 * 1000)


def non_blocking_sleep(time):
    start = ticks_ms()
    while (ticks_ms() - start) < (time * 1000):
        buzzer.duty_u16(RAS.read_u16())
        pass


def PlayNote(note, time, vol=1000, octave=6):
    if (note == "DO"):
        DO(octave, vol)
    elif (note == "DOd"):
        DOd(octave, vol)
    elif (note == "RE"):
        RE(octave, vol)
    elif (note == "REd"):
        REd(octave, vol)
    elif (note == "MI"):
        MI(octave, vol)
    elif (note == "FA"):
        FA(octave, vol)
    elif (note == "FAd"):
        FAd(octave, vol)
    elif (note == "SOL"):
        SOL(octave, vol)
    elif (note == "SOLd"):
        SOLd(octave, vol)
    elif (note == "LA"):
        LA(octave, vol)
    elif (note == "LAd"):
        LAd(octave, vol)
    elif (note == "SI"):
        SI(octave, vol)
    else:
        N()

    if (time == "croche"):
        non_blocking_sleep(croche)
    elif (time == "noir"):
        non_blocking_sleep(noir)
    elif (time == "blanche"):
        non_blocking_sleep(blanche)
    elif (time == "rond"):
        non_blocking_sleep(rond)
    else:
        N()


ode_joy_note = ["FA", "FA", "SOL", "LA", "LA", "SOL", "FA", "MI", "RE", "RE", "MI", "FA", "FA", "MI", "MI", "FA",
                "FA", "FA", "SOL", "LA", "LA", "SOL", "FA", "MI", "RE", "RE", "MI", "FA", "MI", "RE", "RE", "RE",
                "FA", "FA", "SOL", "LA", "LA", "SOL", "FA", "MI", "RE", "RE", "MI", "FA", "MI", "RE", "RE"]

ode_joy_time = ["noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir",
                "noir", "croche", "blanche",
                "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir",
                "noir", "croche", "blanche",
                "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir", "noir",
                "croche", "blanche"]

ode_joy_octave = []
for i in range(len(ode_joy_note)):
    ode_joy_octave.append(5)

while True:
    for i in range(len(ode_joy_note)):
        PlayNote(ode_joy_note[i], ode_joy_time[i], RAS.read_u16(), ode_joy_octave[i])
        print(i)
        print(RAS.read_u16())

    N()
    sleep(10)







