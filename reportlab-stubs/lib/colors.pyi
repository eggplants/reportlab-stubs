from ast import literal_eval as literal_eval
from collections.abc import Generator
from typing import Any

from reportlab.lib.rl_accel import fp_str as fp_str
from reportlab.lib.utils import asNative as asNative
from reportlab.lib.utils import isStr as isStr
from reportlab.lib.utils import rl_safe_eval as rl_safe_eval

__version__: str
__doc__: str

class Color:
    red: Any
    green: Any
    blue: Any
    alpha: Any
    def __init__(
        self, red: int = ..., green: int = ..., blue: int = ..., alpha: int = ...
    ) -> None: ...
    def __repr__(self): ...
    @property
    def __key__(self): ...
    def __hash__(self): ...
    def __comparable__(self, other): ...
    def __lt__(self, other): ...
    def __eq__(self, other): ...
    def rgb(self): ...
    def rgba(self): ...
    def bitmap_rgb(self): ...
    def bitmap_rgba(self): ...
    def hexval(self): ...
    def hexvala(self): ...
    def int_rgb(self): ...
    def int_rgba(self): ...
    _cKwds: Any
    def cKwds(self) -> Generator[Any, None, None]: ...
    cKwds: Any
    def clone(self, **kwds): ...
    def _lookupName(self, D=...): ...
    @property
    def normalizedAlpha(self): ...

def opaqueColor(c): ...

class CMYKColor(Color):
    _scale: float
    cyan: Any
    magenta: Any
    yellow: Any
    black: Any
    spotName: Any
    density: Any
    knockout: Any
    alpha: Any
    def __init__(
        self,
        cyan: int = ...,
        magenta: int = ...,
        yellow: int = ...,
        black: int = ...,
        spotName: Any | None = ...,
        density: int = ...,
        knockout: Any | None = ...,
        alpha: int = ...,
    ) -> None: ...
    def __repr__(self): ...
    def fader(self, n, reverse: bool = ...): ...
    @property
    def __key__(self): ...
    def __comparable__(self, other): ...
    def cmyk(self): ...
    def cmyka(self): ...
    def _density_str(self): ...
    _cKwds: Any
    def _lookupName(self, D=...): ...
    @property
    def normalizedAlpha(self): ...

class PCMYKColor(CMYKColor):
    _scale: float
    def __init__(
        self,
        cyan,
        magenta,
        yellow,
        black,
        density: int = ...,
        spotName: Any | None = ...,
        knockout: Any | None = ...,
        alpha: int = ...,
    ) -> None: ...
    def __repr__(self): ...
    def cKwds(self) -> Generator[Any, None, None]: ...
    cKwds: Any

class CMYKColorSep(CMYKColor):
    _scale: float
    def __init__(
        self,
        cyan: int = ...,
        magenta: int = ...,
        yellow: int = ...,
        black: int = ...,
        spotName: Any | None = ...,
        density: int = ...,
        alpha: int = ...,
    ) -> None: ...
    _cKwds: Any

class PCMYKColorSep(PCMYKColor, CMYKColorSep):
    _scale: float
    def __init__(
        self,
        cyan: int = ...,
        magenta: int = ...,
        yellow: int = ...,
        black: int = ...,
        spotName: Any | None = ...,
        density: int = ...,
        alpha: int = ...,
    ) -> None: ...
    _cKwds: Any

def cmyk2rgb(cmyk, density: int = ...): ...
def rgb2cmyk(r, g, b): ...
def color2bw(colorRGB): ...
def HexColor(val, htmlOnly: bool = ..., hasAlpha: bool = ...): ...
def linearlyInterpolatedColor(c0, c1, x0, x1, x): ...
def obj_R_G_B(c): ...

