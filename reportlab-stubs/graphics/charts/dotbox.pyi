from typing import Any

from reportlab.graphics.charts.lineplots import _maxWidth as _maxWidth
from reportlab.graphics.charts.textlabels import Label as Label
from reportlab.graphics.shapes import Circle as Circle
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Line as Line
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.shapes import String as String
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.lib.attrmap import *
from reportlab.lib.colors import _PCMYK_black as _PCMYK_black
from reportlab.lib.units import cm as cm
from reportlab.lib.validators import *
from reportlab.pdfbase.pdfmetrics import getFont as getFont

class DotBox(Widget):
    _attrMap: Any
    xlabels: Any
    ylabels: Any
    labelFontName: str
    labelFontSize: int
    labelOffset: int
    strokeWidth: float
    gridDivWidth: Any
    gridColor: Any
    dotDiameter: Any
    dotColor: Any
    dotXPosition: int
    dotYPosition: int
    x: int
    y: int
    def __init__(self) -> None: ...
    def _getDrawingDimensions(self): ...
    def demo(self, drawing: Any | None = ...): ...
    def draw(self): ...
