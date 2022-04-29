from typing import Any

from reportlab.graphics.shapes import Circle as Circle
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Polygon as Polygon
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.graphics.widgets.flags import Flag as Flag
from reportlab.graphics.widgets.flags import _Symbol as _Symbol
from reportlab.graphics.widgets.signsandsymbols import SmileyFace as SmileyFace
from reportlab.lib.attrmap import AttrMap as AttrMap
from reportlab.lib.attrmap import AttrMapValue as AttrMapValue
from reportlab.lib.colors import black as black
from reportlab.lib.utils import isClass as isClass
from reportlab.lib.validators import OneOf as OneOf
from reportlab.lib.validators import Validator as Validator
from reportlab.lib.validators import isColorOrNone as isColorOrNone
from reportlab.lib.validators import isNumber as isNumber

__version__: str
__doc__: str
_toradians: Any

class Marker(Widget):
    _attrMap: Any
    def __init__(self, *args, **kw) -> None: ...
    def clone(self, **kwds): ...
    def _Smiley(self): ...
    def _Square(self): ...
    def _Diamond(self): ...
    def _Circle(self): ...
    def _Cross(self): ...
    def _Triangle(self): ...
    def _StarSix(self): ...
    def _StarFive(self): ...
    def _Pentagon(self): ...
    def _Hexagon(self): ...
    def _Heptagon(self): ...
    def _Octagon(self): ...
    def _ArrowHead(self): ...
    def _doPolygon(self, P): ...
    fillColor: Any
    def _doFill(self): ...
    def _doNgon(self, n): ...
    _FilledCircle: Any
    _FilledSquare: Any
    _FilledDiamond: Any
    _FilledCross: Any
    _FilledTriangle: Any
    _FilledStarSix: Any
    _FilledPentagon: Any
    _FilledHexagon: Any
    _FilledHeptagon: Any
    _FilledOctagon: Any
    _FilledStarFive: Any
    _FilledArrowHead: Any
    def draw(self): ...

def uSymbol2Symbol(uSymbol, x, y, color): ...

class _isSymbol(Validator):
    def test(self, x): ...

isSymbol: Any

def makeMarker(name, **kw): ...
