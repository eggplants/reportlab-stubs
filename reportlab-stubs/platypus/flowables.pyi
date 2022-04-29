from collections.abc import Generator
from typing import Any

from reportlab.lib.abag import ABag

class TraceInfo:
    srcFile: str
    startLineNo: int
    startLinePos: int
    endLineNo: int
    endLinePos: int
    def __init__(self) -> None: ...

class Flowable:
    _fixedWidth: int
    _fixedHeight: int
    width: int
    height: int
    wrapped: int
    hAlign: str
    vAlign: str
    _traceInfo: Any
    _showBoundary: Any
    encoding: Any
    def __init__(self) -> None: ...
    canv: Any
    def _drawOn(self, canv) -> None: ...
    def _hAlignAdjust(self, x, sW: int = ...): ...
    def drawOn(self, canvas, x, y, _sW: int = ...) -> None: ...
    def wrapOn(self, canv, aW, aH): ...
    def wrap(self, availWidth, availHeight): ...
    def minWidth(self): ...
    def splitOn(self, canv, aW, aH): ...
    def split(self, availWidth, availheight): ...
    def getKeepWithNext(self): ...
    def getSpaceAfter(self): ...
    def getSpaceBefore(self): ...
    def isIndexing(self): ...
    def identity(self, maxLen: Any | None = ...): ...
    @property
    def _doctemplate(self): ...
    def _doctemplateAttr(self, a): ...
    def _frameName(self): ...

class XBox(Flowable):
    width: Any
    height: Any
    text: Any
    def __init__(self, width, height, text: str = ...) -> None: ...
    def __repr__(self): ...
    def draw(self) -> None: ...

def splitLines(lines, maximum_length, split_characters, new_line_characters): ...
def splitLine(
    line_to_split, lines_split, maximum_length, split_characters, new_line_characters
) -> None: ...

class Preformatted(Flowable):
    style: Any
    bulletText: Any
    lines: Any
    def __init__(
        self,
        text,
        style,
        bulletText: Any | None = ...,
        dedent: int = ...,
        maxLineLength: Any | None = ...,
        splitChars: Any | None = ...,
        newLineChars: str = ...,
    ) -> None: ...
    def __repr__(self): ...
    width: Any
    height: Any
    def wrap(self, availWidth, availHeight): ...
    def minWidth(self): ...
    def split(self, availWidth, availHeight): ...
    def draw(self) -> None: ...

class Image(Flowable):
    _fixedWidth: int
    _fixedHeight: int
    hAlign: Any
    _mask: Any
    _drawing: Any
    _file: Any
    filename: Any
    _img: Any
    _dpi: Any
    imageWidth: Any
    imageHeight: Any
    def __init__(
        self,
        filename,
        width: Any | None = ...,
        height: Any | None = ...,
        kind: str = ...,
        mask: str = ...,
        lazy: int = ...,
        hAlign: str = ...,
        useDPI: bool = ...,
    ) -> None: ...
    def _dpiAdjust(self) -> None: ...
    _lazy: Any
    _width: Any
    _height: Any
    _kind: Any
    def _setup(self, width, height, kind, lazy) -> None: ...
    drawWidth: Any
    drawHeight: Any
    def _setup_inner(self) -> None: ...
    _oldDrawSize: Any
    def _restrictSize(self, aW, aH): ...
    def _unRestrictSize(self) -> None: ...
    def __getattr__(self, a): ...
    def wrap(self, availWidth, availHeight): ...
    def draw(self) -> None: ...
    def identity(self, maxLen: Any | None = ...): ...

class NullDraw(Flowable):
    def draw(self) -> None: ...

class Spacer(NullDraw):
    _fixedWidth: int
    _fixedHeight: int
    width: Any
    height: float
    spacebefore: Any
    def __init__(self, width, height, isGlue: bool = ...) -> None: ...
    def __repr__(self): ...

class UseUpSpace(NullDraw):
    def __init__(self) -> None: ...
    def __repr__(self): ...
    width: Any
    height: Any
    def wrap(self, availWidth, availHeight): ...

