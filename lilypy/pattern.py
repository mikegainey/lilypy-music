"""
assert pattern("d", 1, "1 3, 5' 7  6,, 4'' r 1") == "d8 fs,8 a'8 cs8 b,,8 g''8 r8 d8"
assert pattern("ef", 2, "1 2 b3 4 5 b3 2 1") == "f8 g8 af8 bf8 c8 af8 g8 f8"
assert pattern("c","b2", "1 2 3 #4'' 5 4 3 b2") == "df8 ef8 f8 g''8 af8 gf8 f8 eff8"
assert pattern("c", 5, "1 b2 #2 3 5 b7 b5 3") == "g8 af8 as8 b8 d8 f8 df8 b8"
"""
from .scale import scale # scale('a') == ['a', 'b', 'cs', 'd', 'e', 'fs', 'gs', 'a']
from .accidental import accidental # accidental('c', '#') == 'cs'
from .scale_degree import scale_degree # scale_degree('c', '#4') == 'fs'

import re
oct_re = re.compile(r"[',]+") # regex that matches octave modifiers

def pattern(key="c", degree=1, pattern="1 2 3 4  5 4 3 2",
            rhythm="8 8 8 8  8 8 8 8", text="", reset_octave=False):
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
        outputlist[0] = f"{outputlist[0]}^{text}"

    if reset_octave:
        print("\octaveCheck c'")

    output = " ".join(outputlist)
    print(output) # the real output
    return output # only used for pytest-3 tests
