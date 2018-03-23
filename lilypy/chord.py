# define constants
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
notes = (['a', 'gss', 'bff'], ['as', 'bf'], ['b', 'cf', 'ass'], ['bs', 'c', 'dff'], ['cs', 'df'], ['d', 'css', 'eff'],
         ['ds', 'ef'], ['e', 'ff', 'dss'], ['es', 'f', 'gff'], ['fs', 'gf'], ['g', 'fss', 'aff'], ['gs', 'af'])
chords = {'maj' : [[1, 0], [3, 4], [5, 7]], 'min' : [[1, 0], [3, 3], [5, 7]],
          'dim' : [[1, 0], [3, 3], [5, 6]], 'aug' : [[1, 0], [3, 4], [5, 8]],
          'MM7' : [[1, 0], [3, 4], [5, 7], [7, 11]], 'Mm7' : [[1, 0], [3, 4], [5, 7], [7, 10]],
          'mm7' : [[1, 0], [3, 3], [5, 7], [7, 10]], 'mM7' : [[1, 0], [3, 3], [5, 7], [7, 11]]}


def chord(one, quality):
    """chord(one : str, quality : str) -> [str]
    Given a starting note (of the format found in the notes constant) and a quality
    (a key in the chords dictionary), return a list representing the notes of the chord.
    >>> chord('a', 'maj')
    ['a', 'cs', 'e']
    >>> chord('c', 'mm7')
    ['c', 'ef', 'g', 'bf']
    >>> chord('bf', 'Mm7')
    ['bf', 'd', 'f', 'af']
    """
    # is the argument (one) a valid note?
    for index, note in enumerate(notes):
        if one in note:
            one_note = one                           # the note
            one_index = index                        # the index of the note in notes
            one_letter = one[0]                      # just the letter part
            one_letter_x = letters.index(one_letter) # the index of the letter in letters
            break
    else:
        print(f"Error: The input note was not recognized:  '{one}'\n")
        return None

    # make a list with degrees (1, 3, 5) and halfstep intervals (0, 4, 7)
    degrees = chords[quality]

    chord = []
    for degree, steps in degrees:

        # compute the letter names of the chord tones
        letter_x = (one_letter_x + degree - 1) % 7
        chord_letter = letters[letter_x]

        halfstep_interval = (one_index + steps) % 12
        pitch_class = notes[halfstep_interval]

        for note in pitch_class:        # check each note of the pitch class
            if chord_letter == note[0]: # do the note letters match?
                chord.append(note)      # append the note to the output list
                break

    return chord
