from collections.abc import Generator
from typing import Any

unicode = str

class QR:
    valid: Any
    bits: Any
    group: int
    data: Any
    def __init__(self, data) -> None: ...
    def __len__(self): ...
    @property
    def bitlength(self): ...
    def getLengthBits(self, ver): ...
    def getLength(self): ...
    def __repr__(self): ...
    def write_header(self, buffer, version) -> None: ...
    def write(self, buffer, version) -> None: ...

class QRNumber(QR):
    valid: Any
    chars: str
    bits: Any
    group: int
    mode: int
    lengthbits: Any

class QRAlphaNum(QR):
    valid: Any
    chars: str
    bits: Any
    group: int
    mode: int
    lengthbits: Any

class QR8bitByte(QR):
    bits: Any
    group: int
    mode: int
    lengthbits: Any
    data: Any
    def __init__(self, data) -> None: ...
    def write(self, buffer, version) -> None: ...

class QRKanji(QR):
    bits: Any
    group: int
    mode: int
    lengthbits: Any
    data: Any
    def __init__(self, data) -> None: ...
    def unicode_to_qrkanji(self, data): ...
    def write(self, buffer, version) -> None: ...

class QRHanzi(QR):
    bits: Any
    group: int
    mode: int
    lengthbits: Any
    data: Any
    def __init__(self, data) -> None: ...
    def unicode_to_qrhanzi(self, data): ...
    def write_header(self, buffer, version) -> None: ...
    def write(self, buffer, version) -> None: ...

class QRECI(QR):
    mode: int
    lengthbits: Any
    data: Any
    def __init__(self, data) -> None: ...
    def write(self, buffer, version) -> None: ...

class QRStructAppend(QR):
    mode: int
    lengthbits: Any
    part: Any
    total: Any
    parity: Any
    def __init__(self, part, total, parity) -> None: ...
    def write(self, buffer, version) -> None: ...

class QRFNC1First(QR):
    mode: int
    lengthbits: Any
    def __init__(self) -> None: ...
    def write(self, buffer, version) -> None: ...

class QRFNC1Second(QR):
    valid: Any
    mode: int
    lengthbits: Any
    def write(self, buffer, version) -> None: ...

class QRCode:
    version: Any
    errorCorrectLevel: Any
    modules: Any
    moduleCount: int
    dataCache: Any
    dataList: Any
    def __init__(self, version, errorCorrectLevel) -> None: ...
    def addData(self, data) -> None: ...
    def isDark(self, row, col): ...
    def getModuleCount(self): ...
    def calculate_version(self): ...
    def make(self) -> None: ...
    def makeImpl(self, test, maskPattern) -> None: ...
    _positionProbePattern: Any
    def setupPositionProbePattern(self, row, col) -> None: ...
    def getBestMaskPattern(self): ...
    def setupTimingPattern(self) -> None: ...
    _positionAdjustPattern: Any
    def setupPositionAdjustPattern(self) -> None: ...
    def setupTypeNumber(self, test) -> None: ...
    def setupTypeInfo(self, test, maskPattern) -> None: ...
    def _dataPosIterator(self) -> Generator[Any, None, None]: ...
    _dataPosList: Any
    def dataPosIterator(self): ...
    def _dataBitIterator(self, data) -> Generator[Any, None, None]: ...
    _dataBitList: Any
    def dataBitIterator(self, data): ...
    def mapData(self, data, maskPattern) -> None: ...
    PAD0: int
    PAD1: int
    @staticmethod
    def createData(version, errorCorrectLevel, dataList): ...
    @staticmethod
    def createBytes(buffer, rsBlocks): ...

class QRErrorCorrectLevel:
    L: int
    M: int
    Q: int
    H: int

class QRMaskPattern:
    PATTERN000: int
    PATTERN001: int
    PATTERN010: int
    PATTERN011: int
    PATTERN100: int
    PATTERN101: int
    PATTERN110: int
    PATTERN111: int

class QRUtil:
    PATTERN_POSITION_TABLE: Any
    G15: Any
    G18: Any
    G15_MASK: Any
    @staticmethod
    def getBCHTypeInfo(data): ...
    @staticmethod
    def getBCHTypeNumber(data): ...
    @staticmethod
    def getBCHDigit(data): ...
    @staticmethod
    def getPatternPosition(version): ...
    maskPattern: Any
    @classmethod
    def getMask(cls, maskPattern): ...
    @staticmethod
    def getErrorCorrectPolynomial(errorCorrectLength): ...
    @classmethod
    def maskScoreRule1vert(cls, modules): ...
    @classmethod
    def maskScoreRule2(cls, modules): ...
    @classmethod
    def maskScoreRule3hor(cls, modules, pattern=...): ...
    @classmethod
    def maskScoreRule4(cls, modules): ...
    @classmethod
    def getLostPoint(cls, qrCode): ...

class QRMath:
    @staticmethod
    def glog(n): ...
    @staticmethod
    def gexp(n): ...

EXP_TABLE: Any
LOG_TABLE: Any

class QRPolynomial:
    num: Any
    def __init__(self, num, shift) -> None: ...
    def get(self, index): ...
    def getLength(self): ...
    def multiply(self, e): ...
    def mod(self, e): ...

class QRRSBlock:
    RS_BLOCK_TABLE: Any
    totalCount: Any
    dataCount: Any
    def __init__(self, totalCount, dataCount) -> None: ...
    @staticmethod
    def getRSBlocks(version, errorCorrectLevel): ...
    @staticmethod
    def getRsBlockTable(version, errorCorrectLevel): ...

class QRBitBuffer:
    buffer: Any
    length: int
    def __init__(self) -> None: ...
    def __repr__(self): ...
    def get(self, index): ...
    def put(self, num, length) -> None: ...
    def getLengthInBits(self): ...
    def putBit(self, bit) -> None: ...
