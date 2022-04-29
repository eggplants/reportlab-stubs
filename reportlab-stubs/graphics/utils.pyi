from typing import Any

class RenderPMError(Exception): ...

def setFont(gs, fontName, fontSize) -> None: ...
def pathNumTrunc(n): ...
def processGlyph(G, truncate: int = ..., pathReverse: int = ...): ...
def text2PathDescription(
    text,
    x: int = ...,
    y: int = ...,
    fontName=...,
    fontSize: int = ...,
    anchor: str = ...,
    truncate: int = ...,
    pathReverse: int = ...,
    gs: Any | None = ...,
): ...
def text2Path(
    text,
    x: int = ...,
    y: int = ...,
    fontName=...,
    fontSize: int = ...,
    anchor: str = ...,
    truncate: int = ...,
    pathReverse: int = ...,
    gs: Any | None = ...,
    **kwds
): ...
