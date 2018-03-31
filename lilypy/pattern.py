from .scale import scale  # scale('a') == ['a', 'b', 'cs', 'd', 'e', 'fs', 'gs', 'a']
from .accidental import accidental  # accidental('c', '#') == 'cs'
from .scale_degree import scale_degree  # scale_degree('c', '#4') == 'fs'

import re
oct_re = re.compile(r"[',]+")  # regex that matches octave modifiers


def pattern(key="c", degree=1, pattern="1 2 3 4  5 4 3 2", rhythm="8", text="", reset_octave=False):
    chord_root = scale_degree(key, degree)
    patternlist = pattern.split()
    rhythmlist = rhythm.split()
    outputlist = []
    for index, note in enumerate(patternlist):

        if index < len(rhythmlist):
            duration = rhythmlist[index]
        else:
            duration = ""

        # handle rests
        if note == "r":
            outputlist.append(f"{note}{duration}")
            continue

        # find octave modifiers: ' or ,
        octfound = oct_re.search(note)
        if octfound:
            octmod = octfound.group()
            degree = note.strip("',")
        else:
            octmod = ""
            degree = note

        pitch = scale_degree(chord_root, degree)
        lilynote = f"{pitch}{octmod}{duration}"
        outputlist.append(lilynote)

    if text:
        outputlist[0] = f'{outputlist[0]}^"{text}"'

    if reset_octave:
        print("\octaveCheck c'")

    output = " ".join(outputlist)
    print(output)  # the real output
    return output  # only used for pytest-3 tests
