from abc import abstractmethod, ABC


class FitStrategy(ABC):

    @abstractmethod
    def fit_ttf(self, nombre_proyecto, datos):
        pass

    @abstractmethod
    def fit_agrupados_acum(self, nombre_proyecto, datos):
        pass

    @abstractmethod
    def fit_agrupados_fpd(self, nombre_proyecto, datos):
        pass

    @abstractmethod
    def validar_formato(self, datos):
        pass
