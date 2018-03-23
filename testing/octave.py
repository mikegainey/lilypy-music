# figure out how to know if the absolute octave has changed and in which direction
# Given two notes, determine if c is crossed and in which direction
# assume the smaller interval (2nd instead of 7th, 3rd instead of 6th, 4th instead of 5th)
# it works

def newOct(fst, snd):
    letters = list("abcdefg")
    fstx = letters.index(fst)
    letters = letters[fstx:] + letters[:fstx]
    sndx = letters.index(snd)
    fLetters = letters[:sndx + 1]

    letters = list(reversed(list("abcdefg")))
    fstx = letters.index(fst)
    letters = letters[fstx:] + letters[:fstx]
    sndx = letters.index(snd)
    rLetters = letters[:sndx + 1]

    if len(fLetters) < len(rLetters):
        if 'c' in fLetters[1:]:
            return "'"
        else:
            return " "
    else:
        if 'c' in rLetters[:-1] and len(rLetters) >= 2:
            return ","
        else:
            return " "

print(letters)
for fst in letters:
    for snd in letters:
        print(f"{newOct(fst, snd)}", end=" ")
    print()

