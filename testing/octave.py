# figure out how to know if the absolute octave has changed and in which direction
# Given two notes, determine if c is crossed and in which direction
# assume the smaller interval (2nd instead of 7th, 3rd instead of 6th, 4th instead of 5th)
# diff_oct1 and diff_oct2 are alternate implementations that do the same thing and both work

def diff_oct1(fst, snd):
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
            return "up"
        else:
            return " "
    else:
        if 'c' in rLetters[:-1] and len(rLetters) >= 2:
            return "down"
        else:
            return " "


def diff_oct2(fst, snd):
    letters = list("abcdefg")
    fstx = letters.index(fst)
    sndx = letters.index(snd)
    diff = sndx - fstx

    if diff > 0:
        if abs(diff) <= 3:
            if fstx <= 1 and sndx >= 2:
                return "up oct"
            else:
                return "up but not to a new octave"
        else:
            if fstx == 2:
                return "down oct"
            else:
                return "down but not to a new octave"
    elif diff < 0:
        if abs(diff) <= 3:
            if fstx >= 2 and sndx <= 1:
                return "down oct"
            else:
                return "down but not to a new octave"
        else:
            if sndx >= 2: # e up to a
                return "up oct"
            else:
                return "up but not to a new octave"
    else: # diff == 0
        return("repeated note")


# 0 1 2 3 4 5 6
# a b c d e f g
letters = list("abcdefg")
for fst in letters:
    print(letters)
    for snd in letters:
        print(f"{fst} to {snd} : {oct2(fst, snd)}")
    input()

