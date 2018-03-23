letters = 'a', 'b', 'c', 'd', 'e', 'f', 'g'
notes = (['a', 'gss', 'bff'], ['as', 'bf'], ['b', 'cf', 'ass'], ['bs', 'c', 'dff'], ['cs', 'df'], ['d', 'css', 'eff'],
         ['ds', 'ef'], ['e', 'ff', 'dss'], ['es', 'f', 'gff'], ['fs', 'gf'], ['g', 'fss', 'aff'], ['gs', 'af'])
major_scale = 2, 2, 1, 2, 2, 2, 1

def mode(mode):

    # inferior algorithm with a loop & modulus
    pattern = []
    for mode_x in range(7):
        step = major_scale[(mode_x + mode - 1) % 7]
        pattern.append(step)

    # a better algorithm with slices
    x = mode - 1
    pattern2 = major_scale[x:] + major_scale[:x]

    print(pattern)
    print(pattern2)

print("Try:  mode(5)")
