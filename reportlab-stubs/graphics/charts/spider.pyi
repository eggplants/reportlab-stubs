from typing import Any

from reportlab.graphics.charts.areas import PlotArea as PlotArea
from reportlab.graphics.charts.legends import _objStr as _objStr
from reportlab.graphics.charts.piecharts import WedgeLabel as WedgeLabel
from reportlab.graphics.shapes import STATE_DEFAULTS as STATE_DEFAULTS
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Line as Line
from reportlab.graphics.shapes import Polygon as Polygon
from reportlab.graphics.shapes import PolyLine as PolyLine
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.widgetbase import PropHolder as PropHolder
from reportlab.graphics.widgetbase import (
    TypedPropertyCollection as TypedPropertyCollection,
)
from reportlab.graphics.widgets.markers import isSymbol as isSymbol
from reportlab.graphics.widgets.markers import makeMarker as makeMarker
from reportlab.graphics.widgets.markers import uSymbol2Symbol as uSymbol2Symbol
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import *
from reportlab.lib.validators import EitherOr as EitherOr
from reportlab.lib.validators import OneOf as OneOf
from reportlab.lib.validators import isBoolean as isBoolean
from reportlab.lib.validators import isCallable as isCallable
from reportlab.lib.validators import isColorOrNone as isColorOrNone
from reportlab.lib.validators import isListOfNumbersOrNone as isListOfNumbersOrNone
from reportlab.lib.validators import isListOfStringsOrNone as isListOfStringsOrNone
from reportlab.lib.validators import isNumber as isNumber
from reportlab.lib.validators import isNumberOrNone as isNumberOrNone
from reportlab.lib.validators import isStringOrNone as isStringOrNone

__version__: str
__doc__: str

class StrandProperty(PropHolder):
    _attrMap: Any
    strokeWidth: int
    fillColor: Any
    strokeColor: Any
    strokeDashArray: Any
    symbol: Any
    symbolSize: int
    name: Any
    def __init__(self) -> None: ...

class SpokeProperty(PropHolder):
    _attrMap: Any
    strokeWidth: float
    fillColor: Any
    strokeColor: Any
    strokeDashArray: Any
    visible: int
    labelRadius: float
    def __init__(self, **kw) -> None: ...

class SpokeLabel(WedgeLabel):
    _text: str
    def __init__(self, **kw) -> None: ...

class StrandLabel(SpokeLabel):
    _attrMap: Any
    format: str
    dR: int
    def __init__(self, **kw) -> None: ...

def _setupLabel(labelClass, text, radius, cx, cy, angle, car, sar, sty): ...

class SpiderChart(PlotArea):
    _attrMap: Any
    def makeSwatchSample(self, rowNo, x, y, width, height): ...
    def getSeriesName(self, i, default: Any | None = ...): ...
    data: Any
    labels: Any
    startAngle: int
    direction: str
    strands: Any
    spokes: Any
    spokeLabels: Any
    strandLabels: Any
    x: int
    y: int
    width: int
    height: int
    def __init__(self) -> None: ...
    def demo(self): ...
    _norm: Any
    def normalizeData(self, outer: float = ...): ...
    def _innerDrawLabel(self, sty, radius, cx, cy, angle, car, sar, labelClass=...): ...
    _radius: Any
    _seriesCount: Any
    def draw(self): ...

def sample1(): ...
def sample2(): ...
