from typing import Any

from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.shapes import String as String
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.lib import colors as colors
from reportlab.lib.utils import int2Byte as int2Byte
from reportlab.pdfbase import cidfonts as cidfonts
from reportlab.pdfbase import pdfmetrics as pdfmetrics
from reportlab.pdfgen.canvas import Canvas as Canvas
from reportlab.platypus import Flowable as Flowable

__version__: str
__doc__: str
adobe2codec: Any

class CodeChartBase(Flowable):
    rows: Any
    width: Any
    height: Any
    ylist: Any
    xlist: Any
    def calcLayout(self) -> None: ...
    def formatByte(self, byt): ...
    def drawChars(self, charList) -> None: ...
    def drawLabels(self, topLeft: str = ...) -> None: ...

class SingleByteEncodingChart(CodeChartBase):
    codePoints: int
    faceName: Any
    encodingName: Any
    fontName: Any
    charsPerRow: Any
    boxSize: Any
    hex: Any
    rowLabels: Any
    def __init__(
        self,
        faceName: str = ...,
        encodingName: str = ...,
        charsPerRow: int = ...,
        boxSize: int = ...,
        hex: int = ...,
    ) -> None: ...
    def draw(self): ...

class KutenRowCodeChart(CodeChartBase):
    row: Any
    codePoints: int
    boxSize: int
    charsPerRow: int
    rows: int
    rowLabels: Any
    hex: int
    faceName: Any
    encodingName: Any
    fontName: Any
    def __init__(self, row, faceName, encodingName) -> None: ...
    def makeRow(self, row): ...
    def draw(self) -> None: ...

class Big5CodeChart(CodeChartBase):
    row: Any
    codePoints: int
    boxSize: int
    charsPerRow: int
    rows: int
    hex: int
    faceName: Any
    encodingName: Any
    rowLabels: Any
    fontName: Any
    def __init__(self, row, faceName, encodingName) -> None: ...
    def makeRow(self, row): ...
    def draw(self) -> None: ...

def hBoxText(msg, canvas, x, y, fontName) -> None: ...

class CodeWidget(Widget):
    x: int
    y: int
    width: int
    height: int
    def __init__(self) -> None: ...
    def draw(self): ...

def test() -> None: ...
