from typing import Any

from reportlab.lib.units import inch as inch
from reportlab.lib.units import mm as mm

__version__: str
A0: Any
A1: Any
A2: Any
A3: Any
A4: Any
A5: Any
A6: Any
A7: Any
A8: Any
A9: Any
A10: Any
B0: Any
B1: Any
B2: Any
B3: Any
B4: Any
B5: Any
B6: Any
B7: Any
B8: Any
B9: Any
B10: Any
C0: Any
C1: Any
C2: Any
C3: Any
C4: Any
C5: Any
C6: Any
C7: Any
C8: Any
C9: Any
C10: Any
LETTER: Any
LEGAL: Any
ELEVENSEVENTEEN: Any
JUNIOR_LEGAL: Any
HALF_LETTER: Any
GOV_LETTER: Any
GOV_LEGAL: Any
TABLOID = ELEVENSEVENTEEN
LEDGER: Any
letter = LETTER
legal = LEGAL
elevenSeventeen = ELEVENSEVENTEEN

def landscape(pagesize): ...
def portrait(pagesize): ...
