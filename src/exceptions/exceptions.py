class ExceptionWithMessage(Exception):

    def __init__(self, arg):
        self.strerror = arg
        self.args = tuple(arg)


class NotAdmittedFormatException(ExceptionWithMessage):

    pass


class InvalidArgumentException(ExceptionWithMessage):

    pass


class InvalidFitException(ExceptionWithMessage):

    pass

