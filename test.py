letters = 'a', 'b', 'c', 'd', 'e', 'f', 'g'
notes = (['a', 'gss', 'bff'], ['as', 'bf'], ['b', 'cf', 'ass'], ['bs', 'c', 'dff'], ['cs', 'df'], ['d', 'css', 'eff'], 
         ['ds', 'ef'], ['e', 'ff', 'dss'], ['es', 'f', 'gff'], ['fs', 'gf'], ['g', 'fss', 'aff'], ['gs', 'af'])
major_scale = 2, 2, 1, 2, 2, 2, 1

def mode(one, mode):

    scale = []
    m = mode
    for mx in range(7):
        step = major_scale[(mx + m - 1) % 7]
        scale.append(step)
    print scale


mode('a', 5)
