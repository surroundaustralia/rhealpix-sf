"""
This Python 3.8 code tests the ``sources.dggs_functions`` module.
Beware, these tests cover only some functions and only some scenarios.
Keep adding tests!
CHANGELOG:
- 2021-07-19:   David Habgood (DH): Initial version
- 2021-09-20:   DH: converted from Unittest to pytest, minor bugfixes
"""
from rhealsf import *


# equals
def test_sf_equals():
    assert sfEquals("P1", "P1")

def test_sf_not_equals():
    assert not sfEquals("P1", "P2")

# overlaps
def test_sf_overlaps():
    assert sfOverlaps("P1 P2", "P2 P3")

def test_sf_not_overlaps_equal():
    assert not sfOverlaps("P1", "P1")

def test_sf_not_overlaps_disjoint():
    assert not sfOverlaps("P1", "P2")

def test_sf_not_overlaps_within():
    assert not sfOverlaps("P100", "P1")

def test_sf_not_overlaps_contains():
    assert not sfOverlaps("P1", "P100")

# disjoint
def test_sf_disjoint():
    assert sfDisjoint("P0", "P2")

def test_sf_disjoint():
    assert not sfDisjoint("P1", "P1")

def test_sf_not_disjoint():
    assert not sfDisjoint("P1", "P2")

def test_sf_disjoint_different_res():
    assert not sfDisjoint("P100", "P1")

def test_sf_disjoint_list_str():
    assert not sfDisjoint("P1 P2", "P100")

def test_sf_disjoint_list_str():
    assert not sfDisjoint("P1 P2", "P3")

# contains
def test_sf_contains():
    assert sfContains("P1", "P123")

def test_sf_not_contains_within():
    assert not sfContains("P1", "P1 P2")

def test_sf_not_contains_equal():
    assert not sfContains("P1", "P1")

def test_sf_not_contains_overlaps():
    assert not sfContains("P1 P2", "P2 P3")

# within
def test_sf_within():
    assert sfWithin("P1", "P1 P2")

def test_sf_not_within_contains():
    assert not sfWithin("P1", "P123")

def test_sf_not_within_equal():
    assert not sfWithin("P1", "P1")

def test_sf_not_within_overlaps():
    assert not sfWithin("P1 P2", "P2 P3")

# touches
def test_sf_touches_true_basic():
    assert sfTouches("P1", "P2")

def test_sf_touches_true_diagonal():
    assert sfTouches("P1", "P5")

def test_sf_touches_false():
    assert not sfTouches("P1", "P7")

def test_sf_touches_false_2():
    assert not sfTouches("P1", "P1")

def test_sf_touches_false_3():
    assert not sfTouches("R03 R04", "R03 R04 R06 R07")

if __name__ == '__main__':
    test_sf_overlaps()
