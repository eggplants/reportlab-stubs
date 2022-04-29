from typing import Any

from reportlab.graphics.barcode.common import Barcode as Barcode
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.lib.attrmap import AttrMap as AttrMap
from reportlab.lib.attrmap import AttrMapValue as AttrMapValue
from reportlab.lib.colors import toColor as toColor
from reportlab.lib.utils import asBytes as asBytes
from reportlab.lib.validators import isBoxAnchor as isBoxAnchor
from reportlab.lib.validators import isColor as isColor
from reportlab.lib.validators import isColorOrNone as isColorOrNone
from reportlab.lib.validators import isNumber as isNumber
from reportlab.lib.validators import isString as isString

__all__: Any

def _numConv(x): ...

class _DMTXCheck:
    @classmethod
    def pylibdmtx_check(cls) -> None: ...

class DataMatrix(Barcode, _DMTXCheck):
    _recalc: bool
    color: Any
    bgColor: Any
    def __init__(self, value: str = ..., **kwds) -> None: ...
    @property
    def value(self): ...
    _value: Any
    @value.setter
    def value(self, v) -> None: ...
    @property
    def size(self): ...
    _size: Any
    @size.setter
    def size(self, v) -> None: ...
    @property
    def border(self): ...
    _border: Any
    @border.setter
    def border(self, v) -> None: ...
    @property
    def x(self): ...
    _x: Any
    @x.setter
    def x(self, v) -> None: ...
    @property
    def y(self): ...
    _y: Any
    @y.setter
    def y(self, v) -> None: ...
    @property
    def cellSize(self): ...
    _cellSize: Any
    @size.setter
    def cellSize(self, v) -> None: ...
    @property
    def encoding(self): ...
    _encoding: Any
    @encoding.setter
    def encoding(self, v) -> None: ...
    @property
    def anchor(self): ...
    _anchor: Any
    @anchor.setter
    def anchor(self, v) -> None: ...
    _nRows: Any
    _nCols: Any
    _matrix: Any
    _cellWidth: Any
    _cellHeight: Any
    _bord: Any
    _width: Any
    _height: Any
    def recalc(self) -> None: ...
    @property
    def matrix(self): ...
    @property
    def width(self): ...
    @property
    def height(self): ...
    @property
    def cellWidth(self): ...
    @property
    def cellHeight(self): ...
    def draw(self) -> None: ...

class DataMatrixWidget(Widget, _DMTXCheck):
    codeName: str
    _attrMap: Any
    _defaults: Any
    value: Any
    def __init__(self, value: str = ..., **kwds) -> None: ...
    def rect(self, x, y, w, h, fill: int = ..., stroke: int = ...) -> None: ...
    def saveState(self, *args, **kwds) -> None: ...
    restoreState: Any
    setStrokeColor: Any
    _fillColor: Any
    def setFillColor(self, c) -> None: ...
    _gadd: Any
    def draw(self): ...
