from typing import Any

from reportlab.lib import colors as colors
from reportlab.lib import logger as logger
from reportlab.lib.attrmap import *
from reportlab.lib.fonts import tt2ps as tt2ps
from reportlab.lib.rl_accel import fp_str as fp_str
from reportlab.lib.utils import asBytes as asBytes
from reportlab.lib.utils import isSeq as isSeq
from reportlab.lib.validators import *
from reportlab.pdfbase.pdfmetrics import stringWidth as stringWidth
from reportlab.pdfgen.canvas import FILL_EVEN_ODD as FILL_EVEN_ODD
from reportlab.pdfgen.canvas import FILL_NON_ZERO as FILL_NON_ZERO
from reportlab.platypus import Flowable as Flowable
from reportlab.rl_config import _unset_ as _unset_
from reportlab.rl_config import decimalSymbol as decimalSymbol
from reportlab.rl_config import shapeChecking as shapeChecking
from reportlab.rl_config import verbose as verbose

from .transform import *

__version__: str
__doc__: str
isOpacity: Any
_baseGFontNameB: Any
_baseGFontNameI: Any
_baseGFontNameBI: Any
NON_ZERO_WINDING: str
EVEN_ODD: str
STATE_DEFAULTS: Any

def _textBoxLimits(text, font, fontSize, leading, textAnchor, boxAnchor): ...
def _rotatedBoxLimits(x, y, w, h, angle): ...

class _DrawTimeResizeable:
    def _drawTimeResize(self, w, h) -> None: ...

class _SetKeyWordArgs:
    def __init__(self, keywords=...) -> None: ...

def getRectsBounds(rectList): ...
def _getBezierExtrema(y0, y1, y2, y3): ...
def getPathBounds(points): ...
def getPointsBounds(pointList): ...

class Shape(_SetKeyWordArgs, _DrawTimeResizeable):
    _attrMap: Any
    def copy(self) -> None: ...
    def getProperties(self, recur: int = ...): ...
    def setProperties(self, props) -> None: ...
    def dumpProperties(self, prefix: str = ...) -> None: ...
    def verify(self) -> None: ...
    def __setattr__(self, attr, value) -> None: ...
    def getBounds(self) -> None: ...

class Group(Shape):
    _attrMap: Any
    contents: Any
    transform: Any
    def __init__(self, *elements, **keywords) -> None: ...
    def _addNamedNode(self, name, node) -> None: ...
    def add(self, node, name: Any | None = ...) -> None: ...
    def _nn(self, node): ...
    def insert(self, i, n, name: Any | None = ...) -> None: ...
    def expandUserNodes(self): ...
    def _explode(self): ...
    def _copyContents(self, obj) -> None: ...
    def _copyNamedContents(self, obj, aKeys: Any | None = ..., noCopy=...) -> None: ...
    def _copy(self, obj): ...
    def copy(self): ...
    def rotate(self, theta) -> None: ...
    def translate(self, dx, dy) -> None: ...
    def scale(self, sx, sy) -> None: ...
    def skew(self, kx, ky) -> None: ...
    def shift(self, x, y) -> None: ...
    __class__: Any
    width: Any
    height: Any
    def asDrawing(self, width, height) -> None: ...
    def getContents(self): ...
    def getBounds(self): ...

def _addObjImport(obj, I, n: Any | None = ...) -> None: ...
def _repr(self, I: Any | None = ...): ...
def _renderGroupPy(G, pfx, I, i: int = ..., indent: str = ...): ...
def _extraKW(self, pfx, **kw): ...

class Drawing(Group, Flowable):
    _saveModes: Any
    _bmModes: Any
    _xtraAttrMap: Any
    _attrMap: Any
    background: Any
    width: Any
    height: Any
    hAlign: str
    vAlign: str
    renderScale: float
    def __init__(
        self, width: int = ..., height: int = ..., *nodes, **keywords
    ) -> None: ...
    def _renderPy(self): ...
    def draw(self, showBoundary=...) -> None: ...
    def wrap(self, availWidth, availHeight): ...
    def expandUserNodes(self): ...
    def copy(self): ...
    def asGroup(self, *args, **kw): ...
    def save(
        self,
        formats: Any | None = ...,
        verbose: Any | None = ...,
        fnRoot: Any | None = ...,
        outDir: Any | None = ...,
        title: str = ...,
        **kw
    ): ...
    def asString(self, format, verbose: Any | None = ..., preview: int = ..., **kw): ...
    def resized(
        self,
        kind: str = ...,
        lpad: int = ...,
        rpad: int = ...,
        bpad: int = ...,
        tpad: int = ...,
    ): ...

class _DrawingEditorMixin:
    def _add(
        self,
        obj,
        value,
        name: Any | None = ...,
        validate: Any | None = ...,
        desc: Any | None = ...,
        pos: Any | None = ...,
    ) -> None: ...

class isStrokeDashArray(Validator):
    def test(self, x): ...

