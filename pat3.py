"""To create a lilypond source file, redirect printed output to a name.ly file:
   $ python3 pat1.py > pat1.ly
Then compile the file:
   $ lilypond name.ly
"""
from lilypy.lp_pattern import pattern

print("""\\version "2.18.0"
\\language "english"
\\relative c'{
\set Staff.extraNatural = ##f
""")

rhythm = "8 8 8 8  8 8 8 8"
for key in ["c", "f", "bf", "ef", "af", "df", "gf", "b", "e" ,"a", "d", "g"]:
    print(f"\n% key of {key}:")
    pattern(key, 1, "1 2 3 4  5 4 3 2", rhythm, text=f'^"key of {key}"', reset_octave=True)
    pattern(key, 1, "1 3 5 8  7 5 4 2", rhythm)

print("}\n")