from collections.abc import Generator
from typing import Any

from reportlab.lib.utils import strTypes as strTypes
from reportlab.pdfbase.pdfdoc import PDFObject as PDFObject
from reportlab.pdfbase.pdfdoc import format as format
from reportlab.pdfbase.pdfdoc import pdfdocEnc as pdfdocEnc

__doc__: str

def _patternSequenceCheck(pattern_sequence) -> None: ...

class PDFPattern(PDFObject):
    __RefOnly__: int
    pattern: Any
    arguments: Any
    def __init__(self, pattern_sequence, **keywordargs) -> None: ...
    def __setitem__(self, item, value) -> None: ...
    def __getitem__(self, item): ...
    def eval(self, L) -> Generator[Any, None, None]: ...
    __document: Any
    def format(self, document): ...
    def clone(self): ...

class PDFPatternIf:
    cond: Any
    thenPart: Any
    elsePart: Any
    def __init__(self, cond, thenPart=..., elsePart=...) -> None: ...
