"""To create a lilypond source file, redirect printed output to a name.ly file:
$ python3 pat1.py > pat1.ly

Then compile the file:
$ lilypond name.ly
"""
from lilypy.pattern import pattern
from lilypy.header import header, footer

print(header)

for key in ["ef", "af", "df", "gf", "b", "e" ,"a", "d", "g", "c", "f", "bf"]:
    print(f"\n% key of {key}:")
    pattern(key, 2, "1 2 b3 5", text=f'key of {key}', reset_octave=True)
    pattern(key, 5, "4 #2 3 2")
    pattern(key, 3, "b3 4 5 b7")
    pattern(key, 6, "3 b2 1 b7")
    pattern(key, 2, "b3 4 5 b7")
    pattern(key, 5, "6 5 3 2")
    pattern(key, 1, "5 3 4 5")
    pattern(key, 1, "5", rhythm="2")

print(footer)
