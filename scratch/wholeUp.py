letters = 'a', 'b', 'c', 'd', 'e', 'f', 'g'
notes = (['a', 'gss', 'bff'], ['as', 'bf'], ['b', 'cf', 'ass'], ['bs', 'c', 'dff'], ['cs', 'df'], ['d', 'css', 'eff'],
         ['ds', 'ef'], ['e', 'ff', 'dss'], ['es', 'f', 'gff'], ['fs', 'gf'], ['g', 'fss', 'aff'], ['gs', 'af'])
major_scale = 2, 2, 1, 2, 2, 2, 1
steps = {'c':2, 'd':2, 'e':1, 'f':2, 'g':2, 'a':2, 'b':1}
modifiers = {'ff':-2, 'f':-1, 's':1, 'ss':2}

# an alternate algorithm to find the note a whole-step up from the given note

def wholeUp(one):
    one_letter = one[0] # letter of the input note
    one_modifier = one[1:] # modifier of the input note
    half_steps = steps[one_letter] # starting number of halfsteps from one_letter to the next letter
    half_steps += modifiers[one_modifier]
    print(f"letter = {one_letter}, mod = {one_modifier}, half_steps to next letter = {half_steps}")


