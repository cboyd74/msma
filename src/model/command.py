from enum import Enum


class Command(Enum):
    """
    Enum class for the commands that the user can input.
    """
    QUIT = 'q'
    HELP = 'h'
    TOGGLE_MODE = 'm'
    TOGGLE_RELATIVE = 'r'
    TOGGLE_PENTATONIC = 'p'
    TOGGLE_BLUES = 'b'
