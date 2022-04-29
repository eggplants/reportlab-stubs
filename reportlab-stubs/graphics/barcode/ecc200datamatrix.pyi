from typing import Any

from reportlab.graphics.barcode.common import Barcode

class ECC200DataMatrix(Barcode):
    barWidth: int
    row_modules: int
    col_modules: int
    row_regions: int
    col_regions: int
    cw_data: int
    cw_ecc: int
    row_usable_modules: Any
    col_usable_modules: Any
    def __init__(self, *args, **kwargs) -> None: ...
    valid: int
    validated: Any
    def validate(self) -> None: ...
    def _encode_c40_char(self, char): ...
    def _encode_c40(self, value): ...
    def _gfsum(self, int1, int2): ...
    def _gfproduct(self, int1, int2): ...
    def _get_reed_solomon_code(self, data, num_code_words): ...
    def _get_next_bits(self, data): ...
    def _place_bit(self, row, col, bit) -> None: ...
    def _place_bit_corner_1(self, data) -> None: ...
    def _place_bit_corner_2(self, data) -> None: ...
    def _place_bit_corner_3(self, data) -> None: ...
    def _place_bit_corner_4(self, data) -> None: ...
    def _place_bit_standard(self, data, row, col) -> None: ...
    _matrix: Any
    def _create_matrix(self, data): ...
    def _create_data_regions(self, matrix): ...
    def _create_empty_matrix(self, row, col): ...
    def _wrap_data_regions_with_finders(self, regions): ...
    def _merge_data_regions(self, regions): ...
    encoded: Any
    def encode(self): ...
    _height: Any
    _width: Any
    def computeSize(self, *args) -> None: ...
    def draw(self) -> None: ...

# Names in __all__ with no definition:
#   ECC200datamatrix
