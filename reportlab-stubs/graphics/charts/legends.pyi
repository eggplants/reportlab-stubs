from typing import Any

from reportlab.graphics.shapes import STATE_DEFAULTS as STATE_DEFAULTS
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Line as Line
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.shapes import String as String
from reportlab.graphics.shapes import _baseGFontName as _baseGFontName
from reportlab.graphics.widgetbase import PropHolder as PropHolder
from reportlab.graphics.widgetbase import (
    TypedPropertyCollection as TypedPropertyCollection,
)
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.graphics.widgets.markers import isSymbol as isSymbol
from reportlab.graphics.widgets.markers import uSymbol2Symbol as uSymbol2Symbol
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import *
from reportlab.lib.utils import asNative as asNative
from reportlab.lib.utils import find_locals as find_locals
from reportlab.lib.utils import isSeq as isSeq
from reportlab.lib.utils import isStr as isStr
from reportlab.lib.validators import Auto as Auto
from reportlab.lib.validators import AutoOr as AutoOr
from reportlab.lib.validators import EitherOr as EitherOr
from reportlab.lib.validators import NoneOr as NoneOr
from reportlab.lib.validators import OneOf as OneOf
from reportlab.lib.validators import SequenceOf as SequenceOf
from reportlab.lib.validators import isAuto as isAuto
from reportlab.lib.validators import isBoolean as isBoolean
from reportlab.lib.validators import isBoxAnchor as isBoxAnchor
from reportlab.lib.validators import isColorOrNone as isColorOrNone
from reportlab.lib.validators import isInstanceOf as isInstanceOf
from reportlab.lib.validators import isListOfNumbersOrNone as isListOfNumbersOrNone
from reportlab.lib.validators import isNumber as isNumber
from reportlab.lib.validators import isNumberOrNone as isNumberOrNone
from reportlab.lib.validators import isString as isString
from reportlab.pdfbase.pdfmetrics import getFont as getFont
from reportlab.pdfbase.pdfmetrics import stringWidth as stringWidth

__version__: str
__doc__: str

def _transMax(n, A): ...
def _objStr(s): ...
def _getStr(s): ...
def _getLines(s): ...
def _getLineCount(s): ...
def _getWidths(i, s, fontName, fontSize, subCols): ...

class SubColProperty(PropHolder):
    dividerLines: int
    _attrMap: Any

class LegendCallout:
    def _legendValues(legend, *args): ...
    _legendValues: Any
    def _selfOrLegendValues(self, legend, *args): ...
    def __call__(self, legend, g, thisx, y, colName) -> None: ...

class LegendSwatchCallout(LegendCallout):
    def __call__(self, legend, g, thisx, y, i, colName, swatch) -> None: ...

class LegendColEndCallout(LegendCallout):
    def __call__(self, legend, g, x, xt, y, width, lWidth) -> None: ...

class Legend(Widget):
    _attrMap: Any
    x: int
    y: int
    alignment: str
    deltax: int
    deltay: int
    autoXPadding: int
    autoYPadding: int
    dx: int
    dy: int
    swdx: int
    swdy: int
    dxTextSpace: int
    columnMaximum: int
    colorNamePairs: Any
    fontName: Any
    fontSize: Any
    leading: Any
    fillColor: Any
    strokeColor: Any
    strokeWidth: Any
    swatchMarker: Any
    boxAnchor: str
    yGap: int
    variColumn: int
    dividerLines: int
    dividerWidth: float
    dividerDashArray: Any
    dividerColor: Any
    dividerOffsX: Any
    dividerOffsY: int
    colEndCallout: Any
    def __init__(self) -> None: ...
    def _init_subCols(self) -> None: ...
    def _getChartStyleName(self, chart): ...
    def _getChartStyle(self, chart): ...
    def _getTexts(self, colorNamePairs): ...
    def _calculateMaxBoundaries(self, colorNamePairs): ...
    def _calcHeight(self): ...
    def _defaultSwatch(self, x, this, dx, dy, fillColor, strokeWidth, strokeColor): ...
    def draw(self): ...
    def demo(self): ...

class TotalAnnotator(LegendColEndCallout):
    lText: Any
    rText: Any
    fontName: Any
    fontSize: Any
    fillColor: Any
    dy: Any
    dx: Any
    dly: Any
    dlx: Any
    strokeWidth: Any
    strokeColor: Any
    strokeDashArray: Any
    def __init__(
        self,
        lText: str = ...,
        rText: str = ...,
        fontName=...,
        fontSize: int = ...,
        fillColor=...,
        strokeWidth: float = ...,
        strokeColor=...,
        strokeDashArray: Any | None = ...,
        dx: int = ...,
        dy: int = ...,
        dly: int = ...,
        dlx=...,
    ) -> None: ...
    def __call__(self, legend, g, x, xt, y, width, lWidth) -> None: ...

class LineSwatch(Widget):
    _attrMap: Any
    x: int
    y: int
    width: int
    height: int
    strokeColor: Any
    strokeDashArray: Any
    def __init__(self) -> None: ...
    def draw(self): ...

class LineLegend(Legend):
    dx: int
    dy: int
    def __init__(self) -> None: ...
    def _defaultSwatch(self, x, this, dx, dy, fillColor, strokeWidth, strokeColor): ...
