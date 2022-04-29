from typing import Any

from reportlab.graphics.charts.areas import PlotArea
from reportlab.lib.attrmap import *

class Ean13BarcodeWidget(PlotArea):
    codeName: str
    _attrMap: Any
    _digits: int
    _start_right: int
    _nbars: int
    barHeight: Any
    barWidth: Any
    humanReadable: int
    _0csw: int
    _1csw: int
    _left: Any
    _right: Any
    quiet: int
    rquiet: Any
    lquiet: Any
    _tail: str
    _sep: str
    _lhconvert: Any
    fontSize: int
    fontName: str
    textColor: Any
    barFillColor: Any
    barStrokeColor: Any
    barStrokeWidth: int
    x: int
    y: int
    value: Any
    def __init__(self, value: str = ..., **kw) -> None: ...
    width: Any
    def wrap(self, aW, aH): ...
    def _encode_left(self, s, a) -> None: ...
    def _short_bar(self, i): ...
    def _calc_quiet(self, v): ...
    _lquiet: Any
    def draw(self): ...
    def _add_human_readable(self, s, gAdd) -> None: ...
    def _checkdigit(cls, num): ...
    _checkdigit: Any

class Ean8BarcodeWidget(Ean13BarcodeWidget):
    codeName: str
    _attrMap: Any
    _start_right: int
    _nbars: int
    _digits: int
    _0csw: int
    _1csw: int
    def _encode_left(self, s, a) -> None: ...
    def _short_bar(self, i): ...
    def _add_human_readable(self, s, gAdd) -> None: ...

class UPCA(Ean13BarcodeWidget):
    codeName: str
    _attrMap: Any
    _start_right: int
    _digits: int
    _0csw: int
    _1csw: int
    _nbars: Any
    def _encode_left(self, s, a) -> None: ...
    def _short_bar(self, i): ...
    def _add_human_readable(self, s, gAdd) -> None: ...

class Ean5BarcodeWidget(Ean13BarcodeWidget):
    codeName: str
    _attrMap: Any
    _nbars: int
    _digits: int
    _sep: str
    _tail: str
    _0csw: int
    _1csw: int
    _lhconvert: Any
    def _checkdigit(cls, num): ...
    def _encode_left(self, s, a) -> None: ...
    def _short_bar(self, i): ...
    def _add_human_readable(self, s, gAdd) -> None: ...
    _lquiet: Any
    def draw(self): ...

class ISBNBarcodeWidget(Ean13BarcodeWidget):
    codeName: str
    _attrMap: Any
    def draw(self): ...
    def _add_human_readable(self, s, gAdd) -> None: ...

# Names in __all__ with no definition:
#   isEanString
