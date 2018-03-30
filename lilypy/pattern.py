from .scale import scale # scale('a') == ['a', 'b', 'cs', 'd', 'e', 'fs', 'gs', 'a']
from .accidental import accidental # accidental('c', '#') == 'cs'
from .scale_degree import scale_degree # scale_degree('c', '#4') == 'fs'

import re
oct_re = re.compile(r"[',]+") # regex that matches octave modifiers

def pattern(key="c", degree=1, pattern="1 2 3 4  5 4 3 2",
            rhythm="8", text="", reset_octave=False):
    chord_root = scale_degree(key, degree) # the chord root
    patternlist = pattern.split()
    rhythmlist = rhythm.split()
    outputlist = []
    for index, deg in enumerate(patternlist):
        degree = deg # degree will mutate

        # dur == duration of the current note
        if index < len(rhythmlist):
            dur = rhythmlist[index]
        else:
            dur = ""

        # handle rests
        if degree == "r":
            outputlist.append(f"{degree}{dur}")
            continue

        # find octave modifiers: ' or ,
        octfound = oct_re.search(degree)
        if octfound:
            octmod = octfound.group()
            degree = degree.strip("',")
        else:
            octmod = ""

        pitch = scale_degree(chord_root, degree)
        lilynote = f"{pitch}{octmod}{dur}"
        outputlist.append(lilynote)

    if text:
        outputlist[0] = f'{outputlist[0]}^"{text}"'

    if reset_octave:
        print("\octaveCheck c'")

    output = " ".join(outputlist)
    print(output) # the real output
    return output # only used for pytest-3 tests
