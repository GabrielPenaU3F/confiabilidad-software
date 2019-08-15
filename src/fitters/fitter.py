from abc import ABC, abstractmethod

from src.fitters.fit_strategy.ds_fit_strategy import DSFitStrategy
from src.fitters.fit_strategy.goel_okumoto_fit_strategy import GoelOkumotoFitStrategy
from src.fitters.fit_strategy.logistico_fit_strategy import LogisticoFitStrategy


class Fitter(ABC):

    fit_strategy = {
        'goel-okumoto': GoelOkumotoFitStrategy(),
        'delayed-s-shaped': DSFitStrategy(),
        'logistico': LogisticoFitStrategy()
    }

    def get_estrategia_modelo(self, modelo):
        return self.fit_strategy.get(modelo)

    @abstractmethod
    def fit(self, modelo, nombre_proyecto):
        pass
