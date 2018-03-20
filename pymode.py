letters = 'a', 'b', 'c', 'd', 'e', 'f', 'g'
notes = (['a', 'gss', 'bff'], ['as', 'bf'], ['b', 'cf', 'ass'], ['bs', 'c', 'dff'], ['cs', 'df'], ['d', 'css', 'eff'],
         ['ds', 'ef'], ['e', 'ff', 'dss'], ['es', 'f', 'gff'], ['fs', 'gf'], ['g', 'fss', 'aff'], ['gs', 'af'])
major_scale = 2, 2, 1, 2, 2, 2, 1


def mode(one, mode):

    pattern = []
    for mode_x in range(7):
        step = major_scale[(mode_x + mode - 1) % 7]
        pattern.append(step)

    # is the argument (one) a valid note?
    for note in notes:
        if one in note:
            one_note = one                             # the note
            one_letter = one[0]                        # just the letter part
            one_letter_x = letters.index(one_letter)   # the index of the letter in letters
            one_index = notes.index(note)              # the index of the note in notes
            break
    else:
        print one, 'The note entered was not in my list.'
        print
        return

    scale = []
    for degree in range(8):
        halfstep_span = sum(pattern[:degree])        # number of halfsteps to each scale degree
        scale_note_x = (one_index + halfstep_span) % 12  # index of the scale degree in notes
        pitch_class = notes[scale_note_x]                # the pitch class of the scale degree
        scale_letter_x = (one_letter_x + degree) % 7     # index of the letter of the scale degree in letters
        scale_letter = letters[scale_letter_x]           # the letter of the scale degree in letters

        for pc in range(len(pitch_class)):               # check each note of the pitch class
            if scale_letter == pitch_class[pc][0]:         # do the note letters match?
                scale.append(pitch_class[pc])                 # append the note to the output list
    return scale
