class Note:

    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    absolute_pitch = "c'" # the default starting pitch for relative mode
                          # then, the absolute pitch of the last Note

    def __init__(self, letter, accidental='', change_octave='', duration='8'):
        self.letter = letter # r = rest
        self.accidental = accidental
        self.change_octave = change_octave
        self.duration = duration # 8 = eighth note
        self.abs_pitch = ""

        # update the absolute_pitch
        self.first = Note.letters.index(Note.absolute_pitch[0])
        self.second = Note.letters.index(self.letter)

        print(Note.letters)
        print(f'first : {Note.absolute_pitch[0]} {self.first}')
        print(f"second: {self.letter} {self.second}")
        diff = (self.second - self.first)
        if abs(diff) <= 3:
            print(f"up {diff}")
        else:
            print(f"down {7 - diff}")

        Note.absolute_pitch = self.letter


    def __str__(self):
        return f"{self.letter}{self.accidental} {self.change_octave}"
