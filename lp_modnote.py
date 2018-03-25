"""
>>> modnote("cff", "#")
'cf'
>>> modnote("cf", "#")
'c'
>>> modnote("c", "#")
'cs'
>>> modnote("cs", "#")
'css'
>>> modnote("css", "b")
'cs'
>>> modnote("cs", "b")
'c'
>>> modnote("c", "b")
'cf'
>>> modnote("cf", "b")
'cff'
"""

def modnote(note, mod): # the note and modifier (b or #)
    if mod not in ("b", "#"):
        return note

    elif mod == "b":
        if note[-1] == "s":
            return note[:-1]  # css -> cs and cs -> c
        else:
            return f"{note}f" # c -> cf and cf -> cff

    else: # mod == "#":
        if len(note) >= 2 and note[-1] == "f":
            return note[:-1]  # cff -> cf and cf -> c
        else:
            return f"{note}s" # c -> cs and cs -> css

