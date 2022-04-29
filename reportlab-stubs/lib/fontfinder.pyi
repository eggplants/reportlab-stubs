from typing import Any

from reportlab.lib.utils import asBytes as asBytes
from reportlab.lib.utils import rl_getmtime as rl_getmtime
from reportlab.lib.utils import rl_isdir as rl_isdir
from reportlab.lib.utils import rl_isfile as rl_isfile
from reportlab.lib.utils import rl_listdir as rl_listdir

__version__: str
__doc__: str

def asNative(s): ...

EXTENSIONS: Any
FF_FIXED: Any
FF_SERIF: Any
FF_SYMBOLIC: Any
FF_SCRIPT: Any
FF_NONSYMBOLIC: Any
FF_ITALIC: Any
FF_ALLCAP: Any
FF_SMALLCAP: Any
FF_FORCEBOLD: Any

class FontDescriptor:
    name: Any
    fullName: Any
    familyName: Any
    styleName: Any
    isBold: bool
    isItalic: bool
    isFixedPitch: bool
    isSymbolic: bool
    typeCode: Any
    fileName: Any
    metricsFileName: Any
    timeModified: int
    def __init__(self) -> None: ...
    def __repr__(self): ...
    def getTag(self): ...

class FontFinder:
    useCache: Any
    validate: Any
    _fsEncoding: Any
    _dirs: Any
    _recur: Any
    _fonts: Any
    _skippedFiles: Any
    _badFiles: Any
    _fontsByName: Any
    _fontsByFamily: Any
    _fontsByFamilyBoldItalic: Any
    verbose: Any
    def __init__(
        self,
        dirs=...,
        useCache: bool = ...,
        validate: bool = ...,
        recur: bool = ...,
        fsEncoding: Any | None = ...,
        verbose: int = ...,
    ) -> None: ...
    def addDirectory(self, dirName, recur: Any | None = ...) -> None: ...
    def addDirectories(self, dirNames, recur: Any | None = ...) -> None: ...
    def getFamilyNames(self): ...
    def getFontsInFamily(self, familyName): ...
    def getFamilyXmlReport(self): ...
    def getFontsWithAttributes(self, **kwds): ...
    def getFont(self, familyName, bold: bool = ..., italic: bool = ...): ...
    def _getCacheFileName(self): ...
    def save(self, fileName) -> None: ...
    def load(self, fileName) -> None: ...
    def search(self) -> None: ...

def test() -> None: ...
