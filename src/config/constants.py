from src.model.mode import Mode

# Single Constants #############################################
NUM_FRETS = 22
DIM_CHAR = '°'
FLAT_CHAR = 'b'
SHARP_CHAR = '#'

# Lists of notes ################################################
STANDARD_TUNING = ['E', 'B', 'G', 'D', 'A', 'E']
TRADITIONAL_ROOTS = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb']
SHARP_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
FLAT_KEYS_MAJOR = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb']
FLAT_KEYS_MINOR = ['D', 'G', 'C', 'F', 'Bb', 'Eb', 'Ab', 'Db']

# Translators #################################################
STEP_DEFINITIONS = {
    'MAJOR': ['W', 'W', 'H', 'W', 'W', 'W', 'H'],
    'MINOR': ['W', 'H', 'W', 'W', 'H', 'W', 'W']
}
STEP_VALUES = {'W': 2, 'H': 1, '2W': 2, '3W': 3}

CHORD_PATTERNS = {
    'MAJOR': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'],
    'MINOR': ['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII']
}

MAJOR_RELATIVES = {
    'C': 'A', 'G': 'E', 'D': 'B', 'A': 'F#', 'E': 'C#', 'B': 'G#', 'F#': 'D#', 'C#': 'A#', 'F': 'D',
    'Bb': 'G', 'Eb': 'C', 'Ab': 'F', 'Db': 'Bb', 'Gb': 'Eb', 'Cb': 'Ab'
}
MINOR_RELATIVES = {
    'A': 'C', 'E': 'G', 'B': 'D', 'F#': 'A', 'C#': 'E', 'G#': 'B', 'D#': 'F#', 'A#': 'C#', 'D': 'F',
    'G': 'Bb', 'C': 'Eb', 'F': 'Ab', 'Bb': 'Db', 'Eb': 'Gb', 'Ab': 'Cb'
}

SHARP_TO_FLAT = {'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab', 'A#': 'Bb', 'B#': 'Cb'}

normal_fixes = {
    "E#": "F",
    "B#": "C",
    "Fb": "E",
    'Cb': 'B'
}

enharmonic_to_traditional = {
    ("C#", Mode.MAJOR): {"E#": "F"},
    ("F#", Mode.MAJOR): {"E#": "F"},
    ("G#", Mode.MAJOR): {"B": "C", "E": "F", "F#": "G"},
    ("Db", Mode.MAJOR): {"E": "Fb", "A": "Bb", "E#": "F"},
    ("D", Mode.MAJOR): {"Fb": "E"},
    ("Ab", Mode.MAJOR): {"E": "Fb"},
    ("Cb", Mode.MAJOR): {"E": "Fb", 'B': 'Cb'},
    # TODO: gb to g bc of enharmonic fix in backend, update this
    ("Eb", Mode.MAJOR): {"E#": "F", "F#": "G", 'B': 'Cb', "B#": "C", 'Gb': 'G'},
    ("Gb", Mode.MAJOR): {"E#": "F", 'B': 'Cb'},
    ("Ab", Mode.MINOR): {"E": "Fb", 'B': 'Cb'},
    ("Db", Mode.MINOR): {"E": "Fb", "A": "Bb", "E#": "F", 'B': 'Cb'},
    ("Eb", Mode.MINOR): {"E#": "F", 'B': 'Cb'},
}

TRADITIONAL_FLAT_TO_SHARP = {
    "Db": "C#",
    "Eb": "D#",
    "Gb": "F#",
    "Ab": "G#",
    "Bb": "A#",
    "Cb": "B",
    "Fb": "E"
}

TRADITIONAL_SHARP_TO_FLAT = {
    "C#": "Db",
    "D#": "Eb",
    "F#": "Gb",
    "G#": "Ab",
    "A#": "Bb"
}

HALF_STEP_UP = {
    "Ab": "A",
    "A": "A#",
    "A#": "B",
    "Bb": "B",
    "B": "C",
    "Cb": "C",
    "C": "C#",
    "C#": "D",
    "Db": "D",
    "D": "D#",
    "D#": "E",
    "Eb": "E",
    "E": "F",
    "Fb": "F",
    "F": "F#",
    "F#": "G",
    "Gb": "G",
    "G": "G#",
    "G#": "A"
}

HALF_STEP_DOWN = {
    "Ab": "G",
    "A": "G#",
    "A#": "A",
    "Bb": "A",
    "B": "A#",
    "C": "B",
    "C#": "C",
    "Db": "C",
    "D": "C#",
    "D#": "D",
    "Eb": "D",
    "E": "D#",
    "Fb": "E",
    "F": "E",
    "F#": "F",
    "Gb": "F",
    "G": "Gb",
    "G#": "G"
}

MAJOR_SCALE_ONLY = ['Cb', 'Db', 'Gb']
HAS_BLUES = {
    Mode.MAJOR: ['C', 'G', 'D', 'A', 'E', 'B', 'F'],
    Mode.MINOR: ['A', 'E', 'D', 'G', 'B']
}