# Given a root note (like 'c') and a scale degree (like b5), return the note (in this case, gf).
# Uses scale.py and accidental.py

from .scale import scale
from .accidental import accidental


def scale_degree(note, degree):
    """
   >>> scale_degree('c','b5')
   'gf'
   >>> scale_degree('d','3')
   'fs'
   >>> scale_degree('ef','b7')
   'df'
   """
    key_scale = scale(note)
    # degree is an int
    if type(degree) == int:
        return key_scale[degree - 1]
    # degree is a numeric string
    if len(degree) == 1:
        degree = int(degree)
        return key_scale[degree - 1]
    else:  # assume len == 2
        base = int(degree[1])
        acc = degree[0]
        basenote = key_scale[base - 1]
        realnote = accidental(basenote, acc)
        return realnote
