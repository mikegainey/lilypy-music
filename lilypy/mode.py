# define constants
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
notes = (['a', 'gss', 'bff'], ['as', 'bf'], ['b', 'cf', 'ass'], ['bs', 'c', 'dff'], ['cs', 'df'], ['d', 'css', 'eff'],
         ['ds', 'ef'], ['e', 'ff', 'dss'], ['es', 'f', 'gff'], ['fs', 'gf'], ['g', 'fss', 'aff'], ['gs', 'af'])
major_scale = (2, 2, 1, 2, 2, 2, 1)


def mode(one, mode):
    """mode(one : str, mode : int) -> [str]
    Given a starting note (of the format found in the notes constant) and a mode
    (where 1 = Ionian, 2 = Dorian, etc.), return a list representing the scale
    starting on the given starting note.
    >>> mode('bf', 1) # B-flat major
    ['bf', 'c', 'd', 'ef', 'f', 'g', 'a', 'bf']
    >>> mode('c', 6) # C minor
    ['c', 'd', 'ef', 'f', 'g', 'af', 'bf', 'c']
    >>> mode('e', 5) # E mixolydian
    ['e', 'fs', 'gs', 'a', 'b', 'cs', 'd', 'e']
    """

    split = mode - 1
    pattern = major_scale[split:] + major_scale[:split]

    # is the argument (one) a valid note?
    for index, note in enumerate(notes):
        if one in note:
            one_note = one                             # the note
            one_index = index                          # the index of the note in notes
            one_letter = one[0]                        # just the letter part
            one_letter_x = letters.index(one_letter)   # the index of the letter in letters
            break
    else:
        print(f"Error: The input note was not recognized:  '{one}'\n")
        return None

    scale = []
    for degree in range(8):
        halfstep_span = sum(pattern[:degree])            # number of halfsteps to each scale degree
        pitch_class_x = (one_index + halfstep_span) % 12 # index of the pitch class in notes
        pitch_class = notes[pitch_class_x]               # the pitch class of the scale degree
        scale_letter_x = (one_letter_x + degree) % 7     # index of the letter of the scale degree in letters
        scale_letter = letters[scale_letter_x]           # the letter of the scale degree in letters

        for note in pitch_class:        # check each note of the pitch class
            if scale_letter == note[0]: # do the note letters match?
                scale.append(note)      # append the note to the output list
                break

    return scale
