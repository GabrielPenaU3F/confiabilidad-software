from abc import ABC, abstractmethod

from src.fitters.fit_strategy.ds_fit_strategy import DSFitStrategy
from src.fitters.fit_strategy.goel_okumoto_fit_strategy import GoelOkumotoFitStrategy
from src.fitters.fit_strategy.logistic_fit_strategy import LogisticFitStrategy


class Fitter(ABC):

    fit_strategy = {
        'goel-okumoto': GoelOkumotoFitStrategy(),
        'delayed-s-shaped': DSFitStrategy(),
        'logistic': LogisticFitStrategy()
    }

    def get_model_strategy(self, model):
        return self.fit_strategy.get(model)

    @abstractmethod
    def fit(self, model, project_name):
        pass
