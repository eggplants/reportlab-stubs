from typing import Any

from .flowables import Flowable, _Container, _FindSplitterMixin

class MultiCol(_Container, _FindSplitterMixin, Flowable):
    contents: Any
    widths: Any
    minHeightNeeded: Any
    _spaceBefore: Any
    _spaceAfter: Any
    _naW: Any
    def __init__(
        self,
        contents,
        widths,
        minHeightNeeded: int = ...,
        spaceBefore: Any | None = ...,
        spaceAfter: Any | None = ...,
    ) -> None: ...
    _nW: Any
    def nWidths(self, aW): ...
    width: Any
    height: Any
    def wrap(self, aW, aH): ...
    def split(self, aW, aH): ...
    def getSpaceAfter(self): ...
    def getSpaceBefore(self): ...
    def drawOn(self, canv, x, y, _sW: int = ...) -> None: ...
