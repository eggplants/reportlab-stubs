from typing import Any

from reportlab.graphics.shapes import Rect
from reportlab.graphics.widgetbase import Widget
from reportlab.lib.validators import Validator
from reportlab.platypus.flowables import Flowable

class isLevel(Validator):
    def test(self, x): ...

class isUnicodeOrQRList(Validator):
    def _test(self, x): ...
    def test(self, x): ...
    def normalize(self, x): ...

class SRect(Rect):
    def __init__(self, x, y, width, height, fillColor=...) -> None: ...

class QrCodeWidget(Widget):
    codeName: str
    _attrMap: Any
    x: int
    y: int
    barFillColor: Any
    barStrokeColor: Any
    barStrokeWidth: int
    barHeight: Any
    barWidth: Any
    barBorder: int
    barLevel: str
    qrVersion: Any
    value: Any
    def __init__(self, value: str = ..., **kw) -> None: ...
    def addData(self, value) -> None: ...
    def draw(self): ...

class QrCode(Flowable):
    height: Any
    width: Any
    qrBorder: int
    qrLevel: str
    qrVersion: Any
    value: Any
    qr: Any
    def __init__(self, value: Any | None = ..., **kw) -> None: ...
    def addData(self, value) -> None: ...
    def draw(self) -> None: ...
    def rect(self, x, y, w, h) -> None: ...

# Names in __all__ with no definition:
#   C
#   Q
#   W
#   d
#   d
#   e
#   e
#   g
#   i
#   o
#   r
#   t
