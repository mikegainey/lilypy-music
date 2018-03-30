# lilypond music writer

scale_list = ['c', 'f', 'bf', 'ef', 'af', 'df', 'gf', 'b', 'e', 'a', 'd', 'g']

import pychord
import pyscale

f = open('pylily.ly', 'w')

music = ('''\\version "2.16.0"\n''')
music += ('''\\language "english"\n''')

music += "{\n"

for s in scale_list:  # s = current scale
    note_list = pyscale.scale(s)  # s_list = list of notes in the scale
    topoct = False  # change octaves after note b
    for note in note_list:  # the note in the scale
        if topoct is False:
            music += note + "' "  #
            if note[0] == 'b':
                topoct = True
        else:
            music += note + "'' "  # build the string
    music += "\n"

music += '}'

print music
f.write(music)

f.close()
