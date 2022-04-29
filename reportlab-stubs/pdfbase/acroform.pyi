from typing import Any

from reportlab.pdfbase.pdfdoc import PDFObject

class PDFFromString(PDFObject):
    _s: Any
    def __init__(self, s) -> None: ...
    def format(self, document): ...

class RadioGroup(PDFObject):
    TU: Any
    Ff: Any
    kids: Any
    T: Any
    V: Any
    def __init__(self, name, tooltip: str = ..., fieldFlags: str = ...) -> None: ...
    def format(self, doc): ...

class AcroForm(PDFObject):
    formFontNames: Any
    referenceMap: Any
    _canv: Any
    fonts: Any
    fields: Any
    _radios: Any
    _refMap: Any
    _pdfdocenc: Any
    sigFlags: Any
    extras: Any
    def __init__(self, canv, **kwds) -> None: ...
    @property
    def canv(self): ...
    def fontRef(self, f): ...
    def format(self, doc): ...
    def colorTuple(self, c): ...
    def streamFillColor(self, c): ...
    def streamStrokeColor(self, c): ...
    def checkboxAP(
        self,
        key,
        value,
        buttonStyle: str = ...,
        shape: str = ...,
        fillColor: Any | None = ...,
        borderColor: Any | None = ...,
        textColor: Any | None = ...,
        borderWidth: int = ...,
        borderStyle: str = ...,
        size: int = ...,
        dashLen: int = ...,
    ): ...
    @staticmethod
    def circleArcStream(size, r, arcs=..., rotated: bool = ...): ...
    def zdMark(self, c, size, ds, iFontName): ...
    def getRef(self, obj): ...
    def getRefStr(self, obj): ...
    @staticmethod
    def stdColors(t, b, f): ...
    @staticmethod
    def varyColors(key, t, b, f): ...
    def checkForceBorder(
        self,
        x,
        y,
        width,
        height,
        forceBorder,
        shape,
        borderStyle,
        borderWidth,
        borderColor,
        fillColor,
    ) -> None: ...
    def checkbox(
        self,
        checked: bool = ...,
        buttonStyle: str = ...,
        shape: str = ...,
        fillColor: Any | None = ...,
        borderColor: Any | None = ...,
        textColor: Any | None = ...,
        borderWidth: int = ...,
        borderStyle: str = ...,
        size: int = ...,
        x: int = ...,
        y: int = ...,
        tooltip: Any | None = ...,
        name: Any | None = ...,
        annotationFlags: str = ...,
        fieldFlags: str = ...,
        forceBorder: bool = ...,
        relative: bool = ...,
        dashLen: int = ...,
    ) -> None: ...
    def radio(
        self,
        value: Any | None = ...,
        selected: bool = ...,
        buttonStyle: str = ...,
        shape: str = ...,
        fillColor: Any | None = ...,
        borderColor: Any | None = ...,
        textColor: Any | None = ...,
        borderWidth: int = ...,
        borderStyle: str = ...,
        size: int = ...,
        x: int = ...,
        y: int = ...,
        tooltip: Any | None = ...,
        name: Any | None = ...,
        annotationFlags: str = ...,
        fieldFlags: str = ...,
        forceBorder: bool = ...,
        relative: bool = ...,
        dashLen: int = ...,
    ) -> None: ...
    def makeStream(self, width, height, stream, **D): ...
    def txAP(
        self,
        key,
        value,
        iFontName,
        rFontName,
        fontSize,
        shape: str = ...,
        fillColor: Any | None = ...,
        borderColor: Any | None = ...,
        textColor: Any | None = ...,
        borderWidth: int = ...,
        borderStyle: str = ...,
        width: int = ...,
        height: int = ...,
        dashLen: int = ...,
        wkind: str = ...,
        labels=...,
        I=...,
        sel_bg: str = ...,
        sel_fg: str = ...,
    ): ...
    def makeFont(self, fontName): ...
    def _textfield(
        self,
        value: str = ...,
        fillColor: Any | None = ...,
        borderColor: Any | None = ...,
        textColor: Any | None = ...,
        borderWidth: int = ...,
        borderStyle: str = ...,
        width: int = ...,
        height: int = ...,
        x: int = ...,
        y: int = ...,
        tooltip: Any | None = ...,
        name: Any | None = ...,
        annotationFlags: str = ...,
        fieldFlags: str = ...,
        forceBorder: bool = ...,
        relative: bool = ...,
        maxlen: int = ...,
        fontName: Any | None = ...,
        fontSize: Any | None = ...,
        wkind: Any | None = ...,
        options: Any | None = ...,
        dashLen: int = ...,
    ) -> None: ...
    def textfield(
        self,
        value: str = ...,
        fillColor: Any | None = ...,
        borderColor: Any | None = ...,
        textColor: Any | None = ...,
        borderWidth: int = ...,
        borderStyle: str = ...,
        width: int = ...,
        height: int = ...,
        x: int = ...,
        y: int = ...,
        tooltip: Any | None = ...,
        name: Any | None = ...,
        annotationFlags: str = ...,
        fieldFlags: str = ...,
        forceBorder: bool = ...,
        relative: bool = ...,
        maxlen: int = ...,
        fontName: Any | None = ...,
        fontSize: Any | None = ...,
        dashLen: int = ...,
    ): ...
    def listbox(
        self,
        value: str = ...,
        fillColor: Any | None = ...,
        borderColor: Any | None = ...,
        textColor: Any | None = ...,
        borderWidth: int = ...,
        borderStyle: str = ...,
        width: int = ...,
        height: int = ...,
        x: int = ...,
        y: int = ...,
        tooltip: Any | None = ...,
        name: Any | None = ...,
        annotationFlags: str = ...,
        fieldFlags: str = ...,
        forceBorder: bool = ...,
        relative: bool = ...,
        fontName: Any | None = ...,
        fontSize: Any | None = ...,
        dashLen: int = ...,
        maxlen: Any | None = ...,
        options=...,
    ): ...
    def choice(
        self,
        value: str = ...,
        fillColor: Any | None = ...,
        borderColor: Any | None = ...,
        textColor: Any | None = ...,
        borderWidth: int = ...,
        borderStyle: str = ...,
        width: int = ...,
        height: int = ...,
        x: int = ...,
        y: int = ...,
        tooltip: Any | None = ...,
        name: Any | None = ...,
        annotationFlags: str = ...,
        fieldFlags: str = ...,
        forceBorder: bool = ...,
        relative: bool = ...,
        fontName: Any | None = ...,
        fontSize: Any | None = ...,
        dashLen: int = ...,
        maxlen: Any | None = ...,
        options=...,
    ): ...
    def checkboxRelative(self, **kwds) -> None: ...
    def radioRelative(self, **kwds) -> None: ...
    def textfieldRelative(self, **kwds) -> None: ...
    def listboxRelative(self, **kwds) -> None: ...
    def choiceRelative(self, **kwds) -> None: ...
    @property
    def encRefStr(self): ...

class CBMark:
    opNames: Any
    opCount: Any
    ops: Any
    points: Any
    slack: Any
    def __init__(self, ops, points, bounds, slack: float = ...) -> None: ...
    def scaledRender(self, size, ds: int = ...): ...
