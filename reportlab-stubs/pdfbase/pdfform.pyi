from typing import Any

from reportlab.lib.colors import obj_R_G_B as obj_R_G_B
from reportlab.pdfbase.pdfdoc import PDFDictionary as PDFDictionary
from reportlab.pdfbase.pdfdoc import PDFName as PDFName
from reportlab.pdfbase.pdfdoc import PDFObject as PDFObject
from reportlab.pdfbase.pdfdoc import PDFStream as PDFStream
from reportlab.pdfbase.pdfdoc import PDFString as PDFString
from reportlab.pdfbase.pdfpattern import PDFPattern as PDFPattern
from reportlab.pdfbase.pdfpattern import PDFPatternIf as PDFPatternIf
from reportlab.rl_config import register_reset as register_reset

def textFieldAbsolute(
    canvas,
    title,
    x,
    y,
    width,
    height,
    value: str = ...,
    maxlen: int = ...,
    multiline: int = ...,
): ...
def textFieldRelative(
    canvas,
    title,
    xR,
    yR,
    width,
    height,
    value: str = ...,
    maxlen: int = ...,
    multiline: int = ...,
): ...
def buttonFieldAbsolute(
    canvas, title, value, x, y, width: float = ..., height: float = ...
): ...
def buttonFieldRelative(
    canvas, title, value, xR, yR, width: float = ..., height: float = ...
): ...
def selectFieldAbsolute(canvas, title, value, options, x, y, width, height) -> None: ...
def selectFieldRelative(canvas, title, value, options, xR, yR, width, height): ...
def getForm(canvas): ...

class AcroForm(PDFObject):
    fields: Any
    def __init__(self) -> None: ...
    def textField(
        self,
        canvas,
        title,
        xmin,
        ymin,
        xmax,
        ymax,
        value: str = ...,
        maxlen: int = ...,
        multiline: int = ...,
    ) -> None: ...
    def selectField(
        self, canvas, title, value, options, xmin, ymin, xmax, ymax
    ) -> None: ...
    def buttonField(
        self, canvas, title, value, xmin, ymin, width: float = ..., height: float = ...
    ) -> None: ...
    def format(self, document): ...

FormPattern: Any

def FormFontsDictionary(): ...
def FormResources(): ...

ZaDbPattern: Any
FormResourcesDictionaryPattern: Any
FORMFONTNAMES: Any
EncodingPattern: Any
PDFDocEncodingPattern: Any

def FormFont(BaseFont, Name): ...

FormFontPattern: Any

def resetPdfForm() -> None: ...
def TextField(
    title,
    value,
    xmin,
    ymin,
    xmax,
    ymax,
    page,
    maxlen: int = ...,
    font: str = ...,
    fontsize: int = ...,
    R: int = ...,
    G: int = ...,
    B: float = ...,
    multiline: int = ...,
): ...

TextFieldPattern: Any

def SelectField(
    title,
    value,
    options,
    xmin,
    ymin,
    xmax,
    ymax,
    page,
    font: str = ...,
    fontsize: int = ...,
    R: int = ...,
    G: int = ...,
    B: float = ...,
): ...

SelectFieldPattern: Any

def ButtonField(
    title, value, xmin, ymin, page, width: float = ..., height: float = ...
): ...

ButtonFieldPattern: Any

def buttonStreamDictionary(width: float = ..., height: float = ...): ...
def ButtonStream(content, width: float = ..., height: float = ...): ...
