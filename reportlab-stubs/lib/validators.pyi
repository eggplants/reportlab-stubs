import re
from typing import Any

from reportlab.lib import colors as colors
from reportlab.lib.normalDate import NormalDate as NormalDate
from reportlab.lib.utils import isBytes as isBytes
from reportlab.lib.utils import isSeq as isSeq
from reportlab.lib.utils import isStr as isStr

__version__: str
__doc__: str
_re_Pattern = re.Pattern

class Percentage(float): ...

class Validator:
    def __call__(self, x): ...
    def __str__(self): ...
    def normalize(self, x): ...
    def normalizeTest(self, x): ...

class _isAnything(Validator):
    def test(self, x): ...

class _isNothing(Validator):
    def test(self, x): ...

class _isBoolean(Validator):
    def test(self, x): ...
    def normalize(self, x): ...

class _isString(Validator):
    def test(self, x): ...

class _isCodec(Validator):
    def test(self, x): ...

class _isNumber(Validator):
    def test(self, x): ...
    def normalize(self, x): ...

class _isInt(Validator):
    def test(self, x): ...
    def normalize(self, x): ...

class _isNumberOrNone(_isNumber):
    def test(self, x): ...
    def normalize(self, x): ...

class _isListOfNumbersOrNone(Validator):
    def test(self, x): ...

class isNumberInRange(_isNumber):
    min: Any
    max: Any
    def __init__(self, min, max) -> None: ...
    def test(self, x): ...

class _isListOfShapes(Validator):
    def test(self, x): ...

class _isListOfStringsOrNone(Validator):
    def test(self, x): ...

class _isTransform(Validator):
    def test(self, x): ...

class _isColor(Validator):
    def test(self, x): ...

class _isColorOrNone(Validator):
    def test(self, x): ...

class _isNormalDate(Validator):
    def test(self, x): ...
    def normalize(self, x): ...

class _isValidChild(Validator):
    def test(self, x): ...

class _isValidChildOrNone(_isValidChild):
    def test(self, x): ...

class _isCallable(Validator):
    def test(self, x): ...

class OneOf(Validator):
    _enum: Any
    _patterns: Any
    def __init__(self, enum, *args) -> None: ...
    def test(self, x): ...
    def _test_patterns(self, x): ...

class SequenceOf(Validator):
    _elemTest: Any
    _emptyOK: Any
    _NoneOK: Any
    _str: Any
    def __init__(
        self,
        elemTest,
        name: Any | None = ...,
        emptyOK: int = ...,
        NoneOK: int = ...,
        lo: int = ...,
        hi: int = ...,
    ) -> None: ...
    def test(self, x): ...

class EitherOr(Validator):
    _tests: Any
    _str: Any
    def __init__(self, tests, name: Any | None = ...) -> None: ...
    def test(self, x): ...

class NoneOr(EitherOr):
    def test(self, x): ...

class NotSetOr(EitherOr):
    _not_set: Any
    def test(self, x): ...
    @staticmethod
    def conditionalValue(v, a): ...

class _isNotSet(Validator):
    def test(self, x): ...

class Auto(Validator):
    def __init__(self, **kw) -> None: ...
    def test(self, x): ...

class AutoOr(EitherOr):
    def test(self, x): ...

class isInstanceOf(Validator):
    _klass: Any
    def __init__(self, klass: Any | None = ...) -> None: ...
    def test(self, x): ...

class isSubclassOf(Validator):
    _klass: Any
    def __init__(self, klass: Any | None = ...) -> None: ...
    def test(self, x): ...

class matchesPattern(Validator):
    _pattern: Any
    def __init__(self, pattern) -> None: ...
    def test(self, x): ...

class DerivedValue:
    def getValue(self, renderer, attr) -> None: ...

class Inherit(DerivedValue):
    def __repr__(self): ...
    def getValue(self, renderer, attr): ...

inherit: Any

class NumericAlign(str):
    _dp: Any
    _dpLen: Any
    def __new__(cls, dp: str = ..., dpLen: int = ...): ...

isAuto: Any
isBoolean: Any
isString: Any
isCodec: Any
isNumber: Any
isInt: Any
isNoneOrInt: Any
isNumberOrNone: Any
isTextAnchor: Any
isListOfNumbers: Any
isListOfNoneOrNumber: Any
isListOfListOfNoneOrNumber: Any
isListOfNumbersOrNone: Any
isListOfShapes: Any
isListOfStrings: Any
isListOfStringsOrNone: Any
isTransform: Any
isColor: Any
isListOfColors: Any
isColorOrNone: Any
isShape: Any
isValidChild: Any
isNoneOrShape: Any
isValidChildOrNone: Any
isAnything: Any
isNothing: Any
isXYCoord: Any
isBoxAnchor: Any
isNoneOrString: Any
isNoneOrListOfNoneOrStrings: Any
isListOfNoneOrString: Any
isNoneOrListOfNoneOrNumbers: Any
isCallable: Any
isNoneOrCallable: Any
isStringOrCallable: Any
isStringOrCallableOrNone: Any
isStringOrNone: Any
isNormalDate: Any
isNotSet: Any
