from typing import Any

__version__: str
__doc__: str
_family_alias: Any
_tt2ps_map: Any
_ps2tt_map: Any
v: Any

def ps2tt(psfn): ...
def tt2ps(fn, b, i): ...
def addMapping(face, bold, italic, psname) -> None: ...
