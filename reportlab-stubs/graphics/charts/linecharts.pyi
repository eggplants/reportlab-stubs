from typing import Any

from reportlab.graphics.charts.areas import PlotArea as PlotArea
from reportlab.graphics.charts.axes import XCategoryAxis as XCategoryAxis
from reportlab.graphics.charts.axes import YValueAxis as YValueAxis
from reportlab.graphics.charts.legends import _objStr as _objStr
from reportlab.graphics.charts.textlabels import Label as Label
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
from reportlab.graphics.widgetbase import tpcGetItem as tpcGetItem
from reportlab.graphics.widgets.markers import isSymbol as isSymbol
from reportlab.graphics.widgets.markers import makeMarker as makeMarker
from reportlab.graphics.widgets.markers import uSymbol2Symbol as uSymbol2Symbol
from reportlab.graphics.widgets.signsandsymbols import NoEntry as NoEntry
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import *
from reportlab.lib.utils import flatten as flatten
from reportlab.lib.validators import NoneOr as NoneOr
from reportlab.lib.validators import OneOf as OneOf
from reportlab.lib.validators import Percentage as Percentage
from reportlab.lib.validators import isBoolean as isBoolean
from reportlab.lib.validators import isColorOrNone as isColorOrNone
from reportlab.lib.validators import isListOfNumbersOrNone as isListOfNumbersOrNone
from reportlab.lib.validators import isListOfStringsOrNone as isListOfStringsOrNone
from reportlab.lib.validators import isNumber as isNumber
from reportlab.lib.validators import isNumberOrNone as isNumberOrNone
from reportlab.lib.validators import isStringOrNone as isStringOrNone

from .utils import FillPairedData as FillPairedData

__version__: str
__doc__: str

class LineChartProperties(PropHolder):
    _attrMap: Any

class AbstractLineChart(PlotArea):
    def makeSwatchSample(self, rowNo, x, y, width, height): ...
    def getSeriesName(self, i, default: Any | None = ...): ...

class LineChart(AbstractLineChart): ...

class HorizontalLineChart(LineChart):
    _attrMap: Any
    strokeColor: Any
    fillColor: Any
    categoryAxis: Any
    valueAxis: Any
    data: Any
    categoryNames: Any
    lines: Any
    useAbsolute: int
    groupSpacing: int
    lineLabels: Any
    lineLabelFormat: Any
    lineLabelArray: Any
    lineLabelNudge: int
    joinedLines: int
    inFill: int
    reversePlotOrder: int
    def __init__(self) -> None: ...
    def demo(self): ...
    _seriesCount: Any
    _rowLength: Any
    _normFactor: Any
    _yzero: Any
    _hngs: Any
    _pairInFills: Any
    _positions: Any
    def calcPositions(self) -> None: ...
    def _innerDrawLabel(self, rowNo, colNo, x, y): ...
    def drawLabel(self, G, rowNo, colNo, x, y) -> None: ...
    def makeLines(self): ...
    _inFillG: Any
    def draw(self): ...

def _fakeItemKey(a): ...

class _FakeGroup:
    _data: Any
    def __init__(self) -> None: ...
    def add(self, what) -> None: ...
    def value(self): ...
    def sort(self) -> None: ...

class HorizontalLineChart3D(HorizontalLineChart):
    _attrMap: Any
    theta_x: float
    theta_y: float
    zDepth: int
    zSpace: int
    _3d_dx: Any
    _3d_dy: Any
    def calcPositions(self) -> None: ...
    def _calc_z0(self, rowNo): ...
    def _zadjust(self, x, y, z): ...
    def makeLines(self): ...

class VerticalLineChart(LineChart): ...

def sample1(): ...

class SampleHorizontalLineChart(HorizontalLineChart):
    def demo(self): ...
    def makeBackground(self): ...

def sample1a(): ...
def sample2(): ...
def sample3(): ...
def sampleCandleStick(): ...
