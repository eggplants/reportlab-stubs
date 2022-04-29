from typing import Any

class Formatter:
    pattern: Any
    def __init__(self, pattern) -> None: ...
    def format(self, obj): ...
    def __repr__(self): ...
    def __call__(self, x): ...

class DecimalFormatter(Formatter):
    calcPlaces: Any
    places: Any
    dot: Any
    comma: Any
    prefix: Any
    suffix: Any
    def __init__(
        self,
        places: int = ...,
        decimalSep: str = ...,
        thousandSep: Any | None = ...,
        prefix: Any | None = ...,
        suffix: Any | None = ...,
    ) -> None: ...
    def _calcPlaces(self, V) -> None: ...
    def format(self, num): ...
    def __repr__(self): ...
