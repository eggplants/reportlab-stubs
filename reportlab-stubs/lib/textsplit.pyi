from typing import Any

from reportlab.lib.utils import isUnicode as isUnicode
from reportlab.pdfbase.pdfmetrics import stringWidth as stringWidth
from reportlab.rl_config import _FUZZ as _FUZZ

__version__: str
CANNOT_START_LINE: Any
ALL_CANNOT_START: Any
CANNOT_END_LINE: Any
ALL_CANNOT_END: Any

def is_multi_byte(ch): ...
def getCharWidths(word, fontName, fontSize): ...
def wordSplit(word, maxWidths, fontName, fontSize, encoding: str = ...): ...
def dumbSplit(word, widths, maxWidths): ...
def kinsokuShoriSplit(word, widths, availWidth) -> None: ...

rx: Any

def cjkwrap(text, width, encoding: str = ...): ...
