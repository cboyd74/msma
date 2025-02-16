import random

from src.model.key import Key
from src.service.app_logger import AppLogger
from src.config.constants import NUM_FRETS, MAJOR_RELATIVES, MINOR_RELATIVES, DIM_CHAR, TRADITIONAL_SHARP_TO_FLAT, \
    STANDARD_TUNING, HALF_STEP_UP, normal_fixes, HALF_STEP_DOWN, MAJOR_SCALE_ONLY, HAS_BLUES
from src.model.mode import Mode
from src.service.music import get_notes, get_chord_pattern, get_steps, get_guitar_string
from src.util.helpers import is_flat_key, translate_to_flat, get_traditional_roots

logger = AppLogger.get_logger()


# Public functions ##############################################
def get_new_key(name: str = None, mode: Mode = Mode.MAJOR) -> Key:
    """
    Retrieves a new key with the given root index, name, and mode.
    :param key:
    :param name:
    :param mode:
    :return:
    """
    logger.debug(f"Getting new key with name {name} and mode {mode.value}")
    if name in get_traditional_roots():
        return Key(root_name=name, mode=mode)
    return Key()


def get_key_data(key: Key, is_pent: bool = False, is_blues: bool = False) -> {}:
    """
    Retrieves the data for a given key.
    :param is_pent:
    :param is_blues:
    :param key:
    :return:
    """
    if not key.is_active():
        return {}
    key_data = {
        'root': key.get_traditional_root(),
        'mode': key.get_mode(),
        'relative': _get_relative_key(key),
        'scale': _get_scale_for_frontend(key, is_pent, is_blues),
        'chords': _get_chords_for_frontend(key),
        'steps': get_steps(key.get_mode()),
        'chord_pattern': get_chord_pattern(key.get_mode()),
        'has_minor': False if key.traditional_root in MAJOR_SCALE_ONLY else True,
        'has_blues': True if key.traditional_root in HAS_BLUES.get(key.get_mode()) else False
    }
    logger.debug(f'Getting key data: {key_data}')
    return key_data


def get_fretboard(key: Key, is_pent: bool = False, is_blues: bool = False) -> [[str]]:
    """
    Retrieves the fretboard for a given key.
    :param is_pent:
    :param is_blues:
    :param key:
    :return:
    """
    fretboard = [_get_fret_number_str()]
    for note in STANDARD_TUNING:
        fretboard.append(_get_guitar_string_for_frontend(note, key, is_pent, is_blues))
    logger.debug(f'Getting fretboard: {fretboard}')
    return fretboard


def toggle_mode(key: Key):
    """
    Updates the mode of a given key.
    :param key:
    :return:
    """
    new_mode = Mode.MAJOR if get_current_mode(key) == Mode.MINOR else Mode.MINOR
    logger.debug(f'Toggling mode for {key.get_traditional_root()} {key.get_mode().value} to {new_mode.value}')
    key.toggle_mode()


def is_valid_key(key: Key) -> bool:
    """
    Determines if a given key is valid.
    :param key:
    :return:
    """
    return key.is_active()


def get_key_name(key: Key) -> str:
    """
    Retrieves the name of a given key.
    :param key:
    :return:
    """
    return f'{key.get_traditional_root()} {key.get_mode().value}' if key.is_active() else None


def get_current_mode(key: Key) -> Mode:
    """
    Retrieves the current mode of a given key.
    :param key:
    :return:
    """
    return key.get_mode() if key.is_active() else None


def relative_is_available(key: Key) -> bool:
    """
    Determines if the relative key is available.
    :param key:
    :return:
    """
    relative = _get_relative_key(key)
    return relative and relative.is_active()


def get_random_key() -> Key:
    """
    Retrieves a random key.
    :return:
    """
    mode = random.choice([Mode.MAJOR, Mode.MINOR])
    root = random.choice(get_traditional_roots())
    return Key(root_name=root, mode=mode)


