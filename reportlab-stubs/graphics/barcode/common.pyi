from typing import Any

from reportlab.lib.units import inch as inch
from reportlab.platypus.flowables import Flowable as Flowable

class Barcode(Flowable):
    fontName: str
    fontSize: int
    humanReadable: int
    def _humanText(self): ...
    value: Any
    gap: Any
    def __init__(self, value: str = ..., **kwd) -> None: ...
    def _calculate(self) -> None: ...
    def _setKeywords(self, **kwd) -> None: ...
    valid: int
    validated: Any
    def validate(self) -> None: ...
    encoded: Any
    def encode(self) -> None: ...
    decomposed: Any
    def decompose(self) -> None: ...
    barHeight: Any
    _height: Any
    _width: Any
    def computeSize(self, *args) -> None: ...
    def width(self): ...
    width: Any
    def height(self): ...
    height: Any
    def draw(self) -> None: ...
    def drawHumanReadable(self) -> None: ...
    def rect(self, x, y, w, h) -> None: ...
    def annotate(self, x, y, text, fontName, fontSize, anchor: str = ...) -> None: ...
    def _checkVal(self, name, v, allowed): ...

class MultiWidthBarcode(Barcode):
    barHeight: Any
    _height: Any
    _width: Any
    def computeSize(self, *args) -> None: ...
    def draw(self) -> None: ...

class I2of5(Barcode):
    patterns: Any
    barHeight: Any
    barWidth: Any
    ratio: float
    checksum: int
    bearers: float
    quiet: int
    lquiet: Any
    rquiet: Any
    stop: int
    def __init__(self, value: str = ..., **args) -> None: ...
    valid: int
    validated: Any
    def validate(self): ...
    encoded: Any
    def encode(self) -> None: ...
    decomposed: Any
    def decompose(self): ...

class MSI(Barcode):
    patterns: Any
    stop: int
    barHeight: Any
    barWidth: Any
    ratio: float
    checksum: int
    bearers: float
    quiet: int
    lquiet: Any
    rquiet: Any
    def __init__(self, value: str = ..., **args) -> None: ...
    valid: int
    validated: Any
    def validate(self): ...
    encoded: Any
    def encode(self) -> None: ...
    decomposed: Any
    def decompose(self): ...

class Codabar(Barcode):
    patterns: Any
    values: Any
    chars: Any
    stop: int
    barHeight: Any
    barWidth: Any
    ratio: float
    checksum: int
    bearers: float
    quiet: int
    lquiet: Any
    rquiet: Any
    def __init__(self, value: str = ..., **args) -> None: ...
    valid: int
    Valid: int
    validated: Any
    def validate(self): ...
    encoded: Any
    def encode(self) -> None: ...
    decomposed: Any
    def decompose(self): ...

class Code11(Barcode):
    chars: str
    patterns: Any
    values: Any
    stop: int
    barHeight: Any
    barWidth: Any
    ratio: float
    checksum: int
    bearers: float
    quiet: int
    lquiet: Any
    rquiet: Any
    def __init__(self, value: str = ..., **args) -> None: ...
    valid: int
    Valid: int
    validated: Any
    def validate(self): ...
    def _addCSD(self, s, m): ...
    encoded: Any
    def encode(self) -> None: ...
    decomposed: Any
    def decompose(self): ...
    def _humanText(self): ...
