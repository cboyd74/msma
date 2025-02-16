from src.config.constants import TRADITIONAL_FLAT_TO_SHARP
from src.model.mode import Mode
from src.util.helpers import get_traditional_roots, is_flat


class Key:
    """
    Key class that holds all the information about a key
    """

    def __init__(self, root_name: str = None, mode: Mode = Mode.MAJOR):
        """
        Initializes the key with the root note and mode.
        If root_name is provided, it will be used as the root note.
        Else if root_idx is provided, it will be used to get the root note from the possible roots list.
        Else will initialize the key as empty and inactive.

        :param root_name: str - optional name of the root note
        :param mode: - optional mode of the key, defaults to major
        """
        root = None
        if root_name and root_name in get_traditional_roots():
            root = TRADITIONAL_FLAT_TO_SHARP.get(root_name) if is_flat(root_name) else root_name
        self.root = root
        self.traditional_root = root_name

        if self.root:
            self.active = True
            self.mode = mode  # defaults to major
        else:
            self.active = False
            self.mode = None

    def is_active(self):
        """
        Checks if the key is active.
        :return: bool - True if key is active, else False
        """
        return self.active

    def get_root(self):
        """
        Retrieves the root note of the current key.

        :return: str - root note of the key
        """
        return self.root

    def get_traditional_root(self):
        """
        Retrieves the traditional root note of the current key.

        :return: str - traditional root note of the key
        """
        return self.traditional_root

    def get_mode(self):
        """
        Retrieves the mode of the current key.

        :return: Mode - current mode of the key
        """
        return self.mode

    def toggle_mode(self):
        """
        Sets the mode of the current key.

        """
        self.mode = Mode.MAJOR if self.mode.value == Mode.MINOR.value else Mode.MINOR

