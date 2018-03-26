"""
keys = ['c', 'f', 'bf', ...]

>>> pattern(key="c", scale_degree=2, pattern="1 b3 r 8  #6 5 b3 5", rhythm="8 8 8 8 8 8 8 8")
"d f a d b a f a"
>>> pattern("c", 5, "1 3 5 b7  8 9 8 b7")
"g b d f  g a g f"
>>> pattern("c", 1, "1 8' 2, 3  5 r b3 3")
"c c' d, e g a ef e"
>>> pattern("c", b2, "1 2 3 4  5 3 2 1")
"df ef f gb af f ef df"
"""
from lilypy.scale import scale
from lilypy.accidental import accidental

def pattern(key="c", scale_degree=2, pattern="1 b3' r 8  #6 9 b3 5",
            rhythm="8 8 8 8  8 8 8 8", text="", reset_octave=False):
    key_scale = scale(key)                   # the scale of the key
    chord_root = key_scale[scale_degree - 1] # the chord root
    chord_scale = scale(chord_root)          # the (major) scale of the chord
    outpat = []                              # chord_scale modified according to pattern
    first_note = True
    for n, r in zip(pattern.split(), rhythm.split()):
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
        outpat.insert(0, """\octaveCheck c'""")
    print(" ".join(outpat))