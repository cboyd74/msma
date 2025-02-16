import unittest
from unittest import TestCase

from src.model.key import Key
from src.model.mode import Mode


class TestKey(TestCase):

    # Test Constructor ###########################################
    def test_constructor_no_key(self):
        key = Key()
        self.assertIsNotNone(key)
        self.assertFalse(key.is_active())

    # Passing bad key, get inactive
    def test_constructor_bad_key(self):
        key = Key('invalid')
        self.assertIsNotNone(key)
        self.assertFalse(key.is_active())

    def test_constructor_no_key_mode(self):
        key = Key(mode=Mode.MINOR)
        self.assertIsNotNone(key)
        self.assertFalse(key.is_active())

    # Pass in good key, get good key
    def test_constructor_default(self):
        key = Key('C')
        self.assertIsNotNone(key)
        self.assertTrue(key.is_active())
        self.assertEqual('C', key.get_root())
        self.assertEqual('C', key.get_traditional_root())
        self.assertEqual(Mode.MAJOR.value, key.get_mode().value)

    def test_constructor_minor(self):
        key = Key('C', Mode.MINOR)
        self.assertIsNotNone(key)
        self.assertTrue(key.is_active())
        self.assertEqual('C', key.get_root())
        self.assertEqual('C', key.get_traditional_root())
        self.assertEqual(Mode.MINOR.value, key.get_mode().value)

    # Test toggle_mode ##########################################
    def test_toggle_mode_to_minor(self):
        key = Key('C')
        self.assertIsNotNone(key)
        self.assertTrue(key.is_active())
        self.assertEqual(Mode.MAJOR.value, key.get_mode().value)
        key.toggle_mode()
        self.assertEqual(Mode.MINOR.value, key.get_mode().value)

    def test_set_mode_to_major(self):
        key = Key('C', Mode.MINOR)
        self.assertIsNotNone(key)
        self.assertTrue(key.is_active())
        self.assertEqual(Mode.MINOR.value, key.get_mode().value)
        key.toggle_mode()
        self.assertEqual(Mode.MAJOR.value, key.get_mode().value)


if __name__ == '__main__':
    unittest.main()
