from typing import Any

from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import PolyLine as PolyLine
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.shapes import String as String
from reportlab.graphics.shapes import definePath as definePath
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.lib.attrmap import *
from reportlab.lib.colors import Color as Color
from reportlab.lib.colors import ReportLabBlue as ReportLabBlue
from reportlab.lib.colors import black as black
from reportlab.lib.colors import white as white
from reportlab.lib.formatters import DecimalFormatter as DecimalFormatter
from reportlab.lib.units import cm as cm
from reportlab.lib.units import inch as inch
from reportlab.lib.validators import *
from reportlab.pdfbase.pdfmetrics import stringWidth as stringWidth

__version__: str
__doc__: str

class RL_CorpLogo(Widget):
    _attrMap: Any
    fillColor: Any
    strokeColor: Any
    strokeWidth: float
    background: Any
    border: Any
    borderWidth: int
    shadow: float
    height: int
    width: int
    x: int
    skewX: int
    _dy: float
    showPage: int
    oColors: Any
    pageColors: Any
    prec: Any
    def __init__(self) -> None: ...
    def demo(self): ...
    def _paintLogo(
        self,
        g,
        dx: int = ...,
        dy: int = ...,
        strokeColor: Any | None = ...,
        strokeWidth: float = ...,
        fillColor=...,
        _ocolors: Any | None = ...,
        _pagecolors: Any | None = ...,
    ) -> None: ...
    @staticmethod
    def applyPrec(P, prec): ...
    def draw(self): ...

class RL_CorpLogoReversed(RL_CorpLogo):
    background: Any
    fillColor: Any
    def __init__(self) -> None: ...

class RL_CorpLogoThin(Widget):
    _attrMap: Any
    _h: float
    _w: float
    _text: str
    _fontName: str
    _fontSize: int
    fillColor: Any
    strokeColor: Any
    x: int
    y: int
    height: Any
    width: Any
    def __init__(self) -> None: ...
    def demo(self): ...
    def _getText(self, x: int = ..., y: int = ..., color: Any | None = ...): ...
    def _sw(self, f: Any | None = ..., l: Any | None = ...): ...
    def _addPage(
        self,
        g,
        strokeWidth: int = ...,
        color: Any | None = ...,
        dx: int = ...,
        dy: int = ...,
    ) -> None: ...
    def draw(self): ...

class ReportLabLogo:
    origin: Any
    dimensions: Any
    powered_by: Any
    def __init__(
        self,
        atx: int = ...,
        aty: int = ...,
        width=...,
        height=...,
        powered_by: int = ...,
    ) -> None: ...
    def draw(self, canvas) -> None: ...

class RL_BusinessCard(Widget):
    _attrMap: Any
    _h: Any
    _w: Any
    _fontName: str
    _strapline: str
    fillColor: Any
    strokeColor: Any
    altStrokeColor: Any
    x: int
    y: int
    height: Any
    width: Any
    borderWidth: Any
    bleed: Any
    cropMarks: int
    border: int
    name: str
    position: str
    telephone: str
    mobile: str
    fax: str
    email: str
    web: str
    rh_blurb_top: Any
    def __init__(self) -> None: ...
    def demo(self): ...
    def draw(self): ...

def test(formats=...) -> None: ...
