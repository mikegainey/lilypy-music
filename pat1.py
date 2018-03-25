"""To create a lilypond source file, redirect printed output to a name.ly file:
$ python3 pat1.py > pat1.ly

Then compile the file:
$ lilypond name.ly
"""
from lilypy.lp_pattern import pattern

print("""\\version "2.18.0"
\\language "english"
\\relative c' {""")

rhythm = "8 8 8 8  8 8 8 8"
for key in ["ef", "af", "df", "gf", "b", "e" ,"a", "d", "g", "c", "f", "bf"]:
    print(f"% key of {key}:")
    pattern(key, 2, "1 2 b3 5", rhythm, text=f'^"key of {key}"', reset_octave=True)
    pattern(key, 5, "4 #2 3 2", rhythm)
    pattern(key, 3, "b3 4 5 b7", rhythm)
    pattern(key, 6, "3 b2 1 b7", rhythm)
    pattern(key, 2, "b3 4 5 b7", rhythm)
    pattern(key, 5, "6 5 3 2", rhythm)
    pattern(key, 1, "5 3 4 5", rhythm)
    pattern(key, 1, "5", rhythm="2")
    print()

print("}\n")
