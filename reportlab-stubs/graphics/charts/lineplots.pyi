from typing import Any

from reportlab.graphics.charts.areas import PlotArea as PlotArea
from reportlab.graphics.charts.axes import AdjYValueAxis as AdjYValueAxis
from reportlab.graphics.charts.axes import NormalDateXValueAxis as NormalDateXValueAxis
from reportlab.graphics.charts.axes import XValueAxis as XValueAxis
from reportlab.graphics.charts.axes import YValueAxis as YValueAxis
from reportlab.graphics.charts.linecharts import AbstractLineChart as AbstractLineChart
from reportlab.graphics.charts.textlabels import Label as Label
from reportlab.graphics.charts.utils import *
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Polygon as Polygon
from reportlab.graphics.shapes import PolyLine as PolyLine
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.shapes import _SetKeyWordArgs as _SetKeyWordArgs
from reportlab.graphics.widgetbase import PropHolder as PropHolder
from reportlab.graphics.widgetbase import (
    TypedPropertyCollection as TypedPropertyCollection,
)
from reportlab.graphics.widgetbase import tpcGetItem as tpcGetItem
from reportlab.graphics.widgets.grids import DoubleGrid as DoubleGrid
from reportlab.graphics.widgets.grids import Grid as Grid
from reportlab.graphics.widgets.grids import ShadedPolygon as ShadedPolygon
from reportlab.graphics.widgets.markers import makeMarker as makeMarker
from reportlab.graphics.widgets.markers import uSymbol2Symbol as uSymbol2Symbol
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import *
from reportlab.lib.utils import flatten as flatten
from reportlab.lib.utils import isStr as isStr
from reportlab.lib.validators import *
from reportlab.pdfbase.pdfmetrics import getFont as getFont
from reportlab.pdfbase.pdfmetrics import stringWidth as stringWidth

from .utils import FillPairedData as FillPairedData

__version__: str
__doc__: str

class LinePlotProperties(PropHolder):
    _attrMap: Any

class InFillValue(int):
    yValue: Any
    def __new__(cls, v, yValue: Any | None = ...): ...

class Shader(_SetKeyWordArgs):
    _attrMap: Any
    def shade(self, lp, g, rowNo, rowColor, row) -> None: ...

class NoFiller:
    def fill(self, lp, g, rowNo, rowColor, points) -> None: ...

class Filler:
    _attrMap: Any
    __dict__: Any
    def __init__(self, **kw) -> None: ...
    def fill(self, lp, g, rowNo, rowColor, points) -> None: ...

class ShadedPolyFiller(Filler, ShadedPolygon): ...
class PolyFiller(Filler, Polygon): ...

class LinePlot(AbstractLineChart):
    _attrMap: Any
    reversePlotOrder: int
    xValueAxis: Any
    yValueAxis: Any
    data: Any
    lines: Any
    lineLabels: Any
    lineLabelFormat: Any
    lineLabelArray: Any
    lineLabelNudge: int
    joinedLines: int
    _inFill: Any
    annotations: Any
    behindAxes: int
    gridFirst: int
    def __init__(self) -> None: ...
    def demo(self): ...
    _seriesCount: Any
    _rowLength: Any
    _pairInFills: Any
    _positions: Any
    def calcPositions(self) -> None: ...
    def _innerDrawLabel(self, rowNo, colNo, x, y): ...
    def drawLabel(self, G, rowNo, colNo, x, y) -> None: ...
    def makeLines(self): ...
    _inFillG: Any
    _lineG: Any
    def draw(self): ...
    def addCrossHair(
        self,
        name,
        xv,
        yv,
        strokeColor=...,
        strokeWidth: int = ...,
        beforeLines: bool = ...,
    ): ...

class LinePlot3D(LinePlot):
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

_monthlyIndexData: Any

class SimpleTimeSeriesPlot(LinePlot):
    xValueAxis: Any
    yValueAxis: Any
    data: Any
    def __init__(self) -> None: ...

class GridLinePlot(SimpleTimeSeriesPlot):
    _attrMap: Any
    scaleFactor: Any
    background: Any
    def __init__(self) -> None: ...
    def demo(self, drawing: Any | None = ...): ...
    def draw(self): ...

class AreaLinePlot(LinePlot):
    _inFill: int
    reversePlotOrder: int
    data: Any
    def __init__(self) -> None: ...
    def draw(self): ...

class SplitLinePlot(AreaLinePlot):
    xValueAxis: Any
    yValueAxis: Any
    data: Any
    def __init__(self) -> None: ...

def _maxWidth(T, fontName, fontSize): ...

class ScatterPlot(LinePlot):
    _attrMap: Any
    width: int
    height: int
    outerBorderOn: int
    outerBorderColor: Any
    background: Any
    xLabel: str
    yLabel: str
    data: Any
    joinedLines: int
    leftPadding: int
    rightPadding: int
    topPadding: int
    bottomPadding: int
    x: Any
    y: Any
    lineLabelFormat: str
    lineLabelNudge: int
    def __init__(self) -> None: ...
    def _getDrawingDimensions(self): ...
    def demo(self, drawing: Any | None = ...): ...
    def draw(self): ...

def sample1a(): ...
def sample1b(): ...
def sample1c(): ...
def preprocessData(series): ...
def sample2(): ...
def sampleFillPairedData(): ...
