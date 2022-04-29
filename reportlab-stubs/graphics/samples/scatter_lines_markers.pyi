from reportlab.graphics.charts.legends import Legend as Legend
from reportlab.graphics.charts.lineplots import ScatterPlot as ScatterPlot
from reportlab.graphics.charts.textlabels import Label as Label
from reportlab.graphics.samples.excelcolors import *
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import _DrawingEditorMixin as _DrawingEditorMixin

class ScatterLinesMarkers(_DrawingEditorMixin, Drawing):
    def __init__(self, width: int = ..., height: int = ..., *args, **kw) -> None: ...
