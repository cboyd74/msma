import unittest
from unittest import TestCase

from src.config.constants import TRADITIONAL_FLAT_TO_SHARP
from src.model.mode import Mode
from src.service.music import get_notes, get_steps, get_chord_pattern, get_guitar_string


class TestMusic(TestCase):

    # Test get_notes ############################################
    def test_get_notes_c_major(self):
        expected_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
        notes = get_notes(Mode.MAJOR, 'C')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_c_minor(self):
        expected_notes = ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#', 'C']
        notes = get_notes(Mode.MINOR, 'C')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_g_major(self):
        expected_notes = ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G']
        notes = get_notes(Mode.MAJOR, 'G')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_g_minor(self):
        expected_notes = ['G', 'A', 'A#', 'C', 'D', 'D#', 'F', 'G']
        notes = get_notes(Mode.MINOR, 'G')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_d_major(self):
        expected_notes = ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D']
        notes = get_notes(Mode.MAJOR, 'D')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_d_minor(self):
        expected_notes = ['D', 'E', 'F', 'G', 'A', 'A#', 'C', 'D']
        notes = get_notes(Mode.MINOR, 'D')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_a_major(self):
        expected_notes = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A']
        notes = get_notes(Mode.MAJOR, 'A')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_a_minor(self):
        expected_notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']
        notes = get_notes(Mode.MINOR, 'A')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_e_major(self):
        expected_notes = ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E']
        notes = get_notes(Mode.MAJOR, 'E')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_e_minor(self):
        expected_notes = ['E', 'F#', 'G', 'A', 'B', 'C', 'D', 'E']
        notes = get_notes(Mode.MINOR, 'E')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_b_major(self):
        expected_notes = ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B']
        notes = get_notes(Mode.MAJOR, 'B')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_b_minor(self):
        expected_notes = ['B', 'C#', 'D', 'E', 'F#', 'G', 'A', 'B']
        notes = get_notes(Mode.MINOR, 'B')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_f_sharp_major(self):
        expected_notes = ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F', 'F#']
        notes = get_notes(Mode.MAJOR, 'F#')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_f_sharp_minor(self):
        expected_notes = ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E', 'F#']
        notes = get_notes(Mode.MINOR, 'F#')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_c_sharp_major(self):
        expected_notes = ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C', 'C#']
        notes = get_notes(Mode.MAJOR, 'C#')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_c_sharp_minor(self):
        expected_notes = ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B', 'C#']
        notes = get_notes(Mode.MINOR, 'C#')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_f_major(self):
        expected_notes = ['F', 'G', 'A', 'A#', 'C', 'D', 'E', 'F']
        notes = get_notes(Mode.MAJOR, 'F')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_f_minor(self):
        expected_notes = ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#', 'F']
        notes = get_notes(Mode.MINOR, 'F')
        self.assertEqual(expected_notes, notes)

    def test_get_notes_b_flat_major(self):
        root = TRADITIONAL_FLAT_TO_SHARP.get('Bb')
        expected_notes = ['A#', 'C', 'D', 'D#', 'F', 'G', 'A', 'A#']
        notes = get_notes(Mode.MAJOR, root)
        self.assertEqual(expected_notes, notes)

    def test_get_notes_b_flat_minor(self):
        root = TRADITIONAL_FLAT_TO_SHARP.get('Bb')
        expected_notes = ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#', 'A#']
        notes = get_notes(Mode.MINOR, root)
        self.assertEqual(expected_notes, notes)

    def test_get_notes_e_flat_major(self):
        root = TRADITIONAL_FLAT_TO_SHARP.get('Eb')
        expected_notes = ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D', 'D#']
        notes = get_notes(Mode.MAJOR, root)
        self.assertEqual(expected_notes, notes)

    def test_get_notes_e_flat_minor(self):
        root = TRADITIONAL_FLAT_TO_SHARP.get('Eb')
        expected_notes = ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'C#', 'D#']
        notes = get_notes(Mode.MINOR, root)
        self.assertEqual(expected_notes, notes)

    def test_get_notes_a_flat_major(self):
        root = TRADITIONAL_FLAT_TO_SHARP.get('Ab')
        expected_notes = ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G', 'G#']
        notes = get_notes(Mode.MAJOR, root)
        self.assertEqual(expected_notes, notes)

    def test_get_notes_a_flat_minor(self):
        root = TRADITIONAL_FLAT_TO_SHARP.get('Ab')
        expected_notes = ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#', 'G#']
        notes = get_notes(Mode.MINOR, root)
        self.assertEqual(expected_notes, notes)

    def test_get_notes_d_flat_major(self):
        root = TRADITIONAL_FLAT_TO_SHARP.get('Db')
        expected_notes = ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C', 'C#']
        notes = get_notes(Mode.MAJOR, root)
        self.assertEqual(expected_notes, notes)

    def test_get_notes_d_flat_minor(self):
        root = TRADITIONAL_FLAT_TO_SHARP.get('Db')
        expected_notes = ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B', 'C#']
        notes = get_notes(Mode.MINOR, root)
        self.assertEqual(expected_notes, notes)

    def test_get_notes_g_flat_major(self):
        root = TRADITIONAL_FLAT_TO_SHARP.get('Gb')
        expected_notes = ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F', 'F#']
        notes = get_notes(Mode.MAJOR, root)
        self.assertEqual(expected_notes, notes)

    def test_get_notes_g_flat_minor(self):
        root = TRADITIONAL_FLAT_TO_SHARP.get('Gb')
        expected_notes = ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E', 'F#']
        notes = get_notes(Mode.MINOR, root)
        self.assertEqual(expected_notes, notes)

    def test_get_notes_c_flat_major(self):
        root = TRADITIONAL_FLAT_TO_SHARP.get('Cb')
        expected_notes = ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B']
        notes = get_notes(Mode.MAJOR, root)
        self.assertEqual(expected_notes, notes)

    def test_get_notes_c_flat_minor(self):
        root = TRADITIONAL_FLAT_TO_SHARP.get('Cb')
        expected_notes = ['B', 'C#', 'D', 'E', 'F#', 'G', 'A', 'B']
        notes = get_notes(Mode.MINOR, root)
        self.assertEqual(expected_notes, notes)

    # Test get_steps ############################################
    def test_get_steps_major(self):
        expected_steps = ['W', 'W', 'H', 'W', 'W', 'W', 'H']
        steps = get_steps(Mode.MAJOR)
        self.assertEqual(steps, expected_steps)

    def test_get_steps_minor_mode(self):
        expected_steps = ['W', 'H', 'W', 'W', 'H', 'W', 'W']
        steps = get_steps(Mode.MINOR)
        self.assertEqual(steps, expected_steps)

    # Test get_chord_pattern ######################################
    def test_get_chord_pattern_major_mode(self):
        expected_pattern = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']
        pattern = get_chord_pattern(Mode.MAJOR)
        self.assertEqual(pattern, expected_pattern)

    def test_get_chord_pattern_minor_mode(self):
        expected_pattern = ['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII']
        pattern = get_chord_pattern(Mode.MINOR)
        self.assertEqual(pattern, expected_pattern)

    # Test guitar functions ########################################
    def test_get_guitar_string_e(self):
        expected_string = ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#',
                           'A', 'A#', 'B', 'C', 'C#', 'D']
        string = get_guitar_string('E')
        self.assertEqual(expected_string, string)

    def test_get_guitar_string_a(self):
        expected_string = ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#',
                           'D', 'D#', 'E', 'F', 'F#', 'G']
        string = get_guitar_string('A')
        self.assertEqual(expected_string, string)

    def test_get_guitar_string_d(self):
        expected_string = ['D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#',
                           'G', 'G#', 'A', 'A#', 'B', 'C']
        string = get_guitar_string('D')
        self.assertEqual(expected_string, string)

    def test_get_guitar_string_g(self):
        expected_string = ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C',
                           'C#', 'D', 'D#', 'E', 'F']
        string = get_guitar_string('G')
        self.assertEqual(expected_string, string)

    def test_get_guitar_string_b(self):
        expected_string = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#',
                           'E', 'F', 'F#', 'G', 'G#', 'A']
        string = get_guitar_string('B')
        self.assertEqual(expected_string, string)

if __name__ == '__main__':
    unittest.main()