from typing import Any

from reportlab.lib import colors as colors
from reportlab.lib.colors import toColor as toColor
from reportlab.lib.enums import TA_CENTER as TA_CENTER
from reportlab.lib.enums import TA_LEFT as TA_LEFT
from reportlab.lib.enums import TA_RIGHT as TA_RIGHT
from reportlab.lib.styles import ParagraphStyle as ParagraphStyle
from reportlab.lib.styles import _baseFontName as _baseFontName
from reportlab.lib.styles import _baseFontNameI as _baseFontNameI
from reportlab.lib.units import inch as inch
from reportlab.lib.utils import recursiveImport as recursiveImport
from reportlab.lib.utils import strTypes as strTypes
from reportlab.lib.validators import isColor as isColor
from reportlab.pdfgen.canvas import Canvas as Canvas
from reportlab.platypus import Flowable as Flowable
from reportlab.platypus import Frame as Frame
from reportlab.platypus import Paragraph as Paragraph

__version__: str
captionStyle: Any

class Figure(Flowable):
    width: Any
    figureHeight: Any
    caption: Any
    captionFont: Any
    captionSize: Any
    captionTextColor: Any
    captionBackColor: Any
    captionGap: Any
    captionAlign: Any
    captionPosition: Any
    _captionData: Any
    captionHeight: int
    background: Any
    border: Any
    spaceBefore: Any
    spaceAfter: Any
    hAlign: Any
    def __init__(
        self,
        width,
        height,
        caption: str = ...,
        captionFont=...,
        captionSize: int = ...,
        background: Any | None = ...,
        captionTextColor=...,
        captionBackColor: Any | None = ...,
        border: Any | None = ...,
        spaceBefore: int = ...,
        spaceAfter: int = ...,
        captionGap: Any | None = ...,
        captionAlign: str = ...,
        captionPosition: str = ...,
        hAlign: str = ...,
    ) -> None: ...
    captionPara: Any
    captionStyle: Any
    def _getCaptionPara(self) -> None: ...
    height: Any
    dx: Any
    def wrap(self, availWidth, availHeight): ...
    def draw(self) -> None: ...
    def drawBorder(self) -> None: ...
    def _doBackground(self, color) -> None: ...
    def drawBackground(self) -> None: ...
    def drawCaption(self) -> None: ...
    def drawFigure(self) -> None: ...

def drawPage(canvas, x, y, width, height) -> None: ...

class PageFigure(Figure):
    caption: str
    captionStyle: Any
    background: Any
    def __init__(self, background: Any | None = ...) -> None: ...
    def drawVirtualPage(self) -> None: ...
    def drawFigure(self) -> None: ...

class PlatPropFigure1(PageFigure):
    caption: str
    def __init__(self) -> None: ...
    def drawVirtualPage(self) -> None: ...

class FlexFigure(Figure):
    shrinkToFit: Any
    growToFit: Any
    scaleFactor: Any
    _scaleFactor: Any
    background: Any
    def __init__(
        self,
        width,
        height,
        caption,
        background: Any | None = ...,
        captionFont: str = ...,
        captionSize: int = ...,
        captionTextColor=...,
        shrinkToFit: int = ...,
        growToFit: int = ...,
        spaceBefore: int = ...,
        spaceAfter: int = ...,
        captionGap: int = ...,
        captionAlign: str = ...,
        captionPosition: str = ...,
        scaleFactor: Any | None = ...,
        hAlign: str = ...,
        border: int = ...,
    ) -> None: ...
    width: Any
    figureHeight: Any
    def _scale(self, availWidth, availHeight) -> None: ...
    def wrap(self, availWidth, availHeight): ...
    def split(self, availWidth, availHeight): ...

class ImageFigure(FlexFigure):
    filename: Any
    def __init__(
        self,
        filename,
        caption,
        background: Any | None = ...,
        scaleFactor: Any | None = ...,
        hAlign: str = ...,
        border: Any | None = ...,
    ) -> None: ...
    def drawFigure(self) -> None: ...

class DrawingFigure(FlexFigure):
    drawing: Any
    growToFit: int
    def __init__(
        self,
        modulename,
        classname,
        caption,
        baseDir: Any | None = ...,
        background: Any | None = ...,
    ) -> None: ...
    def drawFigure(self) -> None: ...

_hasPageCatcher: int

class PageCatcherCachingMixIn:
    def getFormName(self, pdfFileName, pageNo): ...
    def needsProcessing(self, pdfFileName, pageNo): ...
    def processPDF(self, pdfFileName, pageNo): ...

class cachePageCatcherFigureNonA4(FlexFigure, PageCatcherCachingMixIn):
    dirname: Any
    pageNo: Any
    formName: Any
    def __init__(
        self, filename, pageNo, caption, width, height, background: Any | None = ...
    ) -> None: ...
    def drawFigure(self) -> None: ...

class cachePageCatcherFigure(cachePageCatcherFigureNonA4):
    def __init__(
        self,
        filename,
        pageNo,
        caption,
        width: int = ...,
        height: int = ...,
        background: Any | None = ...,
    ) -> None: ...

class PageCatcherFigureNonA4(FlexFigure):
    _cache: Any
    pageNo: Any
    prefix: Any
    formName: Any
    caching: Any
    def __init__(
        self,
        filename,
        pageNo,
        caption,
        width,
        height,
        background: Any | None = ...,
        caching: Any | None = ...,
    ) -> None: ...
    def drawFigure(self) -> None: ...

class PageCatcherFigure(PageCatcherFigureNonA4):
    def __init__(
        self,
        filename,
        pageNo,
        caption,
        width: int = ...,
        height: int = ...,
        background: Any | None = ...,
        caching: Any | None = ...,
    ) -> None: ...

def demo1(canvas) -> None: ...
def test1() -> None: ...
