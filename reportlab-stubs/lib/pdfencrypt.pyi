import os
from typing import Any

from reportlab import rl_config as rl_config
from reportlab.lib.utils import asBytes as asBytes
from reportlab.lib.utils import asNative as asNative
from reportlab.lib.utils import int2Byte as int2Byte
from reportlab.lib.utils import md5 as md5
from reportlab.lib.utils import rawBytes as rawBytes
from reportlab.pdfbase.pdfdoc import PDFObject as PDFObject
from reportlab.pdfgen.canvas import Canvas as Canvas
from reportlab.platypus.flowables import Flowable as Flowable

__version__: str

def xorKey(num, key): ...

CLOBBERID: int
CLOBBERPERMISSIONS: int
DEBUG: Any
reserved1: int
reserved2: Any
printable: Any
modifiable: Any
copypastable: Any
annotatable: Any
higherbits: int
_os_random_x: int
_os_random_b: bytes

def os_urandom(n): ...

os_urandom = os.urandom

class StandardEncryption:
    prepared: int
    userPassword: Any
    ownerPassword: Any
    revision: int
    canPrint: Any
    canModify: Any
    canCopy: Any
    canAnnotate: Any
    O: Any
    def __init__(
        self,
        userPassword,
        ownerPassword: Any | None = ...,
        canPrint: int = ...,
        canModify: int = ...,
        canCopy: int = ...,
        canAnnotate: int = ...,
        strength: Any | None = ...,
    ) -> None: ...
    def setAllPermissions(self, value) -> None: ...
    def permissionBits(self): ...
    def encode(self, t): ...
    P: Any
    key: Any
    U: Any
    UE: Any
    OE: Any
    Perms: Any
    objnum: Any
    def prepare(self, document, overrideID: Any | None = ...) -> None: ...
    version: Any
    def register(self, objnum, version) -> None: ...
    def info(self): ...

class StandardEncryptionDictionary(PDFObject):
    __RefOnly__: int
    revision: Any
    def __init__(self, O, OE, U, UE, P, Perms, revision) -> None: ...
    def format(self, document): ...

padding: str

def hexText(text): ...
def unHexText(hexText): ...

PadString: Any

def checkRevision(revision): ...
def encryptionkey(
    password, OwnerKey, Permissions, FileId1, revision: Any | None = ...
): ...
def computeO(userPassword, ownerPassword, revision): ...
def computeU(
    encryptionkey,
    encodestring=...,
    revision: Any | None = ...,
    documentId: Any | None = ...,
): ...
def checkU(encryptionkey, U) -> None: ...
def encodePDF(
    key, objectNumber, generationNumber, string, revision: Any | None = ...
): ...
def equalityCheck(observed, expected, label) -> None: ...
def test() -> None: ...
def encryptCanvas(
    canvas,
    userPassword,
    ownerPassword: Any | None = ...,
    canPrint: int = ...,
    canModify: int = ...,
    canCopy: int = ...,
    canAnnotate: int = ...,
    strength: int = ...,
) -> None: ...

class EncryptionFlowable(StandardEncryption, Flowable):
    def wrap(self, availWidth, availHeight): ...
    def draw(self) -> None: ...

def encryptDocTemplate(
    dt,
    userPassword,
    ownerPassword: Any | None = ...,
    canPrint: int = ...,
    canModify: int = ...,
    canCopy: int = ...,
    canAnnotate: int = ...,
    strength: int = ...,
) -> None: ...
def encryptPdfInMemory(
    inputPDF,
    userPassword,
    ownerPassword: Any | None = ...,
    canPrint: int = ...,
    canModify: int = ...,
    canCopy: int = ...,
    canAnnotate: int = ...,
    strength: int = ...,
): ...
def encryptPdfOnDisk(
    inputFileName,
    outputFileName,
    userPassword,
    ownerPassword: Any | None = ...,
    canPrint: int = ...,
    canModify: int = ...,
    canCopy: int = ...,
    canAnnotate: int = ...,
    strength: int = ...,
): ...
def scriptInterp() -> None: ...
def main() -> None: ...
