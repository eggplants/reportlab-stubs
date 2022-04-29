from typing import Any

from reportlab.lib.rl_accel import escapePDF as escapePDF
from reportlab.lib.utils import isBytes as isBytes
from reportlab.lib.utils import isSeq as isSeq
from reportlab.pdfbase import pdfdoc as pdfdoc
from reportlab.pdfbase import pdfmetrics as pdfmetrics
from reportlab.pdfbase._cidfontdata import CIDFontInfo as CIDFontInfo
from reportlab.pdfbase._cidfontdata import allowedEncodings as allowedEncodings
from reportlab.pdfbase._cidfontdata import allowedTypeFaces as allowedTypeFaces
from reportlab.pdfbase._cidfontdata import (
    defaultUnicodeEncodings as defaultUnicodeEncodings,
)
from reportlab.pdfbase._cidfontdata import widthsByUnichar as widthsByUnichar
from reportlab.pdfgen.canvas import Canvas as Canvas
from reportlab.rl_config import CMapSearchPath as CMapSearchPath

__version__: str
__doc__: str
DISABLE_CMAP: bool

def findCMapFile(name): ...
def structToPDF(structure): ...

class CIDEncoding(pdfmetrics.Encoding):
    name: Any
    _mapFileHash: Any
    _codeSpaceRanges: Any
    _notDefRanges: Any
    _cmap: Any
    source: Any
    def __init__(self, name, useCache: int = ...) -> None: ...
    def _hash(self, text): ...
    def parseCMAPFile(self, name) -> None: ...
    def translate(self, text): ...
    def fastSave(self, directory) -> None: ...
    def fastLoad(self, directory) -> None: ...
    def getData(self): ...

class CIDTypeFace(pdfmetrics.TypeFace):
    def __init__(self, name) -> None: ...
    ascent: Any
    descent: Any
    _defaultWidth: Any
    _explicitWidths: Any
    def _extractDictInfo(self, name) -> None: ...
    def _expandWidths(self, compactWidthArray): ...
    def getCharWidth(self, characterId): ...

class CIDFont(pdfmetrics.Font):
    _multiByte: int
    faceName: Any
    face: Any
    encodingName: Any
    encoding: Any
    fontName: Any
    name: Any
    isVertical: Any
    substitutionFonts: Any
    def __init__(self, face, encoding) -> None: ...
    def formatForPdf(self, text): ...
    def stringWidth(self, text, size, encoding: Any | None = ...): ...
    def addObjects(self, doc) -> None: ...

class UnicodeCIDFont(CIDFont):
    language: Any
    name: Any
    vertical: Any
    isHalfWidth: Any
    unicodeWidths: Any
    def __init__(
        self, face, isVertical: bool = ..., isHalfWidth: bool = ...
    ) -> None: ...
    def formatForPdf(self, text): ...
    def stringWidth(self, text, size, encoding: Any | None = ...): ...

def precalculate(cmapdir) -> None: ...
def test() -> None: ...
