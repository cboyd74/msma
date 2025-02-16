from src.config.constants import SHARP_CHAR, FLAT_CHAR, SHARP_TO_FLAT, \
    FLAT_KEYS_MAJOR, FLAT_KEYS_MINOR, enharmonic_to_traditional, TRADITIONAL_ROOTS
from src.model.mode import Mode


# UI Helpers ##################################################
def center_string_x(string: str, start_x, end_x) -> int:
    """
    Returns the center x position.
    :param string:
    :param start_x:
    :param end_x:
    :return:
    """
    w = end_x - start_x
    starting = (w - len(string)) // 2
    return starting


def center_string_y(string: str, start_y, end_y) -> int:
    """
    Returns the center y position.
    :param string:
    :param start_y:
    :param end_y:
    :return:
    """
    h = end_y - start_y
    return (h - len(string)) // 2


def right_string_x(string: str, start_x, end_x) -> int:
    """
    Returns the right x position.
    :param string:
    :param start_x:
    :param end_x:
    :return:
    """
    w = end_x - start_x
    return w - len(string) - 1


def left_string_x(start_x) -> int:
    """
    Returns the left x position.
    :param start_x:
    :return:
    """
    return start_x + 2


def is_flat_key(key: str, mode: Mode) -> bool:
    """
    Checks if a key is flat.
    :param key:
    :param mode:
    :return:
    """
    if mode == Mode.MAJOR:
        return key in FLAT_KEYS_MAJOR
    return key in FLAT_KEYS_MINOR


# Translate Helpers ############################################
def translate_to_flat(root: str, note: str, mode) -> str:
    """
    Translates a note to flat.
    :param root:
    :param note:
    :param mode:
    :return:
    """
    if (root, mode) in enharmonic_to_traditional.keys():
        fixes = enharmonic_to_traditional.get((root, mode))
        if note in fixes.keys():
            return fixes.get(note)
    if is_sharp(note):
        return SHARP_TO_FLAT.get(note)
    return note


def is_sharp(note: str) -> bool:
    """
    Checks if a note is sharp.

    :param note: str - note to check
    :return: bool - whether the note is sharp
    """
    return note and SHARP_CHAR in note


def is_flat(note: str) -> bool:
    """
    Checks if a note is flat.

    :param note: str - note to check
    :return: bool - whether the note is flat
    """
    return note and FLAT_CHAR in note


def get_traditional_roots() -> [str]:
    """
    Returns the traditional roots.
    :return:
    """
    return TRADITIONAL_ROOTS
