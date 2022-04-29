from typing import Any

from reportlab.graphics.charts.piecharts import AbstractPieChart as AbstractPieChart
from reportlab.graphics.charts.piecharts import WedgeProperties as WedgeProperties
from reportlab.graphics.charts.piecharts import _addWedgeLabel as _addWedgeLabel
from reportlab.graphics.charts.piecharts import fixLabelOverlaps as fixLabelOverlaps
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Wedge as Wedge
from reportlab.graphics.widgetbase import (
    TypedPropertyCollection as TypedPropertyCollection,
)
from reportlab.lib import colors as colors
from reportlab.lib.attrmap import *
from reportlab.lib.validators import EitherOr as EitherOr
from reportlab.lib.validators import OneOf as OneOf
from reportlab.lib.validators import isBoolean as isBoolean
from reportlab.lib.validators import (
    isListOfListOfNoneOrNumber as isListOfListOfNoneOrNumber,
)
from reportlab.lib.validators import isListOfNoneOrNumber as isListOfNoneOrNumber
from reportlab.lib.validators import isListOfStringsOrNone as isListOfStringsOrNone
from reportlab.lib.validators import isNumber as isNumber
from reportlab.lib.validators import isNumberOrNone as isNumberOrNone

__version__: str
__doc__: str

class SectorProperties(WedgeProperties):
    _attrMap: Any

class Doughnut(AbstractPieChart):
    _attrMap: Any
    x: int
    y: int
    width: int
    height: int
    data: Any
    labels: Any
    startAngle: int
    direction: str
    simpleLabels: int
    checkLabelOverlap: int
    sideLabels: int
    innerRadiusFraction: Any
    slices: Any
    def __init__(self) -> None: ...
    def demo(self): ...
    def normalizeData(self, data: Any | None = ...): ...
    _seriesCount: Any
    def makeSectors(self): ...
    def draw(self): ...

def sample1(): ...
def sample2(): ...
def sample3(): ...
def sample4(): ...
