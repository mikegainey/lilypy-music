import chord
import scale


while True:
    one = raw_input('Scale starting note: ')
    print scale.scale(one)
    print

    root = raw_input('Chord root note: ')
    quality = raw_input('Chord quality (maj, min, dim, aug: ')
    print chord.chord(root, quality)
    print
