from typing import Any

from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Line as Line
from reportlab.graphics.shapes import Polygon as Polygon
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.lib.attrmap import AttrMap as AttrMap
from reportlab.lib.attrmap import AttrMapValue as AttrMapValue
from reportlab.lib.colors import grey as grey
from reportlab.lib.validators import isColorOrNone as isColorOrNone
from reportlab.lib.validators import isNoneOrShape as isNoneOrShape
from reportlab.lib.validators import isNumber as isNumber

__version__: str
__doc__: str

class PlotArea(Widget):
    _attrMap: Any
    x: int
    y: int
    height: int
    width: int
    strokeColor: Any
    strokeWidth: int
    fillColor: Any
    background: Any
    debug: int
    def __init__(self) -> None: ...
    def makeBackground(self): ...
