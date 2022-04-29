from typing import Any

from reportlab import cmp as cmp
from reportlab.graphics.charts.areas import PlotArea as PlotArea
from reportlab.graphics.charts.legends import _objStr as _objStr
from reportlab.graphics.charts.textlabels import Label as Label
from reportlab.graphics.charts.utils3d import _2rad as _2rad
from reportlab.graphics.charts.utils3d import _180_pi as _180_pi
from reportlab.graphics.charts.utils3d import _360 as _360
from reportlab.graphics.charts.utils3d import _getShaded as _getShaded
from reportlab.graphics.shapes import STATE_DEFAULTS as STATE_DEFAULTS
from reportlab.graphics.shapes import ArcPath as ArcPath
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Ellipse as Ellipse
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Line as Line
from reportlab.graphics.shapes import Polygon as Polygon
from reportlab.graphics.shapes import PolyLine as PolyLine
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.shapes import String as String
from reportlab.graphics.shapes import Wedge as Wedge
from reportlab.graphics.widgetbase import PropHolder as PropHolder
from reportlab.graphics.widgetbase import (
    TypedPropertyCollection as TypedPropertyCollection,
)
from reportlab.graphics.widgets.markers import isSymbol as isSymbol
from reportlab.graphics.widgets.markers import uSymbol2Symbol as uSymbol2Symbol
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import *
from reportlab.lib.validators import EitherOr as EitherOr
from reportlab.lib.validators import NoneOr as NoneOr
from reportlab.lib.validators import OneOf as OneOf
from reportlab.lib.validators import isBoolean as isBoolean
from reportlab.lib.validators import isBoxAnchor as isBoxAnchor
from reportlab.lib.validators import isColorOrNone as isColorOrNone
from reportlab.lib.validators import isListOfColors as isListOfColors
from reportlab.lib.validators import isListOfNumbers as isListOfNumbers
from reportlab.lib.validators import isListOfNumbersOrNone as isListOfNumbersOrNone
from reportlab.lib.validators import isListOfStringsOrNone as isListOfStringsOrNone
from reportlab.lib.validators import (
    isNoneOrListOfNoneOrNumbers as isNoneOrListOfNoneOrNumbers,
)
from reportlab.lib.validators import (
    isNoneOrListOfNoneOrStrings as isNoneOrListOfNoneOrStrings,
)
from reportlab.lib.validators import isNumber as isNumber
from reportlab.lib.validators import isNumberInRange as isNumberInRange
from reportlab.lib.validators import isNumberOrNone as isNumberOrNone
from reportlab.lib.validators import isString as isString
from reportlab.lib.validators import isStringOrNone as isStringOrNone
from reportlab.lib.validators import isTextAnchor as isTextAnchor

__version__: str
__doc__: str
_ANGLE2BOXANCHOR: Any
_ANGLE2RBOXANCHOR: Any
_ANGLELO: float
_ANGLEHI: Any

class WedgeLabel(Label):
    def _checkDXY(self, ba) -> None: ...
    def _getBoxAnchor(self): ...

class WedgeProperties(PropHolder):
    _attrMap: Any
    strokeWidth: int
    fillColor: Any
    strokeColor: Any
    strokeDashArray: Any
    strokeLineJoin: int
    strokeLineCap: int
    strokeMiterLimit: int
    popout: int
    fontName: Any
    fontSize: Any
    fontColor: Any
    labelRadius: float
    label_dx: int
    label_text: Any
    label_topPadding: int
    label_boxAnchor: str
    label_boxStrokeColor: Any
    label_boxStrokeWidth: float
    label_boxFillColor: Any
    label_strokeColor: Any
    label_strokeWidth: float
    label_leading: Any
    label_textAnchor: str
    label_simple_pointer: int
    label_visible: int
    label_pointer_strokeColor: Any
    label_pointer_strokeWidth: float
    label_pointer_elbowLength: int
    label_pointer_edgePad: int
    label_pointer_piePad: int
    visible: int
    shadingKind: Any
    shadingAmount: float
    shadingAngle: float
    shadingDirection: str
    def __init__(self) -> None: ...

def _addWedgeLabel(self, text, angle, labelX, labelY, wedgeStyle, labelClass=...): ...
def _fixLabels(labels, n): ...

class AbstractPieChart(PlotArea):
    def makeSwatchSample(self, rowNo, x, y, width, height): ...
    def getSeriesName(self, i, default: Any | None = ...): ...

