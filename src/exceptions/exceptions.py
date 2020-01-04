class ExceptionWithMessage(Exception):

    def __init__(self, arg):
        self.strerror = str(arg)
        self.args = tuple(arg)
        super().__init__()


class NotAdmittedFormatException(ExceptionWithMessage):

    pass


class InvalidArgumentException(ExceptionWithMessage):

    pass


class InvalidFitException(ExceptionWithMessage):

    pass


class InvalidStageDefinitionException(ExceptionWithMessage):

    pass

