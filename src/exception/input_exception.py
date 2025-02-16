class InputException(Exception):
    """
    Base class for input exceptions
    """
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_message(self):
        return self.message


class InvalidInputException(InputException):
    """
    Exception for invalid input
    """
    def __init__(self, message):
        super().__init__(message)


class EmptyInputException(InputException):
    """
    Exception for empty input
    """
    def __init__(self, message):
        super().__init__(message)


class InvalidCommandException(InputException):
    """
    Exception for invalid command use
    """
    def __init__(self, message):
        super().__init__(message)
