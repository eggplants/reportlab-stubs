from reportlab.graphics.charts.barcharts import VerticalBarChart as VerticalBarChart
from reportlab.graphics.charts.legends import Legend as Legend
from reportlab.graphics.charts.textlabels import Label as Label
from reportlab.graphics.samples.excelcolors import *
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import _DrawingEditorMixin as _DrawingEditorMixin

class StackedColumn(_DrawingEditorMixin, Drawing):
    def __init__(self, width: int = ..., height: int = ..., *args, **kw) -> None: ...
