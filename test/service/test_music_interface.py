import unittest
from unittest import TestCase

from src.model.mode import Mode
from src.model.key import Key
from src.service.music_interface import (_get_relative_key, _get_chords_for_frontend,
                                         _get_notes_for_frontend, _get_scale_for_frontend, get_new_key, get_key_data,
                                         relative_is_available, get_random_key, get_current_mode, get_key_name,
                                         is_valid_key, toggle_mode)


class TestMusicInterface(TestCase):

    # Test get_chords_for_frontend #################################
    def test_get_notes_for_frontend_c_major(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'], notes)

    def test_get_notes_for_frontend_c_minor(self):
        key = Key(root_name='C', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C'], notes)

    def test_get_notes_for_frontend_g_major(self):
        key = Key(root_name='G', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G'], notes)

    def test_get_notes_for_frontend_g_minor(self):
        key = Key(root_name='G', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['G', 'A', 'Bb', 'C', 'D', 'Eb', 'F', 'G'], notes)

    def test_get_notes_for_frontend_d_major(self):
        key = Key(root_name='D', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D'], notes)

    def test_get_notes_for_frontend_d_minor(self):
        key = Key(root_name='D', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['D', 'E', 'F', 'G', 'A', 'Bb', 'C', 'D'], notes)

    def test_get_notes_for_frontend_a_major(self):
        key = Key(root_name='A', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A'], notes)

    def test_get_notes_for_frontend_a_minor(self):
        key = Key(root_name='A', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'], notes)

    def test_get_notes_for_frontend_e_major(self):
        key = Key(root_name='E', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E'], notes)

    def test_get_notes_for_frontend_e_minor(self):
        key = Key(root_name='E', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['E', 'F#', 'G', 'A', 'B', 'C', 'D', 'E'], notes)

    def test_get_notes_for_frontend_b_major(self):
        key = Key(root_name='B', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'], notes)

    def test_get_notes_for_frontend_b_minor(self):
        key = Key(root_name='B', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['B', 'C#', 'D', 'E', 'F#', 'G', 'A', 'B'], notes)

    def test_get_notes_for_frontend_f_sharp_major(self):
        key = Key(root_name='F#', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F', 'F#'], notes)

    def test_get_notes_for_frontend_f_sharp_minor(self):
        key = Key(root_name='F#', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['F#', 'G#', 'A', 'B', 'C#', 'D', 'E', 'F#'], notes)

    def test_get_notes_for_frontend_c_sharp_major(self):
        key = Key(root_name='C#', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C', 'C#'], notes)

    def test_get_notes_for_frontend_c_sharp_minor(self):
        key = Key(root_name='C#', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B', 'C#'], notes)

    def test_get_notes_for_frontend_f_major(self):
        key = Key(root_name='F', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F'], notes)

    def test_get_notes_for_frontend_f_minor(self):
        key = Key(root_name='F', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F'], notes)

    def test_get_notes_for_frontend_b_flat_major(self):
        key = Key(root_name='Bb', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'], notes)

    def test_get_notes_for_frontend_b_flat_minor(self):
        key = Key(root_name='Bb', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'], notes)

    def test_get_notes_for_frontend_e_flat_major(self):
        key = Key(root_name='Eb', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'], notes)

    def test_get_notes_for_frontend_e_flat_minor(self):
        key = Key(root_name='Eb', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['Eb', 'F', 'Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb'], notes)

    def test_get_notes_for_frontend_a_flat_major(self):
        key = Key(root_name='Ab', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G', 'Ab'], notes)

    def test_get_notes_for_frontend_a_flat_minor(self):
        key = Key(root_name='Ab', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'E', 'Gb', 'Ab'], notes)

    def test_get_notes_for_frontend_d_flat_major(self):
        key = Key(root_name='Db', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C', 'Db'], notes)

    def test_get_notes_for_frontend_d_flat_minor(self):
        key = Key(root_name='Db', mode=Mode.MINOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['Db', 'Eb', 'E', 'Gb', 'Ab', 'Bb', 'Cb', 'Db'], notes)

    def test_get_notes_for_frontend_g_flat_major(self):
        key = Key(root_name='Gb', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F', 'Gb'], notes)

    def test_get_notes_for_frontend_c_flat_major(self):
        key = Key(root_name='Cb', mode=Mode.MAJOR)
        notes = _get_notes_for_frontend(key)
        self.assertEqual(['Cb', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'Bb', 'Cb'], notes)

    # Test get scales for frontend ##################################
    # c g d a e b fs cs f bf ef af df gf cf

    def test_get_scale_for_frontend_c_major(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'], scale)

    def test_get_scale_for_frontend_c_major_pentatonic(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['C', 'D', 'E', 'G', 'A'], scale)

    def test_get_scale_for_frontend_c_major_blues(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_blues=True)
        self.assertEqual(['C', 'D', 'D#', 'E', 'G', 'A'], scale)

    def test_get_scale_for_frontend_c_minor(self):
        key = Key(root_name='C', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C'], scale)

    def test_get_scale_for_frontend_c_minor_pentatonic(self):
        key = Key(root_name='C', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['C', 'Eb', 'F', 'G', 'Bb'], scale)

    def test_get_scale_for_frontend_g_major(self):
        key = Key(root_name='G', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G'], scale)

    def test_get_scale_for_frontend_g_major_pentatonic(self):
        key = Key(root_name='G', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['G', 'A', 'B', 'D', 'E'], scale)

    def test_get_scale_for_frontend_g_major_blues(self):
        key = Key(root_name='G', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_blues=True)
        self.assertEqual(['G', 'A', 'A#', 'B', 'D', 'E'], scale)

    def test_get_scale_for_frontend_g_minor(self):
        key = Key(root_name='G', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['G', 'A', 'Bb', 'C', 'D', 'Eb', 'F', 'G'], scale)

    def test_get_scale_for_frontend_g_minor_pentatonic(self):
        key = Key(root_name='G', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['G', 'Bb', 'C', 'D', 'F'], scale)

    def test_get_scale_for_frontend_g_minor_blues(self):
        key = Key(root_name='G', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_blues=True)
        self.assertEqual(['G', 'Bb', 'C', 'C#', 'D', 'F'], scale)

    def test_get_scale_for_frontend_d_major(self):
        key = Key(root_name='D', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D'], scale)

    def test_get_scale_for_frontend_d_major_pentatonic(self):
        key = Key(root_name='D', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['D', 'E', 'F#', 'A', 'B'], scale)

    def test_get_scale_for_frontend_d_major_blues(self):
        key = Key(root_name='D', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_blues=True)
        self.assertEqual(['D', 'E', 'F', 'F#', 'A', 'B'], scale)

    def test_get_scale_for_frontend_d_minor(self):
        key = Key(root_name='D', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['D', 'E', 'F', 'G', 'A', 'Bb', 'C', 'D'], scale)

    def test_get_scale_for_frontend_d_minor_pentatonic(self):
        key = Key(root_name='D', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['D', 'F', 'G', 'A', 'C'], scale)

    def test_get_scale_for_frontend_d_minor_blues(self):
        key = Key(root_name='D', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_blues=True)
        self.assertEqual(['D', 'F', 'G', 'G#', 'A', 'C'], scale)

    def test_get_scale_for_frontend_a_major(self):
        key = Key(root_name='A', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A'], scale)

    def test_get_scale_for_frontend_a_major_pentatonic(self):
        key = Key(root_name='A', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['A', 'B', 'C#', 'E', 'F#'], scale)

    def test_get_scale_for_frontend_a_major_blues(self):
        # TODO fix B# issue
        key = Key(root_name='A', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_blues=True)
        self.assertEqual(['A', 'B', 'C', 'C#', 'E', 'F#'], scale)

    def test_get_scale_for_frontend_a_minor(self):
        key = Key(root_name='A', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'], scale)

    def test_get_scale_for_frontend_a_minor_pentatonic(self):
        key = Key(root_name='A', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['A', 'C', 'D', 'E', 'G'], scale)

    def test_get_scale_for_frontend_a_minor_blues(self):
        key = Key(root_name='A', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_blues=True)
        self.assertEqual(['A', 'C', 'D', 'D#', 'E', 'G'], scale)

    def test_get_scale_for_frontend_e_major(self):
        key = Key(root_name='E', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E'], scale)

    def test_get_scale_for_frontend_e_major_pentatonic(self):
        key = Key(root_name='E', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['E', 'F#', 'G#', 'B', 'C#'], scale)

    def test_get_scale_for_frontend_e_major_blues(self):
        key = Key(root_name='E', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_blues=True)
        self.assertEqual(['E', 'F#', 'G', 'G#', 'B', 'C#'], scale)

    def test_get_scale_for_frontend_e_minor(self):
        key = Key(root_name='E', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['E', 'F#', 'G', 'A', 'B', 'C', 'D', 'E'], scale)

    def test_get_scale_for_frontend_e_minor_pentatonic(self):
        key = Key(root_name='E', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['E', 'G', 'A', 'B', 'D'], scale)

    def test_get_scale_for_frontend_e_minor_blues(self):
        key = Key(root_name='E', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_blues=True)
        self.assertEqual(['E', 'G', 'A', 'A#', 'B', 'D'], scale)

    def test_get_scale_for_frontend_b_major(self):
        key = Key(root_name='B', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'], scale)

    def test_get_scale_for_frontend_b_major_pentatonic(self):
        key = Key(root_name='B', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['B', 'C#', 'D#', 'F#', 'G#'], scale)

    def test_get_scale_for_frontend_b_major_blues(self):
        key = Key(root_name='B', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_blues=True)
        self.assertEqual(['B', 'C#', 'D', 'D#', 'F#', 'G#'], scale)

    def test_get_scale_for_frontend_b_minor(self):
        key = Key(root_name='B', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['B', 'C#', 'D', 'E', 'F#', 'G', 'A', 'B'], scale)

    def test_get_scale_for_frontend_b_minor_pentatonic(self):
        key = Key(root_name='B', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['B', 'D', 'E', 'F#', 'A'], scale)

    def test_get_scale_for_frontend_b_minor_blues(self):
        key = Key(root_name='B', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_blues=True)
        self.assertEqual(['B', 'D', 'E', 'F', 'F#', 'A'], scale)

    def test_get_scale_for_frontend_f_sharp_major(self):
        key = Key(root_name='F#', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F', 'F#'], scale)

    def test_get_scale_for_frontend_f_sharp_major_pentatonic(self):
        key = Key(root_name='F#', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['F#', 'G#', 'A#', 'C#', 'D#'], scale)

    def test_get_scale_for_frontend_f_sharp_minor(self):
        key = Key(root_name='F#', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['F#', 'G#', 'A', 'B', 'C#', 'D', 'E', 'F#'], scale)

    def test_get_scale_for_frontend_f_sharp_minor_pentatonic(self):
        key = Key(root_name='F#', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['F#', 'A', 'B', 'C#', 'E'], scale)

    def test_get_scale_for_frontend_c_sharp_major(self):
        key = Key(root_name='C#', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C', 'C#'], scale)

    def test_get_scale_for_frontend_c_sharp_major_pentatonic(self):
        key = Key(root_name='C#', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['C#', 'D#', 'F', 'G#', 'A#'], scale)

    # def test_get_scale_for_frontend_c_sharp_major_blues(self):
    #     # TODO disable this one
    #     key = Key(root_name='C#', mode=Mode.MAJOR)
    #     scale = _get_scale_for_frontend(key, is_blues=True)
    #     self.assertEqual(['C#', 'D#', 'E', 'F', 'G#', 'A#'], scale)

    def test_get_scale_for_frontend_c_sharp_minor(self):
        key = Key(root_name='C#', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B', 'C#'], scale)

    def test_get_scale_for_frontend_c_sharp_minor_pentatonic(self):
        key = Key(root_name='C#', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['C#', 'E', 'F#', 'G#', 'B'], scale)

    # def test_get_scale_for_frontend_c_sharp_minor_blues(self):
    #     #TODO disable this one
    #     key = Key(root_name='C#', mode=Mode.MINOR)
    #     scale = _get_scale_for_frontend(key, is_blues=True)
    #     self.assertEqual(['C#', 'E', 'F#', 'G', 'G#', 'B'], scale)

    def test_get_scale_for_frontend_f_major(self):
        key = Key(root_name='F', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F'], scale)

    def test_get_scale_for_frontend_f_major_pentatonic(self):
        key = Key(root_name='F', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['F', 'G', 'A', 'C', 'D'], scale)

    def test_get_scale_for_frontend_f_major_blues(self):
        key = Key(root_name='F', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_blues=True)
        self.assertEqual(['F', 'G', 'G#', 'A', 'C', 'D'], scale)

    def test_get_scale_for_frontend_f_minor(self):
        key = Key(root_name='F', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F'], scale)

    def test_get_scale_for_frontend_f_minor_pentatonic(self):
        key = Key(root_name='F', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['F', 'Ab', 'Bb', 'C', 'Eb'], scale)

    # def test_get_scale_for_frontend_f_minor_blues(self):
    #     #TODO disable this one
    #     key = Key(root_name='F', mode=Mode.MINOR)
    #     scale = _get_scale_for_frontend(key, is_blues=True)
    #     self.assertEqual(['F', 'Ab', 'Bb', 'B', 'C', 'Eb'], scale)

    def test_get_scale_for_frontend_b_flat_major(self):
        key = Key(root_name='Bb', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'], scale)

    def test_get_scale_for_frontend_b_flat_major_pentatonic(self):
        key = Key(root_name='Bb', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['Bb', 'C', 'D', 'F', 'G'], scale)

    # def test_get_scale_for_frontend_b_flat_major_blues(self):
    #     #TODO Disable this one
    #     key = Key(root_name='Bb', mode=Mode.MAJOR)
    #     scale = _get_scale_for_frontend(key, is_blues=True)
    #     self.assertEqual(['Bb', 'C', 'C#', 'D', 'F', 'G'], scale)

    def test_get_scale_for_frontend_b_flat_minor(self):
        key = Key(root_name='Bb', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'], scale)

    def test_get_scale_for_frontend_b_flat_minor_pentatonic(self):
        key = Key(root_name='Bb', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['Bb', 'Db', 'Eb', 'F', 'Ab'], scale)

    # def test_get_scale_for_frontend_b_flat_minor_blues(self):
    #     # TODO disable this one
    #     key = Key(root_name='Bb', mode=Mode.MINOR)
    #     scale = _get_scale_for_frontend(key, is_blues=True)
    #     self.assertEqual(['Bb', 'Db', 'Eb', 'F', 'F#', 'Ab'], scale)

    def test_get_scale_for_frontend_e_flat_major(self):
        key = Key(root_name='Eb', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'], scale)

    def test_get_scale_for_frontend_e_flat_major_pentatonic(self):
        key = Key(root_name='Eb', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['Eb', 'F', 'G', 'Bb', 'C'], scale)

    def test_get_scale_for_frontend_e_flat_minor(self):
        key = Key(root_name='Eb', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['Eb', 'F', 'Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb'], scale)

    def test_get_scale_for_frontend_e_flat_minor_pentatonic(self):
        key = Key(root_name='Eb', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['Eb', 'Gb', 'Ab', 'Bb', 'Db'], scale)

    def test_get_scale_for_frontend_a_flat_major(self):
        key = Key(root_name='Ab', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G', 'Ab'], scale)

    def test_get_scale_for_frontend_a_flat_major_pentatonic(self):
        key = Key(root_name='Ab', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['Ab', 'Bb', 'C', 'Eb', 'F'], scale)

    def test_get_scale_for_frontend_a_flat_minor(self):
        key = Key(root_name='Ab', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'E', 'Gb', 'Ab'], scale)

    def test_get_scale_for_frontend_a_flat_minor_pentatonic(self):
        key = Key(root_name='Ab', mode=Mode.MINOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['Ab', 'Cb', 'Db', 'Eb', 'Gb'], scale)

    def test_get_scale_for_frontend_d_flat_major(self):
        key = Key(root_name='Db', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C', 'Db'], scale)

    def test_get_scale_for_frontend_d_flat_major_pentatonic(self):
        key = Key(root_name='Db', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['Db', 'Eb', 'F', 'Ab', 'Bb'], scale)

    def test_get_scale_for_frontend_g_flat_major(self):
        key = Key(root_name='Gb', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F', 'Gb'], scale)

    def test_get_scale_for_frontend_g_flat_major_pentatonic(self):
        key = Key(root_name='Gb', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['Gb', 'Ab', 'Bb', 'Db', 'Eb'], scale)

    def test_get_scale_for_frontend_c_flat_major(self):
        key = Key(root_name='Cb', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key)
        self.assertEqual(['Cb', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'Bb', 'Cb'], scale)

    def test_get_scale_for_frontend_c_flat_major_pentatonic(self):
        key = Key(root_name='Cb', mode=Mode.MAJOR)
        scale = _get_scale_for_frontend(key, is_pent=True)
        self.assertEqual(['Cb', 'Db', 'Eb', 'Gb', 'Ab'], scale)

    # Test get_chords_for_frontend #################################
    def test_get_chords_for_frontend_c_major(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'], chords)

    def test_get_chords_for_frontend_c_minor(self):
        key = Key(root_name='C', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Cm', 'Ddim', 'Eb', 'Fm', 'Gm', 'Ab', 'Bb'], chords)

    def test_get_chords_for_frontend_g_major(self):
        key = Key(root_name='G', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#dim'], chords)

    def test_get_chords_for_frontend_g_minor(self):
        key = Key(root_name='G', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Gm', 'Adim', 'Bb', 'Cm', 'Dm', 'Eb', 'F'], chords)

    def test_get_chords_for_frontend_d_major(self):
        key = Key(root_name='D', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#dim'], chords)

    def test_get_chords_for_frontend_d_minor(self):
        key = Key(root_name='D', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Dm', 'Edim', 'F', 'Gm', 'Am', 'Bb', 'C'], chords)

    def test_get_chords_for_frontend_a_major(self):
        key = Key(root_name='A', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#dim'], chords)

    def test_get_chords_for_frontend_a_minor(self):
        key = Key(root_name='A', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Am', 'Bdim', 'C', 'Dm', 'Em', 'F', 'G'], chords)

    def test_get_chords_for_frontend_e_major(self):
        key = Key(root_name='E', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#dim'], chords)

    def test_get_chords_for_frontend_e_minor(self):
        key = Key(root_name='E', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Em', 'F#dim', 'G', 'Am', 'Bm', 'C', 'D'], chords)

    def test_get_chords_for_frontend_b_major(self):
        key = Key(root_name='B', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#dim'], chords)

    def test_get_chords_for_frontend_b_minor(self):
        key = Key(root_name='B', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Bm', 'C#dim', 'D', 'Em', 'F#m', 'G', 'A'], chords)

    def test_get_chords_for_frontend_f_sharp_major(self):
        key = Key(root_name='F#', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'Fdim'], chords)

    def test_get_chords_for_frontend_f_sharp_minor(self):
        key = Key(root_name='F#', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['F#m', 'G#dim', 'A', 'Bm', 'C#m', 'D', 'E'], chords)

    def test_get_chords_for_frontend_c_sharp_major(self):
        key = Key(root_name='C#', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['C#', 'D#m', 'Fm', 'F#', 'G#', 'A#m', 'Cdim'], chords)

    def test_get_chords_for_frontend_c_sharp_minor(self):
        key = Key(root_name='C#', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['C#m', 'D#dim', 'E', 'F#m', 'G#m', 'A', 'B'], chords)

    def test_get_chords_for_frontend_f_major(self):
        key = Key(root_name='F', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Edim'], chords)

    def test_get_chords_for_frontend_f_minor(self):
        key = Key(root_name='F', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Fm', 'Gdim', 'Ab', 'Bbm', 'Cm', 'Db', 'Eb'], chords)

    def test_get_chords_for_frontend_b_flat_major(self):
        key = Key(root_name='Bb', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Bb', 'Cm', 'Dm', 'Eb', 'F', 'Gm', 'Adim'], chords)

    def test_get_chords_for_frontend_b_flat_minor(self):
        key = Key(root_name='Bb', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Bbm', 'Cdim', 'Db', 'Ebm', 'Fm', 'Gb', 'Ab'], chords)

    def test_get_chords_for_frontend_e_flat_major(self):
        key = Key(root_name='Eb', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Eb', 'Fm', 'Gm', 'Ab', 'Bb', 'Cm', 'Ddim'], chords)

    def test_get_chords_for_frontend_e_flat_minor(self):
        key = Key(root_name='Eb', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Ebm', 'Fdim', 'Gb', 'Abm', 'Bbm', 'Cb', 'Db'], chords)

    def test_get_chords_for_frontend_a_flat_major(self):
        key = Key(root_name='Ab', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Ab', 'Bbm', 'Cm', 'Db', 'Eb', 'Fm', 'Gdim'], chords)

    def test_get_chords_for_frontend_a_flat_minor(self):
        key = Key(root_name='Ab', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Abm', 'Bbdim', 'Cb', 'Dbm', 'Ebm', 'E', 'Gb'], chords)

    def test_get_chords_for_frontend_d_flat_major(self):
        key = Key(root_name='Db', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Db', 'Ebm', 'Fm', 'Gb', 'Ab', 'Bbm', 'Cdim'], chords)

    def test_get_chords_for_frontend_d_flat_minor(self):
        key = Key(root_name='Db', mode=Mode.MINOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Dbm', 'Ebdim', 'E', 'Gbm', 'Abm', 'Bb', 'Cb'], chords)

    def test_get_chords_for_frontend_g_flat_major(self):
        key = Key(root_name='Gb', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Gb', 'Abm', 'Bbm', 'Cb', 'Db', 'Ebm', 'Fdim'], chords)

    def test_get_chords_for_frontend_c_flat_major(self):
        key = Key(root_name='Cb', mode=Mode.MAJOR)
        chords = _get_chords_for_frontend(key)
        self.assertEqual(['Cb', 'Dbm', 'Ebm', 'E', 'Gb', 'Abm', 'Bbdim'], chords)

    # Test get_relative_key ########################################
    def test_get_relative_c_major(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'A')
        self.assertEqual(relative.get_mode(), Mode.MINOR)

    def test_get_relative_g_major(self):
        key = Key(root_name='G', mode=Mode.MAJOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'E')
        self.assertEqual(relative.get_mode(), Mode.MINOR)

    def test_get_relative_d_major(self):
        key = Key(root_name='D', mode=Mode.MAJOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'B')
        self.assertEqual(relative.get_mode(), Mode.MINOR)

    def test_get_relative_a_major(self):
        key = Key(root_name='A', mode=Mode.MAJOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'F#')
        self.assertEqual(relative.get_mode(), Mode.MINOR)

    def test_get_relative_e_major(self):
        key = Key(root_name='E', mode=Mode.MAJOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'C#')
        self.assertEqual(relative.get_mode(), Mode.MINOR)

    def test_get_relative_f_major(self):
        key = Key(root_name='F', mode=Mode.MAJOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'D')
        self.assertEqual(relative.get_mode(), Mode.MINOR)

    def test_get_relative_b_flat_major(self):
        key = Key(root_name='Bb', mode=Mode.MAJOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'G')
        self.assertEqual(relative.get_mode(), Mode.MINOR)

    def test_get_relative_e_flat_major(self):
        key = Key(root_name='Eb', mode=Mode.MAJOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'C')
        self.assertEqual(relative.get_mode(), Mode.MINOR)

    def test_get_relative_a_flat_major(self):
        key = Key(root_name='Ab', mode=Mode.MAJOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'F')
        self.assertEqual(relative.get_mode(), Mode.MINOR)

    def test_get_relative_d_flat_major(self):
        key = Key(root_name='Db', mode=Mode.MAJOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'Bb')
        self.assertEqual(relative.get_mode(), Mode.MINOR)

    def test_get_relative_g_flat_major(self):
        key = Key(root_name='Gb', mode=Mode.MAJOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'Eb')
        self.assertEqual(relative.get_mode(), Mode.MINOR)

    def test_get_relative_c_flat_major(self):
        key = Key(root_name='Cb', mode=Mode.MAJOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'Ab')
        self.assertEqual(relative.get_mode(), Mode.MINOR)

    # Minors #####
    def test_get_relative_a_minor(self):
        key = Key(root_name='A', mode=Mode.MINOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'C')
        self.assertEqual(relative.get_mode(), Mode.MAJOR)

    def test_get_relative_e_minor(self):
        key = Key(root_name='E', mode=Mode.MINOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'G')
        self.assertEqual(relative.get_mode(), Mode.MAJOR)

    def test_get_relative_b_minor(self):
        key = Key(root_name='B', mode=Mode.MINOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'D')
        self.assertEqual(relative.get_mode(), Mode.MAJOR)

    def test_get_relative_f_sharp_minor(self):
        key = Key(root_name='F#', mode=Mode.MINOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'A')
        self.assertEqual(relative.get_mode(), Mode.MAJOR)

    def test_get_relative_c_sharp_minor(self):
        key = Key(root_name='C#', mode=Mode.MINOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'E')
        self.assertEqual(relative.get_mode(), Mode.MAJOR)

    def test_get_relative_d_minor(self):
        key = Key(root_name='D', mode=Mode.MINOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'F')
        self.assertEqual(relative.get_mode(), Mode.MAJOR)

    def test_get_relative_g_minor(self):
        key = Key(root_name='G', mode=Mode.MINOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'Bb')
        self.assertEqual(relative.get_mode(), Mode.MAJOR)

    def test_get_relative_c_minor(self):
        key = Key(root_name='C', mode=Mode.MINOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'Eb')
        self.assertEqual(relative.get_mode(), Mode.MAJOR)

    def test_get_relative_f_minor(self):
        key = Key(root_name='F', mode=Mode.MINOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'Ab')
        self.assertEqual(relative.get_mode(), Mode.MAJOR)

    def test_get_relative_b_flat_minor(self):
        key = Key(root_name='Bb', mode=Mode.MINOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'Db')
        self.assertEqual(relative.get_mode(), Mode.MAJOR)

    def test_get_relative_e_flat_minor(self):
        key = Key(root_name='Eb', mode=Mode.MINOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'Gb')
        self.assertEqual(relative.get_mode(), Mode.MAJOR)

    def test_get_relative_a_flat_minor(self):
        key = Key(root_name='Ab', mode=Mode.MINOR)
        relative = _get_relative_key(key)
        self.assertEqual(relative.get_traditional_root(), 'Cb')
        self.assertEqual(relative.get_mode(), Mode.MAJOR)

    # Test get_new_key ##########################################
    def test_get_new_key_happy_path(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        self.assertEqual(key.get_traditional_root(), 'C')
        self.assertEqual(key.get_mode(), Mode.MAJOR)
        key = get_new_key('D')
        self.assertEqual(key.get_traditional_root(), 'D')
        self.assertEqual(key.get_mode(), Mode.MAJOR)
        key = get_new_key('F#', Mode.MINOR)
        self.assertEqual(key.get_traditional_root(), 'F#')
        self.assertEqual(key.get_mode(), Mode.MINOR)

    def test_get_new_key_invalid_root(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        self.assertEqual(key.get_traditional_root(), 'C')
        self.assertEqual(key.get_mode(), Mode.MAJOR)
        key = get_new_key('Z')
        self.assertFalse(key.is_active())
        self.assertIsNone(key.get_traditional_root())

    # Test get_key_data ##########################################
    def test_get_key_data_relative_minor_and_blues(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        key_data = get_key_data(key)
        self.assertEqual(key_data.get('root'), 'C')
        self.assertEqual(key_data.get('mode'), Mode.MAJOR)
        self.assertEqual(key_data.get('scale'), ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'])
        self.assertTrue(key_data.get('has_minor'))
        self.assertTrue(key_data.get('has_blues'))
        self.assertEqual(key_data.get('relative').get_traditional_root(), 'A')
        self.assertEqual(key_data.get('relative').get_mode(), Mode.MINOR)

    def test_get_key_data_only_major_scale_no_blues(self):
        key = Key(root_name='Cb', mode=Mode.MAJOR)
        key_data = get_key_data(key)
        self.assertEqual(key_data.get('root'), 'Cb')
        self.assertEqual(key_data.get('mode'), Mode.MAJOR)
        self.assertEqual(key_data.get('scale'), ['Cb', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'Bb', 'Cb'])
        self.assertFalse(key_data.get('has_minor'))
        self.assertFalse(key_data.get('has_blues'))
        self.assertEqual(key_data.get('relative').get_traditional_root(), 'Ab')
        self.assertEqual(key_data.get('relative').get_mode(), Mode.MINOR)

    def test_get_key_data_no_relative_no_blues(self):
        key = Key(root_name='C#', mode=Mode.MAJOR)
        key_data = get_key_data(key)
        self.assertEqual(key_data.get('root'), 'C#')
        self.assertEqual(key_data.get('mode'), Mode.MAJOR)
        self.assertEqual(key_data.get('scale'), ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C', 'C#'])
        self.assertTrue(key_data.get('has_minor'))
        self.assertFalse(key_data.get('has_blues'))
        self.assertFalse(key_data.get('relative').is_active())

    # Test relative_is_available #####################################
    def test_relative_is_available_true(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        self.assertTrue(relative_is_available(key))

    def test_relative_is_available_false(self):
        key = Key(root_name='C#', mode=Mode.MAJOR)
        self.assertFalse(relative_is_available(key))

    # Test get_random_key ########################################
    def test_get_random_key(self):
        key = get_random_key()
        self.assertTrue(key.is_active())

    # Test get_current_mode ######################################
    def test_get_current_mode(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        self.assertEqual(get_current_mode(key), Mode.MAJOR)

    def test_get_current_mode_minor(self):
        key = Key(root_name='C', mode=Mode.MINOR)
        self.assertEqual(get_current_mode(key), Mode.MINOR)

    # Test get_key_name ##########################################
    def test_get_key_name_major(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        self.assertEqual(get_key_name(key), 'C Major')

    def test_get_key_name_minor(self):
        key = Key(root_name='C', mode=Mode.MINOR)
        self.assertEqual(get_key_name(key), 'C Minor')

    # Test is_valid_key ###########################################
    def test_is_valid_key_true(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        self.assertTrue(is_valid_key(key))

    def test_is_valid_key_false(self):
        key = Key()
        self.assertFalse(is_valid_key(key))

    # Test toggle_mode ##########################################
    def test_toggle_mode_major_to_minor(self):
        key = Key(root_name='C', mode=Mode.MAJOR)
        toggle_mode(key)
        self.assertEqual(key.get_mode(), Mode.MINOR)

    def test_toggle_mode_minor_to_major(self):
        key = Key(root_name='C', mode=Mode.MINOR)
        toggle_mode(key)
        self.assertEqual(key.get_mode(), Mode.MAJOR)


if __name__ == '__main__':
    unittest.main()
