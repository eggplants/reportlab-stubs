from typing import Any

from reportlab.graphics import shapes as shapes
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import *
from reportlab.lib.validators import *

__version__: str

class TableWidget(Widget):
    _attrMap: Any
    x: Any
    y: Any
    width: int
    height: int
    borderStrokeColor: Any
    fillColor: Any
    borderStrokeWidth: float
    horizontalDividerStrokeColor: Any
    verticalDividerStrokeColor: Any
    horizontalDividerStrokeWidth: float
    verticalDividerStrokeWidth: float
    dividerDashArray: Any
    data: Any
    boxAnchor: str
    fontSize: int
    fontColor: Any
    alignment: str
    textAnchor: str
    def __init__(self, x: int = ..., y: int = ..., **kw) -> None: ...
    def demo(self): ...
    def draw(self): ...
    def preProcessData(self, data): ...
