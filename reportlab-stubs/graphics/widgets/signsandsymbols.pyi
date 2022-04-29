from typing import Any

from reportlab.graphics import renderPDF as renderPDF
from reportlab.graphics import shapes as shapes
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import *
from reportlab.lib.utils import asUnicode as asUnicode
from reportlab.lib.utils import isStr as isStr
from reportlab.lib.validators import *

__version__: str
__doc__: str

class _Symbol(Widget):
    _nodoc: int
    _attrMap: Any
    x: int
    size: int
    fillColor: Any
    strokeColor: Any
    strokeWidth: float
    def __init__(self) -> None: ...
    def demo(self): ...

class ETriangle(_Symbol):
    def __init__(self) -> None: ...
    def draw(self): ...

class RTriangle(_Symbol):
    x: int
    y: int
    size: int
    fillColor: Any
    strokeColor: Any
    def __init__(self) -> None: ...
    def draw(self): ...

class Octagon(_Symbol):
    x: int
    y: int
    size: int
    fillColor: Any
    strokeColor: Any
    def __init__(self) -> None: ...
    def draw(self): ...

class Crossbox(_Symbol):
    _attrMap: Any
    x: int
    y: int
    size: int
    fillColor: Any
    crossColor: Any
    strokeColor: Any
    crosswidth: int
    def __init__(self) -> None: ...
    def draw(self): ...

class Tickbox(_Symbol):
    _attrMap: Any
    x: int
    y: int
    size: int
    tickColor: Any
    strokeColor: Any
    fillColor: Any
    tickwidth: int
    def __init__(self) -> None: ...
    def draw(self): ...

class SmileyFace(_Symbol):
    x: int
    y: int
    size: int
    fillColor: Any
    strokeColor: Any
    def __init__(self) -> None: ...
    def draw(self): ...

class StopSign(_Symbol):
    _attrMap: Any
    x: int
    y: int
    size: int
    strokeColor: Any
    fillColor: Any
    stopColor: Any
    def __init__(self) -> None: ...
    def draw(self): ...

class NoEntry(_Symbol):
    _attrMap: Any
    x: int
    y: int
    size: int
    strokeColor: Any
    fillColor: Any
    innerBarColor: Any
    def __init__(self) -> None: ...
    def draw(self): ...

class NotAllowed(_Symbol):
    _attrMap: Any
    x: int
    y: int
    size: int
    strokeColor: Any
    fillColor: Any
    def __init__(self) -> None: ...
    def draw(self): ...

class NoSmoking(NotAllowed):
    def __init__(self) -> None: ...
    def draw(self): ...

class DangerSign(_Symbol):
    x: int
    y: int
    size: int
    strokeColor: Any
    fillColor: Any
    strokeWidth: Any
    def __init__(self) -> None: ...
    def draw(self): ...

class YesNo(_Symbol):
    _attrMap: Any
    x: int
    y: int
    size: int
    tickcolor: Any
    crosscolor: Any
    testValue: int
    def __init__(self) -> None: ...
    def draw(self): ...
    def demo(self): ...

class FloppyDisk(_Symbol):
    _attrMap: Any
    x: int
    y: int
    size: int
    diskColor: Any
    def __init__(self) -> None: ...
    def draw(self): ...

class ArrowOne(_Symbol):
    x: int
    y: int
    size: int
    fillColor: Any
    strokeWidth: int
    strokeColor: Any
    def __init__(self) -> None: ...
    def draw(self): ...

class ArrowTwo(ArrowOne):
    x: int
    y: int
    size: int
    fillColor: Any
    strokeWidth: int
    strokeColor: Any
    def __init__(self) -> None: ...
    def draw(self): ...

class CrossHair(_Symbol):
    _attrMap: Any
    x: int
    size: int
    fillColor: Any
    strokeColor: Any
    strokeWidth: float
    innerGap: str
    def __init__(self) -> None: ...
    def draw(self): ...

def test() -> None: ...