# Private functions #############################################
def _get_scale_for_frontend(key: Key, is_pent: bool = False, is_blues: bool = False) -> [str]:
    """
    Retrieves the scale for a given key.
    :param key:
    :return:
    """
    notes = _get_notes_for_frontend(key)
    if is_pent:
        logger.debug(f'Getting pentatonic scale for {key.get_traditional_root()} {key.get_mode().value}')
        if key.mode == Mode.MAJOR:
            notes = [notes[0], notes[1], notes[2], notes[4], notes[5]]
        elif key.mode == Mode.MINOR:
            notes = [notes[0], notes[2], notes[3], notes[4], notes[6]]
    elif is_blues:
        logger.debug(f'Getting blues scale for {key.get_traditional_root()} {key.get_mode().value}')
        if key.mode == Mode.MAJOR:
            notes = [notes[0], notes[1], HALF_STEP_UP.get(notes[1]), notes[2], notes[4], notes[5]]
        elif key.mode == Mode.MINOR:
            notes = [notes[0], notes[2], notes[3], HALF_STEP_DOWN.get(notes[4]), notes[4], notes[6]]
    logger.debug(f'Getting scale: {notes}')
    return notes


def _get_notes_for_frontend(key: Key) -> [str]:
    """
    Retrieves the notes for a given key.

    :param key: Key - key to get notes for
    :return: notes for the given key
    """
    root = key.get_root()
    traditional_root = key.get_traditional_root()
    mode = key.get_mode()
    notes = get_notes(mode, root)
    for note in notes:
        notes[notes.index(note)] = _translate_note_to_frontend(traditional_root, note, mode)
    return notes


def _translate_note_to_frontend(traditional_root: str, note: str, mode: Mode) -> str:
    """
    Translates a note to the frontend.
    :param traditional_root:
    :param note:
    :param mode:
    :return:
    """
    if is_flat_key(traditional_root, mode):
        # maybe do all translations through this map...down the road...
        if note in TRADITIONAL_SHARP_TO_FLAT.keys():
            note = TRADITIONAL_SHARP_TO_FLAT.get(note)
        note = translate_to_flat(traditional_root, note, mode)
    if note not in get_traditional_roots() and note in normal_fixes.keys():
        note = normal_fixes.get(note)
    return note


def _get_chords_for_frontend(key: Key) -> {}:
    """
    Retrieves the chords for a given key.

    - If the chord pattern is lowercase, it is minor
    - If the chord pattern has a degree symbol, it is diminished
    - Otherwise, it is major

    :param key: Key - key to get chords for
    :return: chords for the given key
    """
    mode = key.get_mode()
    chords = []
    notes = _get_notes_for_frontend(key)
    chord_patterns = get_chord_pattern(mode)
    for i, chord in enumerate(chord_patterns):
        note = notes[i]
        if DIM_CHAR in chord:
            chords.append(f'{note}dim')
        elif chord.islower():
            chords.append(f'{note}m')
        else:
            chords.append(note)
    return chords


def _get_relative_key(key: Key) -> Key:
    """
    Retrieves the relative key for a given key.
    :param key:
    :return:
    """
    if key.is_active():
        root = key.get_traditional_root()
        mode = key.get_mode()
        logger.debug(f'Getting relative key for {root} {mode.value}')
        if mode == Mode.MAJOR:
            key_str = MAJOR_RELATIVES.get(root)
            logger.debug(f'Relative key for {root} {mode.value} is {key_str}')
            key = Key(root_name=key_str, mode=Mode.MINOR)
        else:
            key_str = MINOR_RELATIVES.get(root)
            logger.debug(f'Relative key for {root} {mode.value} is {key_str}')
            key = Key(root_name=key_str, mode=Mode.MAJOR)
        return key


def _get_guitar_string_for_frontend(open_string: str, key: Key, is_pent: bool = False, is_blues: bool = False) -> [str]:
    """
    Retrieves a guitar string for the frontend.
    :param open_string:
    :param key:
    :return:
    """
    root = key.get_traditional_root()
    scale = _get_scale_for_frontend(key, is_pent, is_blues)
    string = get_guitar_string(open_string)
    for i, note in enumerate(string):
        new_note = _translate_note_to_frontend(key.get_traditional_root(), note, key.get_mode())
        if new_note in scale:
            string[i] = new_note
        else:
            string[i] = None
    string_str = f'{open_string} |'
    for note in string:
        prefix = '|---' if note != root else '|--*'
        if note and len(note) == 2:
            string_str += f'{prefix}{note}--'
        else:
            string_str += f'{prefix}{note if note else "-"}---'

    string_str += '|'
    return string_str


def _get_fret_number_str() -> str:
    """
    Retrieves the fret number string.
    :return:
    """
    fret_str = '    '
    prefix = '    '
    for i in range(1, NUM_FRETS + 1):
        if i < 10:
            fret_str += f'{prefix}{i}   '
        else:
            fret_str += f'{prefix}{i}  '
    fret_str += ' '
    return fret_str

