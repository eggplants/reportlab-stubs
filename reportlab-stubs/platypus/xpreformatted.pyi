from typing import Any

from reportlab.platypus.paragraph import Paragraph

class XPreformatted(Paragraph):
    caseSensitive: Any
    def __init__(
        self,
        text,
        style,
        bulletText: Any | None = ...,
        frags: Any | None = ...,
        caseSensitive: int = ...,
        dedent: int = ...,
    ): ...
    _width_max: int
    height: int
    width: Any
    def breakLines(self, width): ...
    breakLinesCJK: Any
    def _get_split_blParaFunc(self): ...

class PythonPreformatted(XPreformatted):
    formats: Any
    def __init__(
        self,
        text,
        style,
        bulletText: Any | None = ...,
        dedent: int = ...,
        frags: Any | None = ...,
    ) -> None: ...
    def escapeHtml(self, text): ...
    def fontify(self, code): ...
