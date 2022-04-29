from typing import Any

from reportlab.graphics.charts.areas import PlotArea

class _BarcodeWidget(PlotArea):
    _attrMap: Any
    textColor: Any
    barFillColor: Any
    barStrokeColor: Any
    barStrokeWidth: int
    _BCC: Any
    x: int
    def __init__(self, _value: str = ..., **kw) -> None: ...
    def rect(self, x, y, w, h, **kw) -> None: ...
    canv: Any
    _Gadd: Any
    def draw(self): ...
    def annotate(self, x, y, text, fontName, fontSize, anchor: str = ...) -> None: ...

BarcodeI2of5: Any
BarcodeCode128: Any
BarcodeStandard93: Any
BarcodeExtended93: Any
BarcodeStandard39: Any
BarcodeExtended39: Any
BarcodeMSI: Any
BarcodeCodabar: Any
BarcodeCode11: Any
BarcodeFIM: Any
BarcodePOSTNET: Any
BarcodeUSPS_4State: Any
