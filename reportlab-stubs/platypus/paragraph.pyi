from typing import Any

from reportlab.lib.abag import ABag
from reportlab.platypus.flowables import Flowable

class ParaLines(ABag): ...
class FragLine(ABag): ...

def cleanBlockQuotedText(text, joiner: str = ...): ...

class _HSFrag(list): ...
class _InjectedFrag(list): ...
class _SplitFrag(list): ...
class _SplitFragH(_SplitFrag): ...
class _SplitFragHY(_SplitFragH): ...
class _SplitFragHS(_SplitFrag, _HSFrag): ...
class _SplitFragLL(_SplitFragHS): ...

class _SHYIndexedStr(str):
    _shyIndices: Any
    def __new__(cls, u, X: Any | None = ...): ...

class _SHYWord(list):
    _fsww: int
    def shyphenate(self, newWidth, maxWidth): ...

class _SplitFragSHY(_SHYWord, _SplitFragHY): ...
class _SHYWordHS(_SHYWord, _SplitFragHS): ...
class _SplitWord(str): ...
class _SplitWordEnd(_SplitWord): ...
class _SplitWordH(_SplitWord): ...
class _SplitWordHY(_SplitWordH): ...
class _SplitWordLL(str): ...

class _SHYStr(str):
    __sp__: Any
    def __new__(cls, s): ...
    _fsww: int
    def __shysplit__(
        self, fontName, fontSize, baseWidth, limWidth, encoding: str = ...
    ): ...

class _SHYSplitHY(_SHYStr, _SplitWordHY): ...
class _SHYSplit(_SHYStr, _SplitWord): ...

class cjkU(str):
    _frag: Any
    _width: Any
    def __new__(cls, value, frag, encoding): ...
    frag: Any
    width: Any

class Paragraph(Flowable):
    caseSensitive: Any
    encoding: Any
    def __init__(
        self,
        text,
        style: Any | None = ...,
        bulletText: Any | None = ...,
        frags: Any | None = ...,
        caseSensitive: int = ...,
        encoding: str = ...,
    ) -> None: ...
    def __repr__(self): ...
    text: Any
    frags: Any
    style: Any
    bulletText: Any
    debug: int
    def _setup(self, text, style, bulletText, frags, cleaner) -> None: ...
    width: Any
    _wrapWidths: Any
    blPara: Any
    height: Any
    def wrap(self, availWidth, availHeight): ...
    def minWidth(self): ...
    def _split_blParaProcessed(self, blPara, start, stop): ...
    def _get_split_blParaFunc(self): ...
    def split(self, availWidth, availHeight): ...
    def draw(self) -> None: ...
    _width_max: int
    _splitLongWordCount: int
    def breakLines(self, width): ...
    def breakLinesCJK(self, maxWidths): ...
    def beginText(self, x, y): ...
    def drawPara(self, debug: int = ...) -> None: ...
    def getPlainText(self, identify: Any | None = ...): ...
    def getActualLineWidths0(self): ...
    @staticmethod
    def dumpFrags(frags, indent: int = ..., full: bool = ...): ...
