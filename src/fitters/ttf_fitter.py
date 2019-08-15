from src.fitters.fitter import Fitter


class TTFFitter(Fitter):

    """
    Modelos aceptados
        Goel-Okumoto: 'goel-okumoto'
        Delayed S-Shaped: 'delayed-s-shaped'
        Logístico: 'logistico'
    """
    def fit(self, modelo, nombre_proyecto, datos):
        fit_strategy = self.get_estrategia_modelo(modelo)
        fit_strategy.fit_ttf(nombre_proyecto, datos)

