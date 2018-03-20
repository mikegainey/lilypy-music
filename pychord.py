letters = 'a', 'b', 'c', 'd', 'e', 'f', 'g'
notes = (['a', 'gss', 'bff'], ['as', 'bf'], ['b', 'cf', 'ass'], ['bs', 'c', 'dff'], ['cs', 'df'], ['d', 'css', 'eff'],
         ['ds', 'ef'], ['e', 'ff', 'dss'], ['es', 'f', 'gff'], ['fs', 'gf'], ['g', 'fss', 'aff'], ['gs', 'af'])
chords = {  'maj' : [[1, 0], [3, 4], [5, 7]], 'min' : [[1, 0], [3, 3], [5, 7]],
            'dim' : [[1, 0], [3, 3], [5, 6]], 'aug' : [[1, 0], [3, 4], [5, 8]],
            'mM7',
          }



def chord(one, quality):

    chord = []

    # find the note letter and the index in the notes list
    for note in notes:
        if one in note:
            one_note = one								# the note
            one_letter = one[0]							# just the letter part
            one_letter_x = letters.index(one_letter)	# the index of the letter in letters
            one_index = notes.index(note)				# the index of the note in notes
            break

    # make a list with degrees (1, 3, 5) and halfstep intervals (0, 4, 7)
    degrees = [degree for degree in chords[quality]]

    for note in range(len(degrees)):

        # compute the letter names of the chord tones
        letter_x = (one_letter_x + degrees[note][0] - 1) % 7
        chord_letter = letters[letter_x]

        halfstep_interval = (one_index + degrees[note][1]) % 12
        pitch_class = notes[halfstep_interval]

        for pc in range(len(pitch_class)):				# check each note of the pitch class
            if chord_letter == pitch_class[pc][0]:		# do the note letters match?
                chord.append(pitch_class[pc])			# append the note to the output list

    return chord
