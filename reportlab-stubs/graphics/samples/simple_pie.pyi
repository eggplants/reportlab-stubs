from typing import Any

from reportlab.graphics.charts.legends import Legend as Legend
from reportlab.graphics.charts.piecharts import Pie as Pie
from reportlab.graphics.charts.textlabels import Label as Label
from reportlab.graphics.samples.excelcolors import *
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import _DrawingEditorMixin as _DrawingEditorMixin
from reportlab.graphics.widgets.grids import ShadedRect as ShadedRect

class SimplePie(_DrawingEditorMixin, Drawing):
    background: Any
    def __init__(self, width: int = ..., height: int = ..., *args, **kw) -> None: ...
