__version__ = "1.0.0"

from .funcs_testing import below2
from .funcs_testing import format_data_for_display
from .funcs_testing import hello
from .funcs_testing import hello_raises
from .funcs_testing import roll_dice
from .pypi2_testing import guess_number
from .pypi2_testing import get_ip
from .pypi2_testing import randum_sum

__all__ = [
    '__version__',
    'below2',
    'format_data_for_display',
    'hello',
    'hello_raises',
    'roll_dice',
    'guess_number',
    'get_ip',
    'randum_sum',
]
