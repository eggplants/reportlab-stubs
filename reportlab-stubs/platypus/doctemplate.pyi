from typing import Any

from reportlab.platypus.flowables import *

class LayoutError(Exception): ...

class PTCycle(list):
    _restart: int
    _idx: int
    def __new__(cls, *args, **kwds): ...
    @property
    def next_value(self): ...
    @property
    def peek(self): ...

class IndexingFlowable(Flowable):
    def isIndexing(self): ...
    def isSatisfied(self): ...
    def notify(self, kind, stuff) -> None: ...
    def beforeBuild(self) -> None: ...
    def afterBuild(self) -> None: ...

class ActionFlowable(Flowable):
    action: Any
    def __init__(self, action=...) -> None: ...
    def apply(self, doc) -> None: ...
    def __call__(self): ...
    def identity(self, maxLen: Any | None = ...): ...

class NullActionFlowable(ActionFlowable):
    def apply(self, doc) -> None: ...

class LCActionFlowable(ActionFlowable):
    locChanger: int
    def wrap(self, availWidth, availHeight) -> None: ...
    def draw(self) -> None: ...

class NextFrameFlowable(ActionFlowable):
    locChanger: int
    def __init__(self, ix, resume: int = ...) -> None: ...

class CurrentFrameFlowable(LCActionFlowable):
    def __init__(self, ix, resume: int = ...) -> None: ...

class NullActionFlowable(ActionFlowable):
    def apply(self, doc) -> None: ...

class _FrameBreak(LCActionFlowable):
    def __call__(self, ix: Any | None = ..., resume: int = ...): ...
    def apply(self, doc) -> None: ...

FrameBreak: Any
PageBegin: Any

class FrameActionFlowable(Flowable):
    _fixedWidth: int
    _fixedHeight: int
    def __init__(self, *arg, **kw) -> None: ...
    def frameAction(self, frame) -> None: ...

class Indenter(FrameActionFlowable):
    _ZEROSIZE: bool
    width: int
    height: int
    left: Any
    right: Any
    def __init__(self, left: int = ..., right: int = ...) -> None: ...
    def frameAction(self, frame) -> None: ...

class NotAtTopPageBreak(FrameActionFlowable):
    locChanger: int
    nextTemplate: Any
    def __init__(self, nextTemplate: Any | None = ...) -> None: ...
    def frameAction(self, frame) -> None: ...

class NextPageTemplate(ActionFlowable):
    locChanger: int
    def __init__(self, pt) -> None: ...

class PageTemplate:
    id: Any
    frames: Any
    onPage: Any
    onPageEnd: Any
    pagesize: Any
    autoNextPageTemplate: Any
    cropBox: Any
    artBox: Any
    trimBox: Any
    bleedBox: Any
    def __init__(
        self,
        id: Any | None = ...,
        frames=...,
        onPage=...,
        onPageEnd=...,
        pagesize: Any | None = ...,
        autoNextPageTemplate: Any | None = ...,
        cropBox: Any | None = ...,
        artBox: Any | None = ...,
        trimBox: Any | None = ...,
        bleedBox: Any | None = ...,
    ) -> None: ...
    def beforeDrawPage(self, canv, doc) -> None: ...
    def checkPageSize(self, canv, doc) -> None: ...
    def afterDrawPage(self, canv, doc) -> None: ...

class onDrawStr(str):
    onDraw: Any
    kind: Any
    label: Any
    def __new__(cls, value, onDraw, label, kind: Any | None = ...): ...

class PageAccumulator:
    _count: int
    name: Any
    data: Any
    def __init__(self, name: Any | None = ...) -> None: ...
    def reset(self) -> None: ...
    def add(self, *args) -> None: ...
    def onDrawText(self, *args): ...
    def __call__(self, canv, kind, label) -> None: ...
    def attachToPageTemplate(self, pt) -> None: ...
    def onPage(self, canv, doc) -> None: ...
    def onPageEnd(self, canv, doc) -> None: ...
    def pageEndAction(self, canv, doc) -> None: ...
    def onDrawStr(self, value, *args): ...