class LineShape(Shape):
    _attrMap: Any
    strokeColor: Any
    strokeWidth: int
    strokeLineCap: int
    strokeLineJoin: int
    strokeMiterLimit: int
    strokeDashArray: Any
    strokeOpacity: Any
    def __init__(self, kw) -> None: ...

class Line(LineShape):
    _attrMap: Any
    x1: Any
    y1: Any
    x2: Any
    y2: Any
    def __init__(self, x1, y1, x2, y2, **kw) -> None: ...
    def getBounds(self): ...

class SolidShape(LineShape):
    _attrMap: Any
    fillColor: Any
    fillOpacity: Any
    def __init__(self, kw) -> None: ...

_MOVETO: Any
_LINETO: Any
_CURVETO: Any
_CLOSEPATH: Any
_PATH_OP_ARG_COUNT: Any
_PATH_OP_NAMES: Any

def _renderPath(path, drawFuncs, countOnly: bool = ..., forceClose: bool = ...): ...

_fillModeMap: Any

class Path(SolidShape):
    _attrMap: Any
    points: Any
    operators: Any
    isClipPath: Any
    autoclose: Any
    fillMode: Any
    def __init__(
        self,
        points: Any | None = ...,
        operators: Any | None = ...,
        isClipPath: int = ...,
        autoclose: Any | None = ...,
        fillMode=...,
        **kw
    ) -> None: ...
    def copy(self): ...
    def moveTo(self, x, y) -> None: ...
    def lineTo(self, x, y) -> None: ...
    def curveTo(self, x1, y1, x2, y2, x3, y3) -> None: ...
    def closePath(self) -> None: ...
    def getBounds(self): ...

EmptyClipPath: Any

def getArcPoints(
    centerx,
    centery,
    radius,
    startangledegrees,
    endangledegrees,
    yradius: Any | None = ...,
    degreedelta: Any | None = ...,
    reverse: Any | None = ...,
): ...

class ArcPath(Path):
    def addArc(
        self,
        centerx,
        centery,
        radius,
        startangledegrees,
        endangledegrees,
        yradius: Any | None = ...,
        degreedelta: Any | None = ...,
        moveTo: Any | None = ...,
        reverse: Any | None = ...,
    ) -> None: ...

def definePath(
    pathSegs=..., isClipPath: int = ..., dx: int = ..., dy: int = ..., **kw
): ...

class Rect(SolidShape):
    _attrMap: Any
    x: Any
    y: Any
    width: Any
    height: Any
    rx: Any
    ry: Any
    def __init__(
        self, x, y, width, height, rx: int = ..., ry: int = ..., **kw
    ) -> None: ...
    def copy(self): ...
    def getBounds(self): ...

class Image(SolidShape):
    _attrMap: Any
    x: Any
    y: Any
    width: Any
    height: Any
    path: Any
    def __init__(self, x, y, width, height, path, **kw) -> None: ...
    def copy(self): ...
    def getBounds(self): ...

class Circle(SolidShape):
    _attrMap: Any
    cx: Any
    cy: Any
    r: Any
    def __init__(self, cx, cy, r, **kw) -> None: ...
    def copy(self): ...
    def getBounds(self): ...

class Ellipse(SolidShape):
    _attrMap: Any
    cx: Any
    cy: Any
    rx: Any
    ry: Any
    def __init__(self, cx, cy, rx, ry, **kw) -> None: ...
    def copy(self): ...
    def getBounds(self): ...

class Wedge(SolidShape):
    _attrMap: Any
    degreedelta: int
    yradius: Any
    annular: Any
    def __init__(
        self,
        centerx,
        centery,
        radius,
        startangledegrees,
        endangledegrees,
        yradius: Any | None = ...,
        annular: bool = ...,
        **kw
    ) -> None: ...
    def _xtraRadii(self): ...
    def asPolygon(self): ...
    def copy(self): ...
    def getBounds(self): ...

class Polygon(SolidShape):
    _attrMap: Any
    points: Any
    def __init__(self, points=..., **kw) -> None: ...
    def copy(self): ...
    def getBounds(self): ...

class PolyLine(LineShape):
    _attrMap: Any
    points: Any
    def __init__(self, points=..., **kw) -> None: ...
    def copy(self): ...
    def getBounds(self): ...

class Hatching(Path):
    _attrMap: Any
    xyLists: Any
    angles: Any
    spacings: Any
    def __init__(
        self, spacings: int = ..., angles: int = ..., xyLists=..., **kwds
    ) -> None: ...

def numericXShift(
    tA, text, w, fontName, fontSize, encoding: Any | None = ..., pivotCharacter=...
): ...

class String(Shape):
    _attrMap: Any
    encoding: str
    x: Any
    y: Any
    text: Any
    textAnchor: str
    fontName: Any
    fontSize: Any
    fillColor: Any
    def __init__(self, x, y, text, **kw) -> None: ...
    def getEast(self): ...
    def copy(self): ...
    def getBounds(self): ...

class UserNode(_DrawTimeResizeable):
    def provideNode(self) -> None: ...

class DirectDraw(Shape):
    def drawDirectly(self, canvas) -> None: ...

def test() -> None: ...