class PageBreak(UseUpSpace):
    locChanger: int
    nextTemplate: Any
    def __init__(self, nextTemplate: Any | None = ...) -> None: ...
    def __repr__(self): ...

class SlowPageBreak(PageBreak): ...
class PageBreakIfNotEmpty(PageBreak): ...

class CondPageBreak(Spacer):
    locChanger: int
    height: Any
    def __init__(self, height) -> None: ...
    def __repr__(self): ...
    def wrap(self, availWidth, availHeight): ...
    def identity(self, maxLen: Any | None = ...): ...

class _ContainerSpace:
    def getSpaceBefore(self, content: Any | None = ...): ...
    def getSpaceAfter(self, content: Any | None = ...): ...

class KeepTogether(_ContainerSpace, Flowable):
    splitAtTop: bool
    _content: Any
    _maxHeight: Any
    def __init__(self, flowables, maxHeight: Any | None = ...) -> None: ...
    def __repr__(self): ...
    _H: Any
    _H0: Any
    _wrapInfo: Any
    def wrap(self, aW, aH): ...
    def split(self, aW, aH): ...
    def identity(self, maxLen: Any | None = ...): ...

class KeepTogetherSplitAtTop(KeepTogether):
    splitAtTop: bool

class Macro(Flowable):
    command: Any
    def __init__(self, command) -> None: ...
    def __repr__(self): ...
    def wrap(self, availWidth, availHeight): ...
    def draw(self) -> None: ...

class CallerMacro(Flowable):
    _drawCallable: Any
    _wrapCallable: Any
    def __init__(
        self, drawCallable: Any | None = ..., wrapCallable: Any | None = ...
    ) -> None: ...
    def __repr__(self): ...
    def wrap(self, aW, aH): ...
    def draw(self) -> None: ...

class ParagraphAndImage(Flowable):
    P: Any
    I: Any
    xpad: Any
    ypad: Any
    _side: Any
    def __init__(
        self, P, I, xpad: int = ..., ypad: int = ..., side: str = ...
    ) -> None: ...
    def getSpaceBefore(self): ...
    def getSpaceAfter(self): ...
    wI: Any
    hI: Any
    width: Any
    _offsets: Any
    height: Any
    def wrap(self, availWidth, availHeight): ...
    def split(self, availWidth, availHeight): ...
    def draw(self) -> None: ...

class FailOnWrap(NullDraw):
    def wrap(self, availWidth, availHeight) -> None: ...

class FailOnDraw(Flowable):
    def wrap(self, availWidth, availHeight): ...
    def draw(self) -> None: ...

class HRFlowable(Flowable):
    width: Any
    lineWidth: Any
    lineCap: Any
    spaceBefore: Any
    spaceAfter: Any
    color: Any
    hAlign: Any
    vAlign: Any
    dash: Any
    def __init__(
        self,
        width: str = ...,
        thickness: int = ...,
        lineCap: str = ...,
        color=...,
        spaceBefore: int = ...,
        spaceAfter: int = ...,
        hAlign: str = ...,
        vAlign: str = ...,
        dash: Any | None = ...,
    ) -> None: ...
    def __repr__(self): ...
    _width: Any
    def wrap(self, availWidth, availHeight): ...
    def draw(self) -> None: ...

class _PTOInfo:
    trailer: Any
    header: Any
    def __init__(self, trailer, header) -> None: ...

class _Container(_ContainerSpace):
    def drawOn(
        self,
        canv,
        x,
        y,
        _sW: int = ...,
        scale: float = ...,
        content: Any | None = ...,
        aW: Any | None = ...,
    ) -> None: ...
    _content: Any
    def copyContent(self, content: Any | None = ...) -> None: ...

class PTOContainer(_Container, Flowable):
    _content: Any
    def __init__(
        self, content, trailer: Any | None = ..., header: Any | None = ...
    ) -> None: ...
    def wrap(self, availWidth, availHeight): ...
    def split(self, availWidth, availHeight): ...

