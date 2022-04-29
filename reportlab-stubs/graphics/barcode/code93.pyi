from typing import Any

from reportlab.graphics.barcode.common import MultiWidthBarcode as MultiWidthBarcode
from reportlab.lib.units import inch as inch
from reportlab.lib.utils import asNative as asNative

_patterns: Any
_charsbyval: Any
_extended: Any

def _encode93(str): ...

class _Code93Base(MultiWidthBarcode):
    barWidth: Any
    lquiet: Any
    rquiet: Any
    quiet: int
    barHeight: Any
    stop: int
    def __init__(self, value: str = ..., **args) -> None: ...
    decomposed: Any
    def decompose(self): ...

class Standard93(_Code93Base):
    valid: int
    validated: Any
    def validate(self): ...
    encoded: Any
    def encode(self): ...

class Extended93(_Code93Base):
    valid: int
    validated: Any
    def validate(self): ...
    encoded: str
    def encode(self): ...
    def _humanText(self): ...
