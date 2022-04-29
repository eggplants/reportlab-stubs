from typing import Any

from reportlab.graphics.charts.utils import CustomDrawChanger as CustomDrawChanger
from reportlab.graphics.shapes import STATE_DEFAULTS as STATE_DEFAULTS
from reportlab.graphics.shapes import Circle as Circle
from reportlab.graphics.shapes import DirectDraw as DirectDraw
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.shapes import String as String
from reportlab.graphics.widgetbase import PropHolder as PropHolder
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import *
from reportlab.lib.enums import TA_CENTER as TA_CENTER
from reportlab.lib.enums import TA_LEFT as TA_LEFT
from reportlab.lib.enums import TA_RIGHT as TA_RIGHT
from reportlab.lib.styles import ParagraphStyle as ParagraphStyle
from reportlab.lib.styles import PropertySet as PropertySet
from reportlab.lib.utils import simpleSplit as simpleSplit
from reportlab.lib.validators import NoneOr as NoneOr
from reportlab.lib.validators import OneOf as OneOf
from reportlab.lib.validators import isBoolean as isBoolean
from reportlab.lib.validators import isBoxAnchor as isBoxAnchor
from reportlab.lib.validators import isColorOrNone as isColorOrNone
from reportlab.lib.validators import isInstanceOf as isInstanceOf
from reportlab.lib.validators import isNoneOrCallable as isNoneOrCallable
from reportlab.lib.validators import isNoneOrString as isNoneOrString
from reportlab.lib.validators import isNumber as isNumber
from reportlab.lib.validators import isNumberOrNone as isNumberOrNone
from reportlab.lib.validators import isString as isString
from reportlab.lib.validators import isSubclassOf as isSubclassOf
from reportlab.lib.validators import isTextAnchor as isTextAnchor
from reportlab.pdfbase.pdfmetrics import getAscentDescent as getAscentDescent
from reportlab.pdfbase.pdfmetrics import stringWidth as stringWidth
from reportlab.platypus import Flowable as Flowable
from reportlab.platypus import XPreformatted as XPreformatted

__version__: str
_ta2al: Any
_A2BA: Any
_BA2TA: Any

class Label(Widget):
    _attrMap: Any
    def __init__(self, **kw) -> None: ...
    _text: Any
    def setText(self, text) -> None: ...
    x: Any
    y: Any
    def setOrigin(self, x, y) -> None: ...
    def demo(self): ...
    def _getBoxAnchor(self): ...
    _baselineRatio: Any
    def _getBaseLineRatio(self) -> None: ...
    _height: Any
    _ewidth: Any
    _eheight: Any
    _top: Any
    _bottom: Any
    _left: Any
    _right: Any
    def _computeSizeEnd(self, objH) -> None: ...
    _lineWidths: Any
    _lines: Any
    _width: Any
    _leading: Any
    _style: Any
    _ddfObj: Any
    def computeSize(self) -> None: ...
    def _getTextAnchor(self): ...
    def _rawDraw(self): ...
    def draw(self): ...

class LabelDecorator:
    _attrMap: Any
    textAnchor: str
    boxAnchor: str
    def __init__(self) -> None: ...
    def decorate(self, l, L) -> None: ...
    def __call__(self, l) -> None: ...

isOffsetMode: Any

class LabelOffset(PropHolder):
    _attrMap: Any
    posMode: str
    pos: int
    def __init__(self) -> None: ...
    def _getValue(self, chart, val): ...

NoneOrInstanceOfLabelOffset: Any

class PMVLabel(Label):
    _attrMap: Any
    _pmv: int
    def __init__(self, **kwds) -> None: ...
    def _getBoxAnchor(self): ...
    def _getTextAnchor(self): ...

class BarChartLabel(PMVLabel):
    _attrMap: Any
    lineStrokeWidth: int
    lineStrokeColor: Any
    fixedStart: Any
    nudge: int
    def __init__(self, **kwds) -> None: ...

class NA_Label(BarChartLabel):
    _attrMap: Any
    text: str
    def __init__(self) -> None: ...

NoneOrInstanceOfNA_Label: Any

class RedNegativeChanger(CustomDrawChanger):
    fillColor: Any
    def __init__(self, fillColor=...) -> None: ...
    def _changer(self, obj): ...

class XLabel(Label):
    _attrMap: Any
    ddfKlass: Any
    ddf: Any
    def __init__(self, *args, **kwds) -> None: ...
    _flowableClass: Any
    _ddf: Any
    def __init__(self, *args, **kwds) -> None: ...
    _lineWidths: Any
    _leading: Any
    _obj: Any
    _width: Any
    def computeSize(self) -> None: ...
    _text: Any
    def _rawDraw(self): ...
