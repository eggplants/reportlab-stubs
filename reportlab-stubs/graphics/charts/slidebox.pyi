from typing import Any

from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Polygon as Polygon
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.shapes import String as String
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.graphics.widgets.grids import ShadedRect as ShadedRect
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import *
from reportlab.lib.colors import black as black
from reportlab.lib.colors import white as white
from reportlab.lib.units import cm as cm
from reportlab.lib.validators import *
from reportlab.pdfbase.pdfmetrics import getFont as getFont

class SlideBox(Widget):
    _attrMap: Any
    labelFontName: str
    labelFontSize: int
    labelStrokeColor: Any
    labelFillColor: Any
    startColor: Any
    endColor: Any
    numberOfBoxes: int
    trianglePosition: int
    triangleHeight: Any
    triangleWidth: Any
    triangleFillColor: Any
    triangleStrokeColor: Any
    triangleStrokeWidth: float
    boxHeight: Any
    boxWidth: Any
    boxSpacing: Any
    boxOutlineColor: Any
    boxOutlineWidth: float
    leftPadding: int
    rightPadding: int
    topPadding: int
    bottomPadding: int
    background: Any
    sourceLabelText: str
    sourceLabelOffset: Any
    sourceLabelFontName: str
    sourceLabelFontSize: int
    sourceLabelFillColor: Any
    def __init__(self) -> None: ...
    def _getDrawingDimensions(self): ...
    def _getColors(self): ...
    def demo(self, drawing: Any | None = ...): ...
    def draw(self): ...
