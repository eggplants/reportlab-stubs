from typing import Any

from reportlab.graphics.barcode.common import Barcode as Barcode
from reportlab.lib.units import inch as inch
from reportlab.lib.utils import asNative as asNative

_patterns: Any
_stdchrs: Any
_extended: Any
_extchrs: Any

def _encode39(value, cksum, stop): ...

class _Code39Base(Barcode):
    barWidth: Any
    lquiet: Any
    rquiet: Any
    quiet: int
    gap: Any
    barHeight: Any
    ratio: float
    checksum: int
    bearers: float
    stop: int
    def __init__(self, value: str = ..., **args) -> None: ...
    decomposed: Any
    def decompose(self): ...
    def _humanText(self): ...

class Standard39(_Code39Base):
    valid: int
    validated: Any
    def validate(self): ...
    encoded: Any
    def encode(self): ...

class Extended39(_Code39Base):
    valid: int
    validated: Any
    def validate(self): ...
    encoded: str
    def encode(self): ...
