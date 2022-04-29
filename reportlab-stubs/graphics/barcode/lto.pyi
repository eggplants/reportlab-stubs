from typing import Any

from reportlab.graphics.barcode.code39 import Standard39 as Standard39
from reportlab.lib import colors as colors
from reportlab.lib.units import cm as cm

class BaseLTOLabel(Standard39):
    LABELWIDTH: Any
    LABELHEIGHT: Any
    LABELROUND: Any
    CODERATIO: float
    CODENOMINALWIDTH: Any
    CODEBARHEIGHT: Any
    CODEBARWIDTH: Any
    CODEGAP: Any
    CODELQUIET: Any
    CODERQUIET: Any
    height: Any
    border: Any
    label: Any
    def __init__(
        self,
        prefix: str = ...,
        number: Any | None = ...,
        subtype: str = ...,
        border: Any | None = ...,
        checksum: bool = ...,
        availheight: Any | None = ...,
    ) -> None: ...
    def drawOn(self, canvas, x, y) -> None: ...

class VerticalLTOLabel(BaseLTOLabel):
    LABELFONT: Any
    BLOCKWIDTH: Any
    BLOCKHEIGHT: Any
    LINEWIDTH: float
    NBBLOCKS: int
    COLORSCHEME: Any
    colored: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def drawOn(self, canvas, x, y) -> None: ...

def test() -> None: ...