def boundsOverlap(P, Q): ...
def _findOverlapRun(B, i, wrap): ...
def findOverlapRun(B, wrap: int = ...): ...
def fixLabelOverlaps(L, sideLabels: bool = ..., mult0: float = ...) -> None: ...
def intervalIntersection(A, B): ...
def _makeSideArcDefs(sa, direction): ...
def _keyFLA(x, y): ...

_keyFLA: Any

def _findLargestArc(xArcs, side): ...
def _fPLSide(l, width, side: Any | None = ...): ...
def _fPLCF(a, b): ...

_fPLCF: Any

def _arcCF(a): ...
def _fixPointerLabels(n, L, x, y, width, height, side: Any | None = ...): ...
def theta0(data, direction): ...

class AngleData(float):
    _data: Any
    def __new__(cls, angle, data): ...

class Pie(AbstractPieChart):
    _attrMap: Any
    other_threshold: Any
    x: int
    y: int
    width: int
    height: int
    data: Any
    labels: Any
    startAngle: int
    direction: str
    simpleLabels: int
    checkLabelOverlap: int
    pointerLabelMode: Any
    sameRadii: bool
    orderMode: str
    xradius: Any
    sideLabels: int
    sideLabelsOffset: float
    slices: Any
    def __init__(self, **kwd) -> None: ...
    def demo(self): ...
    centerx: Any
    centery: Any
    yradius: Any
    lu: Any
    ru: Any
    def makePointerLabels(self, angles, plMode): ...
    def normalizeData(self, keepData: bool = ...): ...
    def makeAngles(self): ...
    _seriesCount: Any
    def makeWedges(self): ...
    def draw(self): ...

class LegendedPie(Pie):
    _attrMap: Any
    x: int
    y: int
    height: int
    width: int
    data: Any
    labels: Any
    direction: str
    pieAndLegend_colors: Any
    legendNumberOffset: int
    legendNumberFormat: str
    legend_data: Any
    legend1: Any
    legend_names: Any
    _legend2: Any
    leftPadding: int
    rightPadding: int
    topPadding: int
    bottomPadding: int
    drawLegend: int
    def __init__(self) -> None: ...
    def draw(self): ...
    def _getDrawingDimensions(self): ...
    def demo(self, drawing: Any | None = ...): ...

class Wedge3dProperties(PropHolder):
    _attrMap: Any
    strokeWidth: int
    shading: float
    visible: int
    strokeColorShaded: Any
    strokeColor: Any
    strokeDashArray: Any
    popout: int
    fontName: Any
    fontSize: Any
    fontColor: Any
    labelRadius: float
    label_dx: int
    label_text: Any
    label_topPadding: int
    label_boxAnchor: str
    label_boxStrokeColor: Any
    label_boxStrokeWidth: float
    label_boxFillColor: Any
    label_strokeColor: Any
    label_strokeWidth: float
    label_leading: Any
    label_textAnchor: str
    label_visible: int
    label_simple_pointer: int
    def __init__(self) -> None: ...

class _SL3D:
    lo: Any
    hi: Any
    mid: Any
    not360: Any
    def __init__(self, lo, hi) -> None: ...
    def __str__(self): ...

def _keyS3D(a, b): ...

_keyS3D: Any
_270r: Any

class Pie3d(Pie):
    _attrMap: Any
    perspective: int
    depth_3d: int
    angle_3d: int
    def _popout(self, i): ...
    def CX(self, i, d): ...
    def CY(self, i, d): ...
    def OX(self, i, o, d): ...
    def OY(self, i, o, d): ...
    def rad_dist(self, a): ...
    slices: Any
    xradius: Any
    width: int
    height: int
    data: Any
    def __init__(self) -> None: ...
    def _fillSide(self, L, i, angle, strokeColor, strokeWidth, fillColor) -> None: ...
    _xdepth_3d: Any
    _ydepth_3d: Any
    _cx: Any
    _cy: Any
    _radiusx: Any
    _radiusy: Any
    _seriesCount: Any
    _ody: Any
    dy: Any
    def draw(self): ...
    def demo(self): ...

def sample0a(): ...
def sample0b(): ...
def sample1(): ...
def sample2(): ...
def sample3(): ...
def sample4(): ...
def sample5(): ...
def sample6(): ...
def sample7(): ...
def sample8(): ...
def sample9(): ...
