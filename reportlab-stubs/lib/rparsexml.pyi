from typing import Any

RequirePyRXP: int
simpleparse: int

def warnCB(s) -> None: ...

pyRXP_parser: Any

def parsexml(
    xmlText,
    oneOutermostTag: int = ...,
    eoCB: Any | None = ...,
    entityReplacer: Any | None = ...,
    parseOpts=...,
): ...

NONAME: str
NAMEKEY: int
CONTENTSKEY: int
CDATAMARKER: str
LENCDATAMARKER: Any
CDATAENDMARKER: str
replacelist: Any

def unEscapeContentList(contentList): ...
def parsexmlSimple(
    xmltext, oneOutermostTag: int = ..., eoCB: Any | None = ..., entityReplacer=...
): ...

parsexml = parsexmlSimple

def parseFile(filename): ...

verbose: int

def skip_prologue(text, cursor): ...
def parsexml0(
    xmltext, startingat: int = ..., toplevel: int = ..., entityReplacer=...
): ...
def pprettyprint(parsedxml): ...

dump: int

def testparse(s) -> None: ...
def test() -> None: ...

filenames: Any
