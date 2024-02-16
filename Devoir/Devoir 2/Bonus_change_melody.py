from machine import Pin, PWM, ADC
from utime import sleep, ticks_ms

buzzer = PWM(Pin(27))
RAS = ADC(0)
BUTTON = machine.Pin(16,machine.Pin.IN)


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

two_tiger_note = ["DO","RE","MI","Do",
                  "DO","RE","MI","Do",
                  "MI","FA","SOL",
                  "MI","FA","SOL",
                  "SOL","LA","SOL","FA","MI","DO",
                  "SOL","LA","SOL","FA","MI","DO",
                  "RE","SOL","DO",
                  "RE","SOL","DO"]

two_tiger_time = ["noir","noir","noir","noir",
                  "noir","noir","noir","noir",
                  "noir","noir","noir",
                  "noir","noir","noir",
                  "croche","croche","croche","croche","noir","noir",
                  "croche","croche","croche","croche","noir","noir",
                  "noir","noir","noir",
                  "noir","noir","noir"]

two_tiger_octave = []
for i in range(len(two_tiger_note)):
    two_tiger_octave.append(5)


melody = [ode_joy_note,two_tiger_note]
melody_time = [ode_joy_time,two_tiger_time]
melody_octave = [ode_joy_octave,two_tiger_octave]

melody_played = 0
melody_len = len(melody[0])
i = 0




def callback(BUTTON):
    N()
    global melody
    global melody_played
    global melody_len
    global i
    melody_played = melody_played + 1
    if(melody_played >= 2):
        melody_played = 0
    melody_len = len(melody[melody_played])
    i = 0
    print("melody_len : " + str(melody_len))
    print("melody_played : " + str(melody_played))



BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=callback)

while True:
    while i < (melody_len):
        print("melody_len boucle : " + str(melody_len))
        PlayNote((melody[melody_played])[i], (melody_time[melody_played])[i], RAS.read_u16(), (melody_octave[melody_played])[i])
        #print(i)
        #print(RAS.read_u16())
        i = i + 1
    i=0    
    N()
    sleep(10)







