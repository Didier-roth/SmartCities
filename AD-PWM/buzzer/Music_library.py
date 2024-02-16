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