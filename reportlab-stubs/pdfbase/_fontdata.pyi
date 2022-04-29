from typing import Any

from reportlab.lib.utils import rl_isfile as rl_isfile
from reportlab.pdfbase._fontdata_enc_macexpert import (
    MacExpertEncoding as MacExpertEncoding,
)
from reportlab.pdfbase._fontdata_enc_macroman import (
    MacRomanEncoding as MacRomanEncoding,
)
from reportlab.pdfbase._fontdata_enc_pdfdoc import PDFDocEncoding as PDFDocEncoding
from reportlab.pdfbase._fontdata_enc_standard import (
    StandardEncoding as StandardEncoding,
)
from reportlab.pdfbase._fontdata_enc_symbol import SymbolEncoding as SymbolEncoding
from reportlab.pdfbase._fontdata_enc_winansi import WinAnsiEncoding as WinAnsiEncoding
from reportlab.pdfbase._fontdata_enc_zapfdingbats import (
    ZapfDingbatsEncoding as ZapfDingbatsEncoding,
)
from reportlab.rl_config import T1SearchPath as T1SearchPath
from reportlab.rl_config import register_reset as register_reset

__version__: str
__doc__: str
widthVectorsByFont: Any
fontsByName: Any
fontsByBaseEnc: Any
standardFonts: Any
standardFontAttributes: Any
_font2fnrMapWin32: Any
_font2fnrMapLinux2: Any
_font2fnrMap = _font2fnrMapLinux2
_font2fnrMap = _font2fnrMapWin32

def _findFNR(fontName): ...
def _searchT1Dirs(n, rl_isfile=..., T1SearchPath=...): ...
def findT1File(fontName, ext: str = ...): ...

standardEncodings: Any

class _Name2StandardEncodingMap(dict):
    _XMap: Any
    def __setitem__(self, x, v) -> None: ...
    def __getitem__(self, x): ...

encodings: Any
ascent_descent: Any
widthsByFontGlyph: Any

def _reset(initial_dicts=...) -> None: ...
