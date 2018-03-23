"""
keys = ['c', 'f', 'bf', ...]

>>> pattern(key="c", scale_degree=2, pattern="1 b3 r 8  #6 5 b3 5", rhythm="4/4 8 8 8 8 8 8 8 8")
"d f a d b a f a"
>>> pattern("c", 5, "1 3 5 b7  8 9 8 b7")
"g b d f  g a g f"
>>> pattern("c", 1, "1 8' 2, 3  5 r b3 3")
"c c' d, e g a ef e"
>>> pattern("c", b2, "1 2 3 4  5 3 2 1")
"df ef f gb af f ef df"

*** for now: ***
>>> pattern("c", "1 2 b3 3 5 6 5 3")
"c d ef e  g a g e"
"""

def pattern(key, pat):
    pass
