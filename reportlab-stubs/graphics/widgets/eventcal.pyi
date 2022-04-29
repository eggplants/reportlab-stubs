from typing import Any

from reportlab.graphics.charts.textlabels import Label as Label
from reportlab.graphics.shapes import Drawing as Drawing
from reportlab.graphics.shapes import Group as Group
from reportlab.graphics.shapes import Rect as Rect
from reportlab.graphics.shapes import String as String
from reportlab.graphics.widgetbase import Widget as Widget
from reportlab.lib import colors as colors

__version__: str
__doc__: str

class EventCalendar(Widget):
    x: int
    y: int
    width: int
    height: int
    timeColWidth: Any
    trackRowHeight: int
    data: Any
    trackNames: Any
    startTime: Any
    endTime: Any
    day: int
    _talksVisible: Any
    _startTime: Any
    _endTime: Any
    _trackCount: int
    _colWidths: Any
    _colLeftEdges: Any
    def __init__(self) -> None: ...
    def computeSize(self) -> None: ...
    def computeStartAndEndTimes(self) -> None: ...
    def getAllTracks(self): ...
    def getRelevantTalks(self, talkList): ...
    def scaleTime(self, theTime): ...
    def getTalkRect(self, startTime, duration, trackId, text): ...
    def draw(self): ...

def test() -> None: ...
