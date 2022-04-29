import random
from typing import Any

from reportlab import rl_config as rl_config

__version__: str
__doc__: str
STARTUP: Any
COMPUTERS: Any
BLAH: Any
BUZZWORD: Any
STARTREK: Any
PRINTING: Any
PYTHON: Any
leadins: Any
subjects: Any
verbs: Any
objects: Any

def format_wisdom(text, line_length: int = ...): ...
def chomsky(times: int = ...): ...

class RLMonkeyPatchRandom(random.Random):
    def randrange(
        self, start, stop: Any | None = ..., step: int = ..., _int=..., _maxwidth=...
    ): ...
    def choice(self, seq): ...

def randomText(theme=..., sentences: int = ...): ...
