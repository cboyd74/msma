import unittest
from unittest import TestCase

from src.model.command import Command
from src.model.input import Input, is_number_input, is_empty_input, is_cmd_input, str_to_cmd


class TestInput(TestCase):

    # Test Helpers ##############################################
    def test_is_number_input_happy(self):
        is_int = is_number_input("1")
        self.assertTrue(is_int)

    def test_is_number_input_fail(self):
        is_int = is_number_input("not_int")
        self.assertFalse(is_int)

    def test_is_empty_input_happy(self):
        inp = None
        is_empty = is_empty_input(inp)
        self.assertTrue(is_empty)
        inp = ""
        is_empty = is_empty_input(inp)
        self.assertTrue(is_empty)

    def test_is_empty_input_fail(self):
        is_empty = is_empty_input('not_empty')
        self.assertFalse(is_empty)

    def test_is_cmd_input_quit(self):
        is_cmd = is_cmd_input(Command.QUIT.value)
        self.assertTrue(is_cmd)

    def test_is_cmd_input_help(self):
        is_cmd = is_cmd_input(Command.HELP.value)
        self.assertTrue(is_cmd)

    def test_is_cmd_input_toggle_relative(self):
        is_cmd = is_cmd_input(Command.TOGGLE_RELATIVE.value)
        self.assertTrue(is_cmd)

    def test_is_cmd_input_toggle_mode(self):
        is_cmd = is_cmd_input(Command.TOGGLE_MODE.value)
        self.assertTrue(is_cmd)

    def test_is_cmd_input_toggle_blues(self):
        is_cmd = is_cmd_input(Command.TOGGLE_BLUES.value)
        self.assertTrue(is_cmd)

    def test_is_cmd_input_toggle_pentatonic(self):
        is_cmd = is_cmd_input(Command.TOGGLE_PENTATONIC.value)
        self.assertTrue(is_cmd)

    def test_str_to_cmd_quit(self):
        cmd = str_to_cmd(Command.QUIT.value)
        self.assertEqual(Command.QUIT, cmd)

    def test_str_to_cmd_help(self):
        cmd = str_to_cmd(Command.HELP.value)
        self.assertEqual(Command.HELP, cmd)

    def test_str_to_cmd_toggle_mode(self):
        cmd = str_to_cmd(Command.TOGGLE_MODE.value)
        self.assertEqual(Command.TOGGLE_MODE, cmd)

    def test_str_to_cmd_toggle_relative(self):
        cmd = str_to_cmd(Command.TOGGLE_RELATIVE.value)
        self.assertEqual(Command.TOGGLE_RELATIVE, cmd)

    def test_str_to_cmd_toggle_pentatonic(self):
        cmd = str_to_cmd(Command.TOGGLE_PENTATONIC.value)
        self.assertEqual(Command.TOGGLE_PENTATONIC, cmd)

    def test_str_to_cmd_toggle_blues(self):
        cmd = str_to_cmd(Command.TOGGLE_PENTATONIC.value)
        self.assertEqual(Command.TOGGLE_PENTATONIC, cmd)

    # Test set_input #############################################
    def test_set_input_empty(self):
        input_obj = Input()
        input_obj.set_input(None)
        self.assertTrue(input_obj.is_empty())
        input_obj.set_input('')
        self.assertTrue(input_obj.is_empty())

    def test_set_input_cmd_quit(self):
        input_obj = Input()
        input_obj.set_input(Command.QUIT.value)
        self.assertTrue(input_obj.is_cmd())
        self.assertEqual(input_obj.get_value(), Command.QUIT)

    def test_set_input_cmd_help(self):
        input_obj = Input()
        input_obj.set_input(Command.HELP.value)
        self.assertTrue(input_obj.is_cmd())
        self.assertEqual(input_obj.get_value(), Command.HELP)

    def test_set_input_cmd_toggle_mode(self):
        input_obj = Input()
        input_obj.set_input(Command.TOGGLE_MODE.value)
        self.assertTrue(input_obj.is_cmd())
        self.assertEqual(input_obj.get_value(), Command.TOGGLE_MODE)

    def test_set_input_cmd_toggle_relative(self):
        input_obj = Input()
        input_obj.set_input(Command.TOGGLE_RELATIVE.value)
        self.assertTrue(input_obj.is_cmd())
        self.assertEqual(input_obj.get_value(), Command.TOGGLE_RELATIVE)

    def test_set_input_cmd_toggle_pentatonic(self):
        input_obj = Input()
        input_obj.set_input(Command.TOGGLE_PENTATONIC.value)
        self.assertTrue(input_obj.is_cmd())
        self.assertEqual(input_obj.get_value(), Command.TOGGLE_PENTATONIC)

    def test_set_input_cmd_toggle_blues(self):
        input_obj = Input()
        input_obj.set_input(Command.TOGGLE_BLUES.value)
        self.assertTrue(input_obj.is_cmd())
        self.assertEqual(input_obj.get_value(), Command.TOGGLE_BLUES)

    def test_set_input_int(self):
        input_obj = Input()
        input_obj.set_input('1')
        self.assertTrue(input_obj.is_int())
        self.assertEqual(input_obj.get_value(), 1)

    def test_set_input_string(self):
        input_obj = Input()
        input_obj.set_input('string')
        self.assertTrue(input_obj.is_string())
        self.assertEqual(input_obj.get_value(), 'string')


if __name__ == '__main__':
    unittest.main()
