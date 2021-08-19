# rHEALPix DGGS Simple Feature functions 

This library contains functions for evaluating Simple Feature relations between DGGS Cells and sets of these.
A wrapped version of this library is available as an RDFLib extension for GeoSPARQL queries: [geosparql-dggs](https://github.com/RDFLib/geosparql-dggs).
  
## Installation 
Coming to PyPI.

This package depends on the [rhealpix-geo](https://github.com/surroundaustralia/rhealpix-geo) package to represent valid sets of Cells, and perform low level operations required to implement these functions.

## Use
These functions are implemented in the file `rhealsf/dggs_functions.py`

This means they can be used like this (full working script):

```python
from rhealsf import sfContains, sfEquals, sfDisjoint, sfOverlaps, sfWithin, sfTouches, sfIntersects

a = "R1"
b = "R11"
c = "R2"
d = "R1 R2"
e = "R2 R3"

print(f"a contains b, expected True, returns: {sfContains(a, b)}")
print(f"b contains a, expected False, returns: {sfContains(b, a)}")
print(f"a equals a, expected True, returns: {sfEquals(a, a)}")
print(f"a equals b, expected False, returns: {sfEquals(a, b)}")
print(f"a disjoint b, expected False, returns: {sfDisjoint(a, b)}")
print(f"b disjoint c, expected True, returns: {sfDisjoint(b, c)}")
print(f"a overlaps d, expected False (within), returns: {sfOverlaps(a, d)}")
print(f"d overlaps e, expected True, returns: {sfOverlaps(d, e)}")
print(f"c within d, expected True, returns: {sfWithin(c, d)}")
print(f"d within c, expected False, returns: {sfWithin(d, c)}")
print(f"a touches b, expected False, returns: {sfTouches(a, b)}")
print(f"a touches c, expected True, returns: {sfTouches(a, c)}")
print(f"a intersects b, expected True, returns: {sfIntersects(a, b)}")
print(f"b intersects c, expected False, returns: {sfIntersects(b, c)}")
```

## Function Definitions

**sfEqual:** Two sets of cells are equal if they have the same identifier.  
**sfWithin:** One set of cells (A) is within some other set of cells (B) if the addition of A's cells to B results in a set of cells equal to B, where A is not equal to B.  
**sfContains:** One set of cells (A) is contains some other set of cells (B) if the addition of A's cells to B results in a set of cells equal to A, where A is not equal to B.  
**sfIntersects:** One set of cells (A) intersects some other set of cells (B) where they share any two cells, or any cell in A is the parent or child of a cell in B, or any cell in A or B touches.  
**sfTouches:** One set of cells (A) touches some other set of cells (B) where the cells meet at an edge, or vertex.  
**sfDisjoint:** One set of cells (A) is disjoint with some other set of cells (B) where they do not share any two cells, no cell in A is the parent or child of a cell in B, and no cells in A and B touch.  
**sfOverlaps:** One set of cells (A) overlaps some other set of cells (B) where the addition of A's cells to B results in a set of cells different from A and B, and A and B are not disjoint and do not touch.   

## Testing
All tests are in `tests/` and implemented using [unittest](http://docs.python.org/library/unittest.html).

There are sets of tests for each of the Simple Feature functions. 

## Contributing
Via GitHub, Issues & Pull Requests: 

* <https://github.com/surroundaustralia/rhealpix-sf

## License
This code is licensed with the BSD 3-clause license as per [LICENSE](LICENSE).

## Citation
```bibtex
@software{https://github.com/surroundaustralia/rhealpix-sf,
  author = {{David Habgood}},
  title = {Simple Feature functions for rHEALPix DGGS},
  version = {0.0.1},
  date = {2021},
  url = {https://github.com/surroundaustralia/rhealpix-sf}
}
```

## Contact
_Creator & maintainer:_  
**David Habgood**  
_Application Architect_  
[SURROUND Australia Pty Ltd](https://surroundaustralia.com)  
<david.habgood@surroundaustrlaia.com>  

https://orcid.org/0000-0002-3322-1868
