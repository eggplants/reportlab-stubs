from typing import Any

from reportlab.graphics.barcode.common import Barcode as Barcode
from reportlab.lib.units import inch as inch
from reportlab.lib.utils import asNative as asNative

_fim_patterns: Any
_postnet_patterns: Any

class FIM(Barcode):
    barWidth: Any
    spaceWidth: Any
    barHeight: Any
    rquiet: Any
    lquiet: Any
    quiet: int
    def __init__(self, value: str = ..., **args) -> None: ...
    valid: int
    validated: str
    def validate(self): ...
    decomposed: str
    def decompose(self): ...
    _width: Any
    _height: Any
    def computeSize(self) -> None: ...
    def draw(self) -> None: ...
    def _humanText(self): ...

class POSTNET(Barcode):
    quiet: int
    shortHeight: Any
    barHeight: Any
    barWidth: Any
    spaceWidth: Any
    def __init__(self, value: str = ..., **args) -> None: ...
    validated: str
    valid: int
    def validate(self): ...
    encoded: str
    def encode(self): ...
    decomposed: str
    def decompose(self): ...
    _width: Any
    _height: Any
    def computeSize(self) -> None: ...
    def draw(self) -> None: ...
    def _humanText(self): ...
