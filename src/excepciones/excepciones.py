class FormatoNoAdmitidoException(Exception):

    def __init__(self, arg):
        self.strerror = arg
        self.args = tuple(arg)


