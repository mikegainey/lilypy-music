letters = 'a', 'b', 'c', 'd', 'e', 'f', 'g'
major_scale = 2, 2, 1, 2, 2, 2, 1
steps = {'c': 2, 'd': 2, 'e': 1, 'f': 2, 'g': 2, 'a': 2, 'b': 1}
modifiers = {'ff': 2, 'f': 1, 'n': 0, 's': -1, 'ss': -2}  # what a modifier on the lower note does
umod = {0: 'ss', 1: 's', 2: '', 3: 'f', 4: 'ff'}

# it works, but it needs tidying


def wholeUp(one):
    '''wholeUp(one : str) -> str
    Given a starting note, return the note up one whole step.
    '''
    one_letter = one[0]  # letter of the input note
    one_letter_x = letters.index(one_letter)
    next_x = (one_letter_x + 1) % 7
    upper_letter = letters[next_x]

    if len(one) > 1:
        one_modifier = one[1:]  # modifier of the input note
    else:
        one_modifier = 'n'

    half_steps = steps[one_letter]  # starting number of halfsteps from one_letter to the next letter
    half_steps += modifiers[one_modifier]
    upper_note = upper_letter + umod[half_steps]
    return upper_note
