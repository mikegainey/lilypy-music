import random

class Note:
    def __init__(self, pos, pitch_base, pitch_mod, pitch_oct, length):
        self.pos = pos
        self.pitch_base = pitch_base
        self.pitch_mode = pitch_mod
        self.pitch_oct = pitch_oct
        self.length = length


    def __str__(self):
        s = ''
        s += str(self.pos) + ' '
        s += self.pitch_base
        return s

notes = []
for a in range(10):
    pitch = random.choice(list('abcdefg'))
    note = Note(a, pitch, '', '', 8)
    notes.append(note)

for a in range(10):
    print notes[a]

# change this so that a note's index in the list is the position of the note in the melody
