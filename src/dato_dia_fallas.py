class DatoDiaFallas:

    def __init__(self, dia, fallas):
        self.numero_dia = dia
        self.fpd = fallas

    def get_dia(self):
        return self.numero_dia

    def get_cantidad_de_fallas(self):
        return self.fpd