class KeepInFrame(_Container, Flowable):
    name: Any
    maxWidth: Any
    maxHeight: Any
    mode: Any
    mergespace: Any
    _content: Any
    vAlign: Any
    hAlign: Any
    fakeWidth: Any
    def __init__(
        self,
        maxWidth,
        maxHeight,
        content=...,
        mergeSpace: int = ...,
        mode: str = ...,
        name: str = ...,
        hAlign: str = ...,
        vAlign: str = ...,
        fakeWidth: Any | None = ...,
    ) -> None: ...
    def _getAvailableWidth(self): ...
    def identity(self, maxLen: Any | None = ...): ...
    width: Any
    height: Any
    _scale: Any
    def wrap(self, availWidth, availHeight): ...
    def drawOn(self, canv, x, y, _sW: int = ...) -> None: ...

class _FindSplitterMixin:
    def _findSplit(
        self,
        canv,
        availWidth,
        availHeight,
        mergeSpace: int = ...,
        obj: Any | None = ...,
        content: Any | None = ...,
        paraFix: bool = ...,
    ): ...
    def _getContent(self, content: Any | None = ...): ...

class ImageAndFlowables(_Container, _FindSplitterMixin, Flowable):
    _content: Any
    _I: Any
    _irpad: Any
    _ilpad: Any
    _ibpad: Any
    _itpad: Any
    _side: Any
    imageHref: Any
    def __init__(
        self,
        I,
        F,
        imageLeftPadding: int = ...,
        imageRightPadding: int = ...,
        imageTopPadding: int = ...,
        imageBottomPadding: int = ...,
        imageSide: str = ...,
        imageHref: Any | None = ...,
    ) -> None: ...
    def deepcopy(self): ...
    def getSpaceAfter(self): ...
    def getSpaceBefore(self): ...
    def _reset(self) -> None: ...
    _wrapArgs: Any
    _wI: Any
    _hI: Any
    _iW: Any
    _C0: Any
    _C1: Any
    width: Any
    height: Any
    def wrap(self, availWidth, availHeight): ...
    def split(self, availWidth, availHeight): ...
    def drawOn(self, canv, x, y, _sW: int = ...) -> None: ...

class _AbsRect(NullDraw):
    _ZEROSIZE: int
    _SPACETRANSFER: bool
    _x: Any
    _y: Any
    _width: Any
    _height: Any
    _strokeColor: Any
    _fillColor: Any
    _strokeWidth: Any
    _strokeDashArray: Any
    def __init__(
        self,
        x,
        y,
        width,
        height,
        strokeWidth: int = ...,
        strokeColor: Any | None = ...,
        fillColor: Any | None = ...,
        strokeDashArray: Any | None = ...,
    ) -> None: ...
    def wrap(self, availWidth, availHeight): ...
    def drawOn(self, canv, x, y, _sW: int = ...) -> None: ...

class _ExtendBG(NullDraw):
    _ZEROSIZE: int
    _SPACETRANSFER: bool
    _y: Any
    _height: Any
    _bg: Any
    def __init__(self, y, height, bg, frame) -> None: ...
    def wrap(self, availWidth, availHeight): ...
    def frameAction(self, frame) -> None: ...

class _AbsLine(NullDraw):
    _ZEROSIZE: int
    _SPACETRANSFER: bool
    _x: Any
    _y: Any
    _x1: Any
    _y1: Any
    _strokeColor: Any
    _strokeWidth: Any
    _strokeDashArray: Any
    def __init__(
        self,
        x,
        y,
        x1,
        y1,
        strokeWidth: int = ...,
        strokeColor: Any | None = ...,
        strokeDashArray: Any | None = ...,
    ) -> None: ...
    def wrap(self, availWidth, availHeight): ...
    def drawOn(self, canv, x, y, _sW: int = ...) -> None: ...