class BaseDocTemplate:
    _initArgs: Any
    _invalidInitArgs: Any
    _firstPageTemplateIndex: int
    filename: Any
    _nameSpace: Any
    _lifetimes: Any
    pageTemplates: Any
    _pageRefs: Any
    _indexingFlowables: Any
    _onPage: Any
    _onProgress: Any
    _flowableCount: int
    _curPageFlowableCount: int
    _emptyPages: int
    _emptyPagesAllowed: int
    _leftExtraIndent: float
    _rightExtraIndent: float
    _topFlowables: Any
    _pageTopFlowables: Any
    _frameBGs: Any
    def __init__(self, filename, **kw) -> None: ...
    _rightMargin: Any
    _topMargin: Any
    width: Any
    height: Any
    def _calc(self) -> None: ...
    def setPageCallBack(self, func) -> None: ...
    def setProgressCallBack(self, func) -> None: ...
    def clean_hanging(self) -> None: ...
    def addPageTemplates(self, pageTemplates) -> None: ...
    _hanging: Any
    pageTemplate: Any
    page: int
    def handle_documentBegin(self) -> None: ...
    frame: Any
    def handle_pageBegin(self) -> None: ...
    def _setPageTemplate(self) -> None: ...
    def _samePT(self, npt): ...
    def handle_pageEnd(self) -> None: ...
    def handle_pageBreak(self, slow: Any | None = ...) -> None: ...
    def handle_frameBegin(
        self, resume: int = ..., pageTopFlowables: Any | None = ...
    ) -> None: ...
    def handle_frameEnd(self, resume: int = ...) -> None: ...
    _nextPageTemplateIndex: Any
    _nextPageTemplateCycle: Any
    def handle_nextPageTemplate(self, pt) -> None: ...
    def _peekNextPageTemplate(self, pt): ...
    def _peekNextFrame(self): ...
    _nextFrameIndex: Any
    def handle_nextFrame(self, fx, resume: int = ...) -> None: ...
    def handle_currentFrame(self, fx, resume: int = ...) -> None: ...
    def handle_breakBefore(self, flowables) -> None: ...
    def handle_keepWithNext(self, flowables) -> None: ...
    def _fIdent(self, f, maxLen: Any | None = ..., frame: Any | None = ...): ...
    def handle_flowable(self, flowables) -> None: ...
    _handle_documentBegin: Any
    _handle_pageBegin: Any
    _handle_pageEnd: Any
    _handle_frameBegin: Any
    _handle_frameEnd: Any
    _handle_flowable: Any
    _handle_nextPageTemplate: Any
    _handle_currentFrame: Any
    _handle_nextFrame: Any
    seq: Any
    def _makeCanvas(self, filename: Any | None = ..., canvasmaker=...): ...
    canv: Any
    def _startBuild(self, filename: Any | None = ..., canvasmaker=...) -> None: ...
    def _endBuild(self) -> None: ...
    _savedInfo: Any
    def build(self, flowables, filename: Any | None = ..., canvasmaker=...) -> None: ...
    def _allSatisfied(self): ...
    def notify(self, kind, stuff) -> None: ...
    def pageRef(self, label) -> None: ...
    _doSave: int
    _multiBuildEdits: Any
    def multiBuild(self, story, maxPasses: int = ..., **buildKwds): ...
    def afterInit(self) -> None: ...
    def beforeDocument(self) -> None: ...
    def beforePage(self) -> None: ...
    def afterPage(self) -> None: ...
    def filterFlowables(self, flowables) -> None: ...
    def afterFlowable(self, flowable) -> None: ...
    _allowedLifetimes: Any
    def docAssign(self, var, expr, lifetime) -> None: ...
    def docExec(self, stmt, lifetime) -> None: ...
    def _addVars(self, vars, lifetime) -> None: ...
    def _removeVars(self, lifetimes) -> None: ...
    def docEval(self, expr): ...

class SimpleDocTemplate(BaseDocTemplate):
    _invalidInitArgs: Any
    def handle_pageBegin(self) -> None: ...
    def build(
        self, flowables, onFirstPage=..., onLaterPages=..., canvasmaker=...
    ) -> None: ...
