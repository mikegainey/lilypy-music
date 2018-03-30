# define constants
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
notes = (['a', 'gss', 'bff'], ['as', 'bf'], ['b', 'cf', 'ass'], ['bs', 'c', 'dff'], ['cs', 'df'], ['d', 'css', 'eff'],
         ['ds', 'ef'], ['e', 'ff', 'dss'], ['es', 'f', 'gff'], ['fs', 'gf'], ['g', 'fss', 'aff'], ['gs', 'af'])
major_scale = (2, 2, 1, 2, 2, 2, 1)


def scale(one):
    """Return a major scale, given a starting note.

    Given a starting note (of the format found in letters), return a list representing
    the major scale beginning on the starting note.
    >>> scale('a')
    ['a', 'b', 'cs', 'd', 'e', 'fs', 'gs', 'a']
    >>> scale('ef')
    ['ef', 'f', 'g', 'af', 'bf', 'c', 'd', 'ef']
    """
    # is the argument (one) a valid note?
    for index, note in enumerate(notes):
        if one in note:
            one_note = one  # the note
            one_x = index  # the index of the note in notes
            one_letter = one[0]  # just the letter part
            one_letter_x = letters.index(one_letter)  # the index of the letter in letters
            break
    else:
        print(f"Error: The input note was not recognized:  '{one}'\n")
        return None

    scale = []
    for degree in range(8):
        halfstep_span = sum(major_scale[:degree])  # number of halfsteps to each scale degree
        pitch_class_x = (one_x + halfstep_span) % 12  # index of the pitch class in notes
        pitch_class = notes[pitch_class_x]  # the pitch class of the scale degree
        scale_letter_x = (one_letter_x + degree) % 7  # index of the letter of the scale degree in letters
        scale_letter = letters[scale_letter_x]  # the letter of the scale degree in letters

        for note in pitch_class:  # check each note of the pitch class
            if scale_letter == note[0]:  # do the note letters match?
                scale.append(note)  # append the note to the output list
                break

    return scale
