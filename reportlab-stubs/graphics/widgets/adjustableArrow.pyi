from typing import Any

from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Polygon as Polygon
from reportlab.graphics.shapes import _DrawingEditorMixin as _DrawingEditorMixin
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import *
from reportlab.lib.validators import *

class AdjustableArrow(Widget):
    _attrMap: Any
    def __init__(self, **kwds) -> None: ...
    def draw(self): ...

class AdjustableArrowDrawing(_DrawingEditorMixin, Drawing):
    def __init__(self, width: int = ..., height: int = ..., *args, **kw) -> None: ...
