from typing import Any

__version__: str
__doc__: str

def replace(src, sep, rep): ...

keywordsList: Any
commentPat: str
pat: str
quotePat: Any
tripleQuotePat: Any
nonKeyPat: str
keyPat: Any
matchPat: Any
matchRE: Any
idKeyPat: str
idRE: Any

def fontify(pytext, searchfrom: int = ..., searchto: Any | None = ...): ...
def test(path) -> None: ...
