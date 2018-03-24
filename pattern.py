"""
keys = ['c', 'f', 'bf', ...]

>>> pattern(key="c", scale_degree=2, pattern="1 b3 r 8  #6 5 b3 5", rhythm="4/4 8 8 8 8 8 8 8 8")
"d f a d b a f a"
>>> pattern("c", 5, "1 3 5 b7  8 9 8 b7")
"g b d f  g a g f"
>>> pattern("c", 1, "1 8' 2, 3  5 r b3 3")
"c c' d, e g a ef e"
>>> pattern("c", b2, "1 2 3 4  5 3 2 1")
"df ef f gb af f ef df"

*** for now: ***
>>> pattern("c", "1 2 b3 3 5 6 5 3")
"c d ef e  g a g e"
"""
from lp_scale import scale
from modnote import modnote

def pattern(key="c", scale_degree=2, pattern="1 b3' r 8  #6 9 b3 5", rhythm="4/4 8 8 8 8 8 8 8 8"):
    pat1 = scale(key)            # the scale of the key
    print(f"\npat1:  {pat1}")
    sdl = pat1[scale_degree - 1] # the chord root
    pat2 = scale(sdl)            # the (major) scale of the chord
    print(f"\npat2:  {pat2}")
    pat3 = []                    #pat2 modified according to pattern
    for n in pattern.split():
        note = n # note will mutate
        if note == "r": # a rest
            pat3.append("r")
            continue
        if note[-1] in "',":
            octmod = note[-1]
            note = note[:-1]
            # print(f"  octmod={octmod}  note={note}")
        else:
            octmod = ""
        if note[0] in "#b":
            alt = note[0]
            note = note[1:]
            # print(f"  alt={alt}  note={note}")
        else:
            alt = "na"
        note = int(note)
        if note >= 8:
            note -= 7
            octmod = "'" # this won't work if there's already an octave modifier
        letter = pat2[note - 1]
        letter = modnote(letter, alt)
        letter = letter + octmod

        pat3.append(letter)

    print()
    print(pat3)


            # pat3.append(note)
    # print(f"\npat3:  {pat3}")

