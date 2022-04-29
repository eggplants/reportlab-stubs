from typing import Any

from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import EmptyClipPath as EmptyClipPath
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Line as Line
from reportlab.graphics.shapes import LineShape as LineShape
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.shapes import definePath as definePath
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import AttrMap as AttrMap
from reportlab.lib.attrmap import AttrMapValue as AttrMapValue
from reportlab.lib.validators import OneOf as OneOf
from reportlab.lib.validators import isBoolean as isBoolean
from reportlab.lib.validators import isColorOrNone as isColorOrNone
from reportlab.lib.validators import isListOfColors as isListOfColors
from reportlab.lib.validators import isListOfNumbers as isListOfNumbers
from reportlab.lib.validators import isNumber as isNumber
from reportlab.lib.validators import isNumberOrNone as isNumberOrNone

__version__: str

def frange(start, end: Any | None = ..., inc: Any | None = ...): ...
def makeDistancesList(list): ...

class Grid(Widget):
    _attrMap: Any
    x: int
    y: int
    width: int
    height: int
    orientation: str
    useLines: int
    useRects: int
    delta: int
    delta0: int
    deltaSteps: Any
    fillColor: Any
    stripeColors: Any
    strokeColor: Any
    strokeWidth: int
    def __init__(self) -> None: ...
    def demo(self): ...
    def makeOuterRect(self): ...
    def makeLinePosList(self, start, isX: int = ...): ...
    def makeInnerLines(self): ...
    def makeInnerTiles(self): ...
    def draw(self): ...

class DoubleGrid(Widget):
    _attrMap: Any
    x: int
    y: int
    width: int
    height: int
    grid0: Any
    grid1: Any
    def __init__(self) -> None: ...
    def demo(self): ...
    def draw(self): ...

class ShadedRect(Widget):
    _attrMap: Any
    x: int
    y: int
    width: int
    height: int
    orientation: str
    numShades: int
    fillColorStart: Any
    fillColorEnd: Any
    strokeColor: Any
    strokeWidth: int
    cylinderMode: int
    def __init__(self, **kw) -> None: ...
    def demo(self): ...
    def _flipRectCorners(self): ...
    def draw(self): ...

def colorRange(c0, c1, n): ...
def centroid(P): ...
def rotatedEnclosingRect(P, angle, rect): ...

class ShadedPolygon(Widget, LineShape):
    _attrMap: Any
    angle: int
    fillColorStart: Any
    fillColorEnd: Any
    cylinderMode: int
    numShades: int
    points: Any
    def __init__(self, **kw) -> None: ...
    def draw(self): ...
