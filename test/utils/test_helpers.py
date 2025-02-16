import unittest
from unittest import TestCase

from util.helpers import is_sharp, is_flat


class TestHelpers(TestCase):

    # Test is_sharp/is_flat ########################################
    def test_is_sharp(self):
        self.assertTrue(is_sharp('C#'))
        self.assertFalse(is_sharp('C'))
        self.assertTrue(is_sharp('C#m'))
        self.assertFalse(is_sharp(''))
        self.assertFalse(is_sharp(None))

    def test_is_flat(self):
        self.assertTrue(is_flat('Cb'))
        self.assertFalse(is_flat('C'))
        self.assertTrue(is_flat('Cbm'))
        self.assertFalse(is_flat(''))
        self.assertFalse(is_flat(None))


if __name__ == '__main__':
    unittest.main()

