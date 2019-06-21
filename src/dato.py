class Dato:

    def __init__(self, n, t):
        self.numero_falla = n
        self.tiempo_falla = t

    def get_tiempo(self):
        return self.tiempo_falla

    def get_numero(self):
        return self.numero_falla