transparent: Any
_CMYK_white: Any
_PCMYK_white: Any
_CMYK_black: Any
_PCMYK_black: Any
ReportLabBlueOLD: Any
ReportLabBlue: Any
ReportLabBluePCMYK: Any
ReportLabLightBlue: Any
ReportLabFidBlue: Any
ReportLabFidRed: Any
ReportLabGreen: Any
ReportLabLightGreen: Any
aliceblue: Any
antiquewhite: Any
aqua: Any
aquamarine: Any
azure: Any
beige: Any
bisque: Any
black: Any
blanchedalmond: Any
blue: Any
blueviolet: Any
brown: Any
burlywood: Any
cadetblue: Any
chartreuse: Any
chocolate: Any
coral: Any
cornflowerblue: Any
cornflower: Any
cornsilk: Any
crimson: Any
cyan: Any
darkblue: Any
darkcyan: Any
darkgoldenrod: Any
darkgray: Any
darkgrey = darkgray
darkgreen: Any
darkkhaki: Any
darkmagenta: Any
darkolivegreen: Any
darkorange: Any
darkorchid: Any
darkred: Any
darksalmon: Any
darkseagreen: Any
darkslateblue: Any
darkslategray: Any
darkslategrey = darkslategray
darkturquoise: Any
darkviolet: Any
deeppink: Any
deepskyblue: Any
dimgray: Any
dimgrey = dimgray
dodgerblue: Any
firebrick: Any
floralwhite: Any
forestgreen: Any
fuchsia: Any
gainsboro: Any
ghostwhite: Any
gold: Any
goldenrod: Any
gray: Any
grey = gray
green: Any
greenyellow: Any
honeydew: Any
hotpink: Any
indianred: Any
indigo: Any
ivory: Any
khaki: Any
lavender: Any
lavenderblush: Any
lawngreen: Any
lemonchiffon: Any
lightblue: Any
lightcoral: Any
lightcyan: Any
lightgoldenrodyellow: Any
lightgreen: Any
lightgrey: Any
lightpink: Any
lightsalmon: Any
lightseagreen: Any
lightskyblue: Any
lightslategray: Any
lightslategrey = lightslategray
lightsteelblue: Any
lightyellow: Any
lime: Any
limegreen: Any
linen: Any
magenta: Any
maroon: Any
mediumaquamarine: Any
mediumblue: Any
mediumorchid: Any
mediumpurple: Any
mediumseagreen: Any
mediumslateblue: Any
mediumspringgreen: Any
mediumturquoise: Any
mediumvioletred: Any
midnightblue: Any
mintcream: Any
mistyrose: Any
moccasin: Any
navajowhite: Any
navy: Any
oldlace: Any
olive: Any
olivedrab: Any
orange: Any
orangered: Any
orchid: Any
palegoldenrod: Any
palegreen: Any
paleturquoise: Any
palevioletred: Any
papayawhip: Any
peachpuff: Any
peru: Any
pink: Any
plum: Any
powderblue: Any
purple: Any
red: Any
rosybrown: Any
royalblue: Any
saddlebrown: Any
salmon: Any
sandybrown: Any
seagreen: Any
seashell: Any
sienna: Any
silver: Any
skyblue: Any
slateblue: Any
slategray: Any
slategrey = slategray
snow: Any
springgreen: Any
steelblue: Any
tan: Any
teal: Any
thistle: Any
tomato: Any
turquoise: Any
violet: Any
wheat: Any
white: Any
whitesmoke: Any
yellow: Any
yellowgreen: Any
fidblue: Any
fidred: Any
fidlightblue: Any
ColorType: Any

def colorDistance(col1, col2): ...
def cmykDistance(col1, col2): ...

_namedColors: Any

def getAllNamedColors(): ...
def describe(aColor, mode: int = ...): ...
def hue2rgb(m1, m2, h): ...
def hsl2rgb(h, s, l): ...

_re_css: Any

class cssParse:
    def pcVal(self, v): ...
    def rgbPcVal(self, v): ...
    def rgbVal(self, v): ...
    def hueVal(self, v): ...
    def alphaVal(self, v, c: int = ..., n: str = ...): ...
    _n_c: Any
    s: Any
    def __call__(self, s): ...

class toColor:
    _G: Any
    extraColorsNS: Any
    def __init__(self) -> None: ...
    def setExtraColorsNameSpace(self, NS) -> None: ...
    def __call__(self, arg, default: Any | None = ...): ...

def toColorOrNone(arg, default: Any | None = ...): ...
def setColors(**kw): ...
def Whiter(c, f): ...
def Blacker(c, f): ...
def fade(aSpotColor, percentages): ...
def _enforceError(kind, c, tc) -> None: ...
def _enforceSEP(c): ...
def _enforceSEP_BLACK(c): ...
def _enforceSEP_CMYK(c): ...
def _enforceCMYK(c): ...
def _enforceRGB(c): ...
def _chooseEnforceColorSpace(enforceColorSpace): ...