class BalancedColumns(_FindSplitterMixin, NullDraw):
    name: Any
    _content: Any
    _nCols: Any
    spaceAfter: Any
    _leftPadding: Any
    _innerPadding: Any
    _rightPadding: Any
    _topPadding: Any
    _bottomPadding: Any
    spaceBefore: Any
    _needed: Any
    showBoundary: Any
    endSlack: Any
    _boxStrokeColor: Any
    _boxStrokeWidth: Any
    _boxFillColor: Any
    _boxMargin: Any
    _vLinesStrokeColor: Any
    _vLinesStrokeWidth: Any
    def __init__(
        self,
        F,
        nCols: int = ...,
        needed: int = ...,
        spaceBefore: int = ...,
        spaceAfter: int = ...,
        showBoundary: Any | None = ...,
        leftPadding: Any | None = ...,
        innerPadding: Any | None = ...,
        rightPadding: Any | None = ...,
        topPadding: Any | None = ...,
        bottomPadding: Any | None = ...,
        name: str = ...,
        endSlack: float = ...,
        boxStrokeColor: Any | None = ...,
        boxStrokeWidth: int = ...,
        boxFillColor: Any | None = ...,
        boxMargin: Any | None = ...,
        vLinesStrokeColor: Any | None = ...,
        vLinesStrokeWidth: Any | None = ...,
    ) -> None: ...
    def identity(self, maxLen: Any | None = ...): ...
    def getSpaceAfter(self): ...
    def getSpaceBefore(self): ...
    bgs: Any
    F: Any
    f: Any
    def _generated_content(self, aW, aH): ...
    def wrap(self, aW, aH): ...

class AnchorFlowable(Spacer):
    _ZEROSIZE: int
    _SPACETRANSFER: bool
    _name: Any
    def __init__(self, name) -> None: ...
    def __repr__(self): ...
    def wrap(self, aW, aH): ...
    def draw(self) -> None: ...

class _FBGBag(ABag):
    def matches(self, frame, canv): ...
    _inst: Any
    def getDims(self, canv): ...
    def setDims(self, canv, x, y, w, h) -> None: ...
    fid: Any
    cid: Any
    pn: Any
    codePos: Any
    def render(self, canv, frame, fbx, fby, fbw, fbh) -> None: ...

class FrameBG(AnchorFlowable):
    _ZEROSIZE: int
    start: Any
    left: Any
    right: Any
    color: Any
    strokeWidth: Any
    strokeColor: Any
    strokeDashArray: Any
    def __init__(
        self,
        color: Any | None = ...,
        left: int = ...,
        right: int = ...,
        start: bool = ...,
        strokeWidth: Any | None = ...,
        strokeColor: Any | None = ...,
        strokeDashArray: Any | None = ...,
    ) -> None: ...
    def __repr__(self): ...
    def draw(self) -> None: ...

class FrameSplitter(NullDraw):
    _ZEROSIZE: int
    nextTemplate: Any
    nextFrames: Any
    gap: Any
    required: Any
    adjustHeight: Any
    def __init__(
        self,
        nextTemplate,
        nextFrames=...,
        gap: int = ...,
        required: int = ...,
        adjustHeight: bool = ...,
    ) -> None: ...
    def wrap(self, aW, aH): ...

class BulletDrawer:
    value: Any
    _bulletAlign: Any
    _bulletType: Any
    _bulletColor: Any
    _bulletFontName: Any
    _bulletFontSize: Any
    _bulletOffsetY: Any
    _bulletDedent: Any
    _bulletDir: Any
    _bulletFormat: Any
    def __init__(
        self,
        value: str = ...,
        bulletAlign: str = ...,
        bulletType: str = ...,
        bulletColor: str = ...,
        bulletFontName: str = ...,
        bulletFontSize: int = ...,
        bulletOffsetY: int = ...,
        bulletDedent: int = ...,
        bulletDir: str = ...,
        bulletFormat: Any | None = ...,
    ) -> None: ...
    def drawOn(self, indenter, canv, x, y, _sW: int = ...) -> None: ...

class DDIndenter(Flowable):
    _IndenterAttrs: Any
    _flowable: Any
    _leftIndent: Any
    _rightIndent: Any
    width: Any
    height: Any
    def __init__(
        self, flowable, leftIndent: int = ..., rightIndent: int = ...
    ) -> None: ...
    def split(self, aW, aH): ...
    def drawOn(self, canv, x, y, _sW: int = ...) -> None: ...
    def wrap(self, aW, aH): ...
    def __getattr__(self, a): ...
    def __setattr__(self, a, v) -> None: ...
    def __delattr__(self, a) -> None: ...
    def identity(self, maxLen: Any | None = ...): ...

