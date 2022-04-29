from typing import Any, NamedTuple

class StdCodecData(NamedTuple):
    exceptions: Any
    rexceptions: Any

class ExtCodecData(NamedTuple):
    baseName: Any
    exceptions: Any
    rexceptions: Any

class RL_Codecs:
    __rl_codecs_data: Any
    __rl_extension_codecs: Any
    __rl_dynamic_codecs: Any
    def __init__(self) -> None: ...
    @staticmethod
    def _makeCodecInfo(name, encoding_map, decoding_map): ...
    @staticmethod
    def _256_exception_codec(name, exceptions, rexceptions, baseRange=...): ...
    __rl_codecs_cache: Any
    @staticmethod
    def __rl_codecs(
        name, cache=..., data=..., extension_codecs=..., _256: bool = ...
    ): ...
    @staticmethod
    def _rl_codecs(name): ...
    @staticmethod
    def register() -> None: ...
    @staticmethod
    def add_dynamic_codec(name, exceptions, rexceptions) -> None: ...
    @staticmethod
    def remove_dynamic_codec(name) -> None: ...
    @staticmethod
    def reset_dynamic_codecs() -> None: ...
