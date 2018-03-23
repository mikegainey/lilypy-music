# test lilypy package structure

from lilypy.scale import scale
from lilypy.mode import mode
from lilypy.chord import chord

a = scale('a')
print(f"A major: {a}")

bfmix = mode('bf', 5)
print(f"B-flat mixolydian: {bfmix}")

fmin = chord('f', 'min')
print(f"F minor triad: {fmin}")
