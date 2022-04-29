from typing import Any

from reportlab.graphics.barcode.common import MultiWidthBarcode as MultiWidthBarcode
from reportlab.lib.units import inch as inch
from reportlab.lib.utils import asNative as asNative

_patterns: Any
starta: Any
startb: Any
startc: Any
stop: Any
seta: Any
setb: Any
setc: Any
setmap: Any
cStarts: Any
tos: Any

class Code128(MultiWidthBarcode):
    barWidth: Any
    lquiet: Any
    rquiet: Any
    quiet: int
    barHeight: Any
    def __init__(self, value: str = ..., **args) -> None: ...
    valid: int
    validated: Any
    def validate(self): ...
    def _try_TO_C(self, l): ...
    encoded: Any
    def encode(self): ...
    decomposed: Any
    def decompose(self): ...
    def _humanText(self): ...

class Code128Auto(Code128):
    encoded: Any
    def encode(self): ...
