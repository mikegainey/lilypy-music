# pyscale is now obsolete because pymode exists
# use pymode(start note, 1) for pyscale

# define constants
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
notes = (['a', 'gss', 'bff'], ['as', 'bf'], ['b', 'cf', 'ass'], ['bs', 'c', 'dff'], ['cs', 'df'], ['d', 'css', 'eff'],
         ['ds', 'ef'], ['e', 'ff', 'dss'], ['es', 'f', 'gff'], ['fs', 'gf'], ['g', 'fss', 'aff'], ['gs', 'af'])
major_scale = (2, 2, 1, 2, 2, 2, 1)


def scale(one):

    scale = []
    ''' scale(one : str) -> [str]
        Given a starting note (of the format found in letters), return a list representing
        the major scale beginning on the starting note.
    '''

    # is the argument (one) a valid note?
    for index, note in enumerate(notes):
        if one in note:
            one_note = one                             # the note
            one_letter = one[0]                        # just the letter part
            one_letter_x = letters.index(one_letter)   # the index of the letter in letters
            one_index = index
            break
    else:
        print(f"The note entered was not in the notes constant:  {one}\n")
        return


    for degree in range(8):
        halfstep_span = sum(major_scale[:degree])        # number of halfsteps to each scale degree
        scale_note_x = (one_index + halfstep_span) % 12  # index of the scale degree in notes
        pitch_class = notes[scale_note_x]                # the pitch class of the scale degree
        scale_letter_x = (one_letter_x + degree) % 7     # index of the letter of the scale degree in letters
        scale_letter = letters[scale_letter_x]           # the letter of the scale degree in letters

        for pc in range(len(pitch_class)):               # check each note of the pitch class
            if scale_letter == pitch_class[pc][0]:         # do the note letters match?
                scale.append(pitch_class[pc])                 # append the note to the output list
    return scale