class LIIndenter(DDIndenter):
    _IndenterAttrs: Any
    _flowable: Any
    _bullet: Any
    _leftIndent: Any
    _rightIndent: Any
    width: Any
    height: Any
    spaceBefore: Any
    spaceAfter: Any
    def __init__(
        self,
        flowable,
        leftIndent: int = ...,
        rightIndent: int = ...,
        bullet: Any | None = ...,
        spaceBefore: Any | None = ...,
        spaceAfter: Any | None = ...,
    ) -> None: ...
    def split(self, aW, aH): ...
    def drawOn(self, canv, x, y, _sW: int = ...) -> None: ...

class ListItem:
    _flowables: Any
    _style: Any
    def __init__(self, flowables, style: Any | None = ..., **kwds) -> None: ...

class _LIParams:
    flowable: Any
    params: Any
    value: Any
    first: Any
    def __init__(self, flowable, params, value, first) -> None: ...

class ListFlowable(_Container, Flowable):
    _numberStyles: str
    _flowables: Any
    style: Any
    _start: Any
    _auto: Any
    _list_content: Any
    _dims: Any
    def __init__(
        self, flowables, start: Any | None = ..., style: Any | None = ..., **kwds
    ) -> None: ...
    @property
    def _content(self): ...
    def wrap(self, aW, aH): ...
    def split(self, aW, aH): ...
    def _flowablesIter(self) -> Generator[Any, None, None]: ...
    def _makeLIIndenter(self, flowable, bullet, params: Any | None = ...): ...
    def _makeBullet(self, value, params: Any | None = ...): ...
    _calcBulletDedent: Any
    def _getContent(self): ...

class TopPadder(Flowable):
    def __init__(self, f) -> None: ...
    def wrap(self, aW, aH): ...
    def split(self, aW, aH): ...
    def drawOn(self, canvas, x, y, _sW: int = ...) -> None: ...
    def __setattr__(self, a, v) -> None: ...
    def __getattr__(self, a): ...
    def __delattr__(self, a) -> None: ...

class DocAssign(NullDraw):
    _ZEROSIZE: int
    args: Any
    def __init__(self, var, expr, life: str = ...) -> None: ...
    def funcWrap(self, aW, aH): ...
    def func(self): ...
    def wrap(self, aW, aH): ...

class DocExec(DocAssign):
    args: Any
    def __init__(self, stmt, lifetime: str = ...) -> None: ...

class DocPara(DocAssign):
    expr: Any
    format: Any
    style: Any
    klass: Any
    escape: Any
    def __init__(
        self,
        expr,
        format: Any | None = ...,
        style: Any | None = ...,
        klass: Any | None = ...,
        escape: bool = ...,
    ) -> None: ...
    def func(self): ...
    def add_content(self, *args) -> None: ...
    def get_value(self, aW, aH): ...
    def wrap(self, aW, aH): ...

class DocAssert(DocPara):
    expr: Any
    format: Any
    def __init__(self, cond, format: Any | None = ...) -> None: ...
    _cond: Any
    def funcWrap(self, aW, aH): ...
    def wrap(self, aW, aH): ...

class DocIf(DocPara):
    expr: Any
    blocks: Any
    def __init__(self, cond, thenBlock, elseBlock=...) -> None: ...
    def checkBlock(self, block): ...
    def wrap(self, aW, aH): ...

class DocWhile(DocIf):
    expr: Any
    block: Any
    def __init__(self, cond, whileBlock) -> None: ...
    def wrap(self, aW, aH): ...

class SetTopFlowables(NullDraw):
    _ZEROZSIZE: int
    _F: Any
    _show: Any
    def __init__(self, F, show: bool = ...) -> None: ...
    def wrap(self, aW, aH): ...

class SetPageTopFlowables(NullDraw):
    _ZEROZSIZE: int
    _F: Any
    _show: Any
    def __init__(self, F, show: bool = ...) -> None: ...
    def wrap(self, aW, aH): ...
