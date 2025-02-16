from enum import Enum

from src.model.command import Command
from src.util.helpers import get_traditional_roots


class InputType(Enum):
    """
    Enum for input types
    """
    CMD = "cmd"
    CHANGE_KEY = "change_key"
    USER_STR = "user_string"
    USER_INT = "user_number"
    EMPTY = "empty"
    ERROR = "error"


class Input:
    """
    Class to handle input from the user
    """

    def __init__(self):
        """
        Constructor
        """
        self.value = None
        self.actual_type = InputType.EMPTY

    def set_input(self, input_str: str = None):
        """
        Set the input string, determine the type

        :param input_str: str - input string
        :return: Input
        """
        if is_empty_input(input_str):
            self.actual_type = InputType.EMPTY
        # if input is in list of commands, set type to CMD, set value
        elif is_cmd_input(input_str):
            self.actual_type = InputType.CMD
            self.value = str_to_cmd(input_str)
        # if input is a key, set type to CHANGE_KEY, set value
        elif is_valid_key(input_str):
            self.actual_type = InputType.CHANGE_KEY
            self.value = input_str
        # if is a number, cast to number
        elif is_number_input(input_str):
            self.actual_type = InputType.USER_INT
            self.value = int(input_str)
        # otherwise is a string
        else:
            self.actual_type = InputType.USER_STR
            self.value = input_str

    def raise_error(self):
        """
        Set input as error
        :return:
        """
        self.actual_type = InputType.ERROR

    def get_value(self):
        """
        Get the value of the input
        :return:
        """
        return self.value

    def is_error(self):
        """
        Check if input is an error
        :return:
        """
        return self.actual_type == InputType.ERROR

    def is_empty(self):
        """
        Check if input is empty
        :return:
        """
        return self.actual_type == InputType.EMPTY

    def is_cmd(self):
        """
        Check if input is a command
        :return:
        """
        return self.actual_type == InputType.CMD

    def is_string(self):
        """
        Check if input is a string
        :return:
        """
        return self.actual_type == InputType.USER_STR

    def is_int(self):
        """
        Check if input is an int
        :return:
        """
        return self.actual_type == InputType.USER_INT

    def is_update_key(self):
        """
        Check if input is an update key
        :return:
        """
        return self.actual_type == InputType.CHANGE_KEY


def is_number_input(input_str: str):
    """
    Check if input is a number
    :param input_str:
    :return:
    """
    try:
        int(input_str)
    except ValueError:
        return False
    return True


def is_empty_input(input_str: str):
    """
    Check if input is empty
    :param input_str:
    :return:
    """
    return input_str is None or input_str == ""


def is_cmd_input(input_str: str):
    """
    Check if input is a command
    :param input_str:
    :return:
    """
    try:
        if input_str in [cmd.value for cmd in Command]:
            return True
    except ValueError:
        pass
    return False


def str_to_cmd(input_str: str) -> Command:
    """
    Convert string to command
    :param input_str:
    :return:
    """
    ret_cmd = None
    for cmd in Command:
        if cmd.value == input_str:
            ret_cmd = cmd
    return ret_cmd


def is_valid_key(input_str: str) -> bool:
    """
    Determines if a given key is valid.
    :param key:
    :return:
    """
    return input_str in get_traditional_roots()
