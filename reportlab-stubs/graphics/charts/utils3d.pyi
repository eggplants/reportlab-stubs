from typing import Any

from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Line as Line
from reportlab.graphics.shapes import Polygon as Polygon

def _getShaded(col, shd: Any | None = ..., shading: float = ...): ...
def _getLit(col, shd: Any | None = ..., lighting: float = ...): ...
def _draw_3d_bar(
    G,
    x1,
    x2,
    y0,
    yhigh,
    xdepth,
    ydepth,
    fillColor: Any | None = ...,
    fillColorShaded: Any | None = ...,
    strokeColor: Any | None = ...,
    strokeWidth: int = ...,
    shading: float = ...,
) -> None: ...

class _YStrip:
    y0: Any
    y1: Any
    slope: Any
    fillColor: Any
    fillColorShaded: Any
    def __init__(
        self, y0, y1, slope, fillColor, fillColorShaded, shading: float = ...
    ) -> None: ...

def _ystrip_poly(x0, x1, y0, y1, xoff, yoff): ...
def _make_3d_line_info(
    G,
    x0,
    x1,
    y0,
    y1,
    z0,
    z1,
    theta_x,
    theta_y,
    fillColor,
    fillColorShaded: Any | None = ...,
    tileWidth: int = ...,
    strokeColor: Any | None = ...,
    strokeWidth: Any | None = ...,
    strokeDashArray: Any | None = ...,
    shading: float = ...,
) -> None: ...

_pi_2: Any
_2pi: Any
_180_pi: Any

def _2rad(angle): ...
def mod_2pi(radians): ...
def _2deg(o): ...
def _360(a): ...

_ZERO: float
_ONE: Any

class _Segment:
    a: Any
    b: Any
    x0: Any
    x1: Any
    y0: Any
    y1: Any
    series: Any
    i: Any
    s: Any
    def __init__(self, s, i, data) -> None: ...
    def __str__(self): ...
    __repr__: Any
    def intersect(self, o, I): ...

def _segKey(a): ...
def find_intersections(data, small: int = ...): ...
