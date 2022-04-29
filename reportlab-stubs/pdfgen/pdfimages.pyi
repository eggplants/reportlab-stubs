from typing import Any

from reportlab import rl_config as rl_config
from reportlab.lib.boxstuff import aspectRatioFix as aspectRatioFix
from reportlab.lib.rl_accel import asciiBase85Encode as asciiBase85Encode
from reportlab.lib.rl_accel import fp_str as fp_str
from reportlab.lib.utils import haveImages as haveImages
from reportlab.lib.utils import isStr as isStr
from reportlab.pdfbase import pdfdoc as pdfdoc
from reportlab.pdfbase import pdfutils as pdfutils

__version__: str
__doc__: str

class PDFImage:
    image: Any
    x: Any
    y: Any
    width: Any
    height: Any
    filename: Any
    imageCaching: Any
    colorSpace: str
    bitsPerComponent: int
    filters: Any
    source: Any
    def __init__(
        self,
        image,
        x,
        y,
        width: Any | None = ...,
        height: Any | None = ...,
        caching: int = ...,
    ) -> None: ...
    def jpg_imagedata(self): ...
    def _jpg_imagedata(self, imageFile): ...
    def cache_imagedata(self): ...
    def PIL_imagedata(self): ...
    def non_jpg_imagedata(self, image): ...
    imageData: Any
    imgwidth: Any
    imgheight: Any
    def getImageData(self, preserveAspectRatio: bool = ...) -> None: ...
    def drawInlineImage(
        self,
        canvas,
        preserveAspectRatio: bool = ...,
        anchor: str = ...,
        anchorAtXY: bool = ...,
        showBoundary: bool = ...,
    ): ...
    def format(self, document): ...
