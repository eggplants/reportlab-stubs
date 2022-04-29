from typing import Any

from reportlab import rl_config as rl_config
from reportlab.lib.utils import isSeq as isSeq
from reportlab.lib.validators import DerivedValue as DerivedValue
from reportlab.lib.validators import isAnything as isAnything

__version__: str
__doc__: str

class CallableValue:
    func: Any
    args: Any
    kw: Any
    def __init__(self, func, *args, **kw) -> None: ...
    def __call__(self): ...

class AttrMapValue:
    validate: Any
    desc: Any
    _initial: Any
    _advancedUsage: Any
    def __init__(
        self,
        validate: Any | None = ...,
        desc: Any | None = ...,
        initial: Any | None = ...,
        advancedUsage: int = ...,
        **kw
    ) -> None: ...
    def __getattr__(self, name): ...
    def __repr__(self): ...

class AttrMap(dict):
    def __init__(self, BASE: Any | None = ..., UNWANTED=..., **kw) -> None: ...
    def remove(self, unwanted) -> None: ...
    def clone(self, UNWANTED=..., **kw): ...

def validateSetattr(obj, name, value) -> None: ...
def _privateAttrMap(obj, ret: int = ...): ...
def _findObjectAndAttr(src, P): ...
def hook__setattr__(obj): ...
def addProxyAttribute(
    src,
    name,
    validate: Any | None = ...,
    desc: Any | None = ...,
    initial: Any | None = ...,
    dst: Any | None = ...,
) -> None: ...
