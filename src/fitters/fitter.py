from abc import ABC, abstractmethod

from src.fitters.fit_strategy.ds_strategy import DSStrategy
from src.fitters.fit_strategy.goel_okumoto_strategy import GoelOkumotoStrategy
from src.fitters.fit_strategy.logistico_strategy import LogisticoStrategy


class Fitter(ABC):

    fit_strategy = {
        'goel-okumoto': GoelOkumotoStrategy(),
        'delayed-s-shaped': DSStrategy(),
        'logistico': LogisticoStrategy()
    }

    def get_estrategia_modelo(self, modelo):
        return self.fit_strategy.get(modelo)

    @abstractmethod
    def fit(self, modelo, nombre_proyecto, datos):
        pass
