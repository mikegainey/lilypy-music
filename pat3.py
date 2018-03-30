"""To create a lilypond source file, redirect printed output to a name.ly file:
   $ python3 pat1.py > pat1.ly
Then compile the file:
   $ lilypond name.ly
"""
from lilypy.pattern import pattern
from lilypy.header import header, footer

print(header)

for key in ["c", "f", "bf", "ef", "af", "df", "gf", "b", "e" ,"a", "d", "g"]:
    print(f"\n% key of {key}:")
    pattern(key, 1, "1 2 3 4  5 4 3 2", text=f'key of {key}', reset_octave=True)
    pattern(key, 1, "1 3 5 8  7 5 4 2")

print(footer)
