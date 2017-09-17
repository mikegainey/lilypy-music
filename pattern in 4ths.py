# lilypond music writer

import pychord
import pyscale
import pymode
import random
import subprocess

scale_list = ['c', 'f', 'bf', 'ef', 'af', 'df', 'gf', 'b', 'e', 'a', 'd', 'g', 'c']
pattern = [5, 3, 1, 3, 5, 7, 5, 3]


f = open('pylily.ly', 'w')

music = ('''\\version "2.16.0"\n''')
music += ('''\\language "english"\n''')

music += "\\relative c' {\n"
#~music += "\\time 6/8\n"

for s in scale_list:                # s = current scale
    note_list = pymode.mode(s, 5)   # note_list = list of notes in the scale

    first = True
    for deg in pattern:
        if first is True:
            music += note_list[deg - 1] + "=''8 "
            first = False
        else:
            music += note_list[deg - 1] + " "
    music += "\n"
    
music += '}'

print music
f.write(music)

f.close()

subprocess.call(['lilypond', 'pylily.ly'])
