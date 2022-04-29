from typing import Any

from reportlab.graphics import renderPDF as renderPDF
from reportlab.graphics.shapes import Circle as Circle
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Line as Line
from reportlab.graphics.shapes import Polygon as Polygon
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.shapes import String as String
from reportlab.graphics.shapes import Wedge as Wedge
from reportlab.graphics.widgets.signsandsymbols import _Symbol as _Symbol
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import *
from reportlab.lib.validators import *

__version__: str
__doc__: str
validFlag: Any
_size: float

class Star(_Symbol):
    _attrMap: Any
    _size: float
    size: int
    fillColor: Any
    strokeColor: Any
    angle: int
    def __init__(self) -> None: ...
    def demo(self): ...
    def draw(self): ...

class Flag(_Symbol):
    _attrMap: Any
    _cache: Any
    kind: Any
    size: int
    fillColor: Any
    border: int
    def __init__(self, **kw) -> None: ...
    def availableFlagNames(self): ...
    def _Flag_None(self): ...
    def _borderDraw(self, f): ...
    def draw(self): ...
    def clone(self): ...
    def demo(self): ...
    def _Flag_UK(self): ...
    def _Flag_USA(self): ...
    def _Flag_Afghanistan(self): ...
    def _Flag_Austria(self): ...
    def _Flag_Belgium(self): ...
    _width: Any
    def _Flag_China(self): ...
    def _Flag_Cuba(self): ...
    def _Flag_Denmark(self): ...
    def _Flag_Finland(self): ...
    def _Flag_France(self): ...
    def _Flag_Germany(self): ...
    def _Flag_Greece(self): ...
    def _Flag_Ireland(self): ...
    def _Flag_Italy(self): ...
    def _Flag_Japan(self): ...
    def _Flag_Luxembourg(self): ...
    def _Flag_Holland(self): ...
    def _Flag_Portugal(self): ...
    def _Flag_Russia(self): ...
    def _Flag_Spain(self): ...
    def _Flag_Sweden(self): ...
    def _Flag_Norway(self): ...
    def _Flag_CzechRepublic(self): ...
    def _Flag_Palestine(self): ...
    def _Flag_Turkey(self): ...
    def _Flag_Switzerland(self): ...
    def _Flag_EU(self): ...
    def _Flag_Brazil(self): ...

def makeFlag(name): ...
def test() -> None: ...
