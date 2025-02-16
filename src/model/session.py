from src.model.input import Input
from src.model.key import Key
from src.service.music_interface import get_new_key, is_valid_key

STANDARD_BUFFER = 2


class Session:
    """
    Session class is used to store the current state of the application.
    """

    def __init__(self, writer):
        self.writer = writer
        self.selected_key: Key = Key()
        self.pentatonic: bool = False
        self.blues: bool = False
        self.height: int = 0
        self.width: int = 0
        self.input_x: int = 0
        self.input_y: int = 0
        self.previous_input = None

    def get_writer(self):
        """
        Retrieves the writer.
        :return:
        """
        return self.writer

    def set_previous_input(self, input_obj: Input):
        """
        Sets the previous input.
        :param input_obj:
        :return:
        """
        self.previous_input = input_obj

    def get_previous_input(self) -> Input:
        """
        Retrieves the previous input.
        :return:
        """
        return self.previous_input

    def set_key(self, key: Key):
        """
        Sets the selected key.
        :param key:
        :return:
        """
        self.selected_key = key

    def get_key(self) -> Key:
        """
        Retrieves the selected key.
        :return:
        """
        return self.selected_key

    def is_pentatonic(self):
        """
        Checks if the key is pentatonic.

        :return: bool - True if key is pentatonic, else False
        """
        return self.pentatonic

    def toggle_pentatonic(self):
        """
        Toggles the pentatonic status of the key.
        """
        self.pentatonic = not self.pentatonic
        self.blues = False

    def is_blues(self):
        """
        Checks if the key is blues.
        :return:
        """
        return self.blues

    def toggle_blues(self):
        """
        Toggles the blues status of the key.
        """
        self.blues = not self.blues
        self.pentatonic = False

    def set_dimensions(self, height, width):
        """
        Sets the dimensions of the screen.
        :param height:
        :param width:
        :return:
        """
        self.height = height - 1
        self.width = width - 1
        start_x, _ = self.get_x_min_max_safe()
        _, end_y = self.get_y_min_max_safe()
        self.input_x = start_x + 1
        self.input_y = end_y

    def get_height_width(self) -> (int, int):
        """
        Retrieves the height and width of the screen.
        :return:
        """
        return self.height, self.width

    def get_input_y_x(self) -> (int, int):
        """
        Retrieves the input y and x positions.
        :return:
        """
        return self.input_y, self.input_x

    # min_y, max_y, min_x, max_x
    def get_y_x_min_max(self) -> (int, int, int, int):
        """
        Retrieves the min and max y and x positions.
        :return:
        """
        return 2, self.height - 2, 2, self.width - 2

    def get_y_x_min_max_safe(self) -> (int, int, int, int):
        """
        Retrieves the min and max y and x positions with a buffer.
        :return:
        """
        min_y, max_y = self.get_y_min_max_safe()
        min_x, max_x = self.get_x_min_max_safe()
        return min_y, max_y, min_x, max_x

    def get_x_min_max_safe(self) -> (int, int):
        """
        Retrieves the min and max x positions with a buffer.
        :return:
        """
        _, _, min_x, max_x = self.get_y_x_min_max()
        return min_x + 2, max_x - 2

    def get_y_min_max_safe(self) -> (int, int):
        """
        Retrieves the min and max y positions with a buffer.
        :return:
        """
        min_y, max_y, _, _ = self.get_y_x_min_max()
        return min_y + 2, max_y - 2


class Component:
    """
    Component class is used to store the position of a component on the screen.
    """

    def __init__(self, start_y: int, end_y: int, start_x: int, end_x: int):
        """
        Constructor
        :param start_y:
        :param end_y:
        :param start_x:
        :param end_x:
        """
        self.start_y = start_y
        self.end_y = end_y
        self.start_x = start_x
        self.end_x = end_x

    def get_start_y(self):
        """
        Retrieves the start y position.
        :return:
        """
        return self.start_y

    def set_start_y(self, start_y):
        """
        Sets the start y position.
        :param start_y:
        :return:
        """
        self.start_y = start_y

    def get_end_y(self):
        """
        Retrieves the end y position.
        :return:
        """
        return self.end_y

    def set_end_y(self, end_y):
        """
        Sets the end y position.
        :param end_y:
        :return:
        """
        self.end_y = end_y

    def get_start_x(self):
        """
        Retrieves the start x position.
        :return:
        """
        return self.start_x

    def get_end_x(self):
        """
        Retrieves the end x position.
        :return:
        """
        return self.end_x

    def get_width(self):
        """
        Retrieves the width of the component.
        :return:
        """
        return self.end_x - self.start_x
