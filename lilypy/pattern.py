"""
keys = ['c', 'f', 'bf', ...]

>>> pattern('d', 1, '1 3 5 7  6 4 2 1')
d8 fs8 a8 cs8 b8 g8 e8 d8
>>> pattern('ef', 2, '1 2 b3 4 5 b3 2 1')
f8 g8 af8 bf8 c8 af8 g8 f8
>>> pattern('c','b2', '1 2 3 4 5 4 3 2 1')
df8 ef8 f8 gf8 af8 gf8 f8 ef8
>>> pattern('c', 5, '1 b2 #2 3 5 b7 b5 3')
g8 af8 as8 b8 d8 f8 df8 b8
"""
from .scale import scale # scale('a') == ['a', 'b', 'cs', 'd', 'e', 'fs', 'gs', 'a']
from .accidental import accidental # accidental('c', '#') == 'cs'
from .scale_degree import scale_degree # scale_degree('c', '#4') == 'fs'

def pattern(key="c", degree=1, pattern="1 2 3 4  5 4 3 2",
            rhythm="8 8 8 8  8 8 8 8", text="", reset_octave=False):
    chord_root = scale_degree(key, degree) # the chord root
    chord_scale = scale(chord_root)        # the (major) scale of the chord
    outpat = []                            # pattern using chord_scale
    first_note = True
    for n, r in zip(pattern.split(), rhythm.split()): # zip limits pattern length to 8 (not good)
        note = n # note will mutate
        if note == "r": # a rest
            outpat.append("r")
            continue

        if note[-1] in "',": # can only handle 1 octave modifier
            octmod = note[-1]
            note = note[:-1]
        else:
            octmod = ""

        if note[0] in "#b": # can only handle 1 sharp or flat
            pitchmod = note[0]
            note = note[1:]
        else:
            pitchmod = "na"

        note = int(note) # can only handle 1 ","
        if note >= 8:
            note -= 7

        outnote = chord_scale[note - 1]
        outnote = accidental(outnote, pitchmod)
        outnote = outnote + octmod + r

        outpat.append(outnote)
        first_note = False

    outpat[0] = outpat[0] + text
    if reset_octave == True:
        # outpat.insert(0, """\octaveCheck c'""")
        print("\octaveCheck c'")
    output = " ".join(outpat)
    print(output) # the real output
    return output # for pytest-3 tests
