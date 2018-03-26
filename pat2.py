"""To create a lilypond source file, redirect printed output to a name.ly file:
   $ python3 pat2.py > pat2.ly
Then compile the file:
   $ lilypond pat2.ly
"""
from lilypy.pattern import pattern
from lilypy.header import header, footer

print(header)

rhythm = "8 8 8 8  8 8 8 8"
for key in ["ef", "af", "df", "gf", "b", "e" ,"a", "d", "g", "c", "f", "bf"]:
    print(f"\n% key of {key}:")
    pattern(key, 2, "1 2 b3 1  2 b3 4 2", rhythm, text=f'^"key of {key}"', reset_octave=True)
    pattern(key, 2, "b3 4 5 b3  1 2 b3 1", rhythm)
    pattern(key, 5, "1 2 3 1  2 3 4 2", rhythm)
    pattern(key, 5, "3 4 5 3  1 2 3 1", rhythm)
    pattern(key, 1, "1, 2 3 1  2 3 4 2", rhythm)
    pattern(key, 1, "3 4 5 3  1 2 3 1", rhythm)
    pattern(key, 1, "2 3 4 2  7 1 2 7", rhythm)
    pattern(key, 1, "1 3 2 1  2 4 3 2", rhythm)

print(footer)
