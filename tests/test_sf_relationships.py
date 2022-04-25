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

def test_sf_touches_large_coll():
    # two L7 collections that TOUCH on an edge, converted using the CENTROID method
    cells_geom_a = """P007227 P007228 P007251 P007252 P008006 P008030 P0072243 P0072244 P0072245 P0072246 P0072247 P0072248 P0072253 P0072254 P0072255 P0072256 P0072257 P0072258 P0072540 P0072541 P0072542 P0072550 P0072551 P0072552 P0080033 P0080034 P0080035 P0080036 P0080037 P0080038 P0080330 P0080331 P0080332"""
    cells_geom_c = """P008007 P0080043 P0080044 P0080045 P0080046 P0080047 P0080048 P0080053 P0080054 P0080056 P0080057 P0080080 P0080081 P0080083 P0080084 P0080086 P0080087"""
    assert sfTouches(cells_geom_a, cells_geom_c)

def test_sf_overlaps_large_coll():
    # two L7 collections that OVERLAP on an edge, converted using the INTERSECTS method
    cells_geom_a = """P007224 P007225 P007227 P007228 P007251 P007252 P008003 P008006 P008030 P0072232 P0072235 P0072238 P0072262 P0072265 P0072268 P0072502 P0072505 P0072508 P0072532 P0072535 P0072540 P0072541 P0072542 P0072543 P0072544 P0072545 P0072550 P0072551 P0072552 P0072553 P0072554 P0072555 P0080040 P0080043 P0080046 P0080070 P0080073 P0080076 P0080310 P0080313 P0080316 P0080330 P0080331 P0080332 P0080333 P0080334 P0080335 P0080340 P0080343"""
    cells_geom_c = """P008004 P008005 P008007 P008008"""
    assert sfOverlaps(cells_geom_a, cells_geom_c)
