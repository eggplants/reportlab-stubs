from typing import Any, NamedTuple

from reportlab import rl_config as rl_config
from reportlab.lib.rl_accel import add32 as add32
from reportlab.lib.rl_accel import calcChecksum as calcChecksum
from reportlab.lib.rl_accel import hex32 as hex32
from reportlab.lib.rl_accel import instanceStringWidthTTF as instanceStringWidthTTF
from reportlab.lib.utils import bytestr as bytestr
from reportlab.lib.utils import char2int as char2int
from reportlab.lib.utils import isBytes as isBytes
from reportlab.lib.utils import isStr as isStr
from reportlab.lib.utils import isUnicode as isUnicode
from reportlab.pdfbase import pdfdoc as pdfdoc
from reportlab.pdfbase import pdfmetrics as pdfmetrics
from reportlab.rl_config import register_reset as register_reset

__version__: str
__doc__: str

class TTFError(pdfdoc.PDFError): ...

def SUBSETN(n, table=...): ...
def makeToUnicodeCMap(fontname, subset): ...
def splice(stream, offset, value): ...
def _set_ushort(stream, offset, value): ...

GF_ARG_1_AND_2_ARE_WORDS: Any
GF_ARGS_ARE_XY_VALUES: Any
GF_ROUND_XY_TO_GRID: Any
GF_WE_HAVE_A_SCALE: Any
GF_RESERVED: Any
GF_MORE_COMPONENTS: Any
GF_WE_HAVE_AN_X_AND_Y_SCALE: Any
GF_WE_HAVE_A_TWO_BY_TWO: Any
GF_WE_HAVE_INSTRUCTIONS: Any
GF_USE_MY_METRICS: Any
GF_OVERLAP_COMPOUND: Any
GF_SCALED_COMPONENT_OFFSET: Any
GF_UNSCALED_COMPONENT_OFFSET: Any
_cached_ttf_dirs: Any

def _ttf_dirs(*roots): ...
def TTFOpenFile(fn): ...

class TTFontParser:
    ttfVersions: Any
    ttcVersions: Any
    fileKind: str
    validate: Any
    subfontNameX: bytes
    def __init__(self, file, validate: int = ..., subfontIndex: int = ...) -> None: ...
    ttcVersion: Any
    numSubfonts: Any
    subfontOffsets: Any
    def readTTCHeader(self) -> None: ...
    def getSubfont(self, subfontIndex) -> None: ...
    numTables: Any
    searchRange: Any
    entrySelector: Any
    rangeShift: Any
    table: Any
    tables: Any
    def readTableDirectory(self) -> None: ...
    version: Any
    def readHeader(self): ...
    filename: Any
    _ttf_data: Any
    _pos: int
    def readFile(self, f) -> None: ...
    def checksumTables(self) -> None: ...
    def checksumFile(self) -> None: ...
    def get_table_pos(self, tag): ...
    def seek(self, pos) -> None: ...
    def skip(self, delta) -> None: ...
    def seek_table(self, tag, offset_in_table: int = ...): ...
    def read_tag(self): ...
    def get_chunk(self, pos, length): ...
    def read_uint8(self): ...
    def read_ushort(self): ...
    def read_ulong(self): ...
    def read_short(self): ...
    def get_ushort(self, pos): ...
    def get_ulong(self, pos): ...
    def get_table(self, tag): ...

class TTFontMaker:
    tables: Any
    def __init__(self) -> None: ...
    def add(self, tag, data) -> None: ...
    def makeStream(self): ...

class CMapFmt2SubHeader(NamedTuple):
    firstCode: Any
    entryCount: Any
    idDelta: Any
    idRangeOffset: Any

class TTFNameBytes(bytes):
    ustr: Any
    def __new__(cls, b, enc: str = ...): ...

class TTFontFile(TTFontParser):
    _agfnc: int
    _agfnm: Any
    def __init__(
        self, file, charInfo: int = ..., validate: int = ..., subfontIndex: int = ...
    ) -> None: ...
    _pos: Any
    name: Any
    familyName: Any
    styleName: Any
    fullName: Any
    uniqueFontID: Any
    fontRevision: Any
    unitsPerEm: Any
    bbox: Any
    ascent: Any
    descent: Any
    capHeight: Any
    stemV: Any
    italicAngle: Any
    underlinePosition: Any
    underlineThickness: Any
    flags: Any
    numGlyphs: Any
    _full_font: bool
    charToGlyph: Any
    defaultWidth: Any
    charWidths: Any
    hmetrics: Any
    glyphPos: Any
    def extractInfo(self, charInfo: int = ...): ...
    def makeSubset(self, subset): ...

FF_FIXED: Any
FF_SERIF: Any
FF_SYMBOLIC: Any
FF_SCRIPT: Any
FF_NONSYMBOLIC: Any
FF_ITALIC: Any
FF_ALLCAP: Any
FF_SMALLCAP: Any
FF_FORCEBOLD: Any

class TTFontFace(TTFontFile, pdfmetrics.TypeFace):
    def __init__(
        self, filename, validate: int = ..., subfontIndex: int = ...
    ) -> None: ...
    def getCharWidth(self, code): ...
    def addSubsetObjects(self, doc, fontname, subset): ...

class TTEncoding:
    name: str
    def __init__(self) -> None: ...

class TTFont:
    class State:
        namePrefix: str
        nextCode: int
        internalName: Any
        frozen: int
        subsets: Any
        def __init__(
            self, asciiReadable: Any | None = ..., ttf: Any | None = ...
        ) -> None: ...
    _multiByte: int
    _dynamicFont: int
    fontName: Any
    face: Any
    encoding: Any
    state: Any
    _asciiReadable: Any
    def __init__(
        self,
        name,
        filename,
        validate: int = ...,
        subfontIndex: int = ...,
        asciiReadable: Any | None = ...,
    ) -> None: ...
    def stringWidth(self, text, size, encoding: str = ...): ...
    def _assignState(
        self, doc, asciiReadable: Any | None = ..., namePrefix: Any | None = ...
    ): ...
    def splitString(self, text, doc, encoding: str = ...): ...
    def getSubsetInternalName(self, subset, doc): ...
    def addObjects(self, doc) -> None: ...

def _reset() -> None: ...
