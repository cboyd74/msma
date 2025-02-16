from src.service.app_logger import AppLogger
from src.config.constants import SHARP_SCALE, STEP_VALUES, STEP_DEFINITIONS, ENHARMONIC_FIXES, CHORD_PATTERNS, NUM_FRETS
from src.model.mode import Mode

logger = AppLogger.get_logger()


def get_next_idx(idx: int, step: str) -> int:
    """
    Retrieves the next index in the scale based on the current index and step value.

    :param idx: int - current index in scale
    :param step: str - step value to move to next note (W, H, 2W, 3W)
    :return: next index in scale
    """
    new_idx = idx
    step_value = STEP_VALUES.get(step)
    for i in range(0, step_value):
        new_idx += 1
        if new_idx == len(SHARP_SCALE):
            new_idx = 0
    return new_idx


# Main functions ##############################################
def get_notes(mode: Mode, root: str) -> [str]:
    """
    Retrieves the list of notes in a given key.
    Applies enharmonic fixes.

    :param mode: Mode - current mode of the key (major, minor, etc.)
    :param root: str - root note of the key
    :return: list of notes in the given key
    """
    steps = STEP_DEFINITIONS.get(mode.name)
    scale = [root]
    chromatic_idx = SHARP_SCALE.index(root)
    for step in steps:
        chromatic_idx = get_next_idx(chromatic_idx, step)
        note = SHARP_SCALE[chromatic_idx]
        scale.append(note)
    if root in ENHARMONIC_FIXES.keys():
        for note in ENHARMONIC_FIXES.get(root):
            if note in scale:
                i = scale.index(note)
                note_fixed = ENHARMONIC_FIXES.get(root).get(note)
                scale[i] = note_fixed
    return scale


def get_chord_pattern(mode: Mode) -> []:
    """
    Retrieves the chord pattern for a given mode.

    :param mode: Mode - current mode of the key
    :return: the chord pattern for the given mode
    """
    return CHORD_PATTERNS.get(mode.name)


# TODO create a step enum
def get_steps(mode: Mode) -> [str]:
    """
    Retrieves the steps for a given mode.

    :param mode: Mode - current mode of the key
    :return: steps for the given mode
    """
    return STEP_DEFINITIONS.get(mode.name)


# Guitar functions #############################################
def get_guitar_string(open_string: str) -> [str]:
    """
    Retrieves a single guitar string for given open string.

    :param open_string: note of the current open string
    :return: all notes on the string in order
    """
    string = []
    chromatic_idx = SHARP_SCALE.index(open_string)
    for i in range(1, NUM_FRETS + 1):
        chromatic_idx = get_next_idx(chromatic_idx, 'H')
        note = SHARP_SCALE[chromatic_idx]
        # TODO maybe add check on root, cast to correct translation
        string.append(note)
    return string
