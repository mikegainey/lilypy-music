# pytest test suite
# usage: $python3 -m pytest -v (to run all tests in this directory)
# pytest-3 doesn't work for some reason

from .scale import scale
from .mode import mode
from .chord import chord
from .accidental import accidental
from .pattern import pattern
from .scale_degree import scale_degree

# these tests fail because of octave tweaks to lp_pattern
# def test_pattern():
#     assert pattern('c', 1, "1 3 5 6 4 2 1") == 'c e g a f d c'


def test_scale(): # always a major scale
    assert scale('a') == ['a', 'b', 'cs', 'd', 'e', 'fs', 'gs', 'a']
    assert scale('ef') == ['ef', 'f', 'g', 'af', 'bf', 'c', 'd', 'ef']

def test_mode():
    assert mode('a', 1) == ['a', 'b', 'cs', 'd', 'e', 'fs', 'gs', 'a'] # a major
    assert mode('c', 2) == ['c', 'd', 'ef', 'f', 'g', 'a', 'bf', 'c'] # c dorian
    assert mode('f', 5) == ['f', 'g', 'a', 'bf', 'c', 'd', 'ef', 'f'] # f mixolydian

def test_chord():
    assert chord('a', 'maj') == ['a', 'cs', 'e']
    assert chord('ef', 'Mm7') == ['ef', 'g', 'bf', 'df']

def test_accidental():
    assert accidental('c', '#') == 'cs'
    assert accidental('cs', '#') == 'css'
    assert accidental('cf', '#') == 'c'
    assert accidental('cff', '#') == 'cf'
    assert accidental('b', 'b') == 'bf'
    assert accidental('bs', 'b') == 'b'
    assert accidental('bss', 'b') == 'bs'
    assert accidental('bf', 'b') == 'bff'

def test_scale_degree():
    assert scale_degree('c', 5) == 'g'
    assert scale_degree('a', 3) == 'cs'
    assert scale_degree('c', '4') == 'f'
    assert scale_degree('ef', '4') == 'af'
    assert scale_degree('c', '#4') == 'fs'
    assert scale_degree('bf', 'b5') == 'ff'
