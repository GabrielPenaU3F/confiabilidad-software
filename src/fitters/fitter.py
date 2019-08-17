from abc import ABC, abstractmethod

from src.domain.fit import Fit
from src.fitters.fit_strategy.ds_fit_strategy import DSFitStrategy
from src.fitters.fit_strategy.goel_okumoto_fit_strategy import GoelOkumotoFitStrategy
from src.fitters.fit_strategy.logistic_fit_strategy import LogisticFitStrategy


class Fitter(ABC):

    fit_strategy = {
        'goel-okumoto': GoelOkumotoFitStrategy,
        'delayed-s-shaped': DSFitStrategy,
        'logistic': LogisticFitStrategy
    }

    def get_model_strategy(self, model):
        return self.fit_strategy.get(model)


    """
    Accepted models
        Goel-Okumoto: 'goel-okumoto'
        Delayed S-Shaped: 'delayed-s-shaped'
        Logistic: 'logistic'
    """
    def fit(self, model, project_name):

        fit_strategy = self.get_model_strategy(model)(project_name)
        lsq_params, ml_params = self.choose_fitter(fit_strategy)

        return Fit(project_name, model, fit_strategy, lsq_params, ml_params)

    @abstractmethod
    def choose_fitter(self, fit_strategy):
        pass


class TTFFitter(Fitter):

    def choose_fitter(self, fit_strategy):
        return fit_strategy.fit_ttf()


class GroupedCumulativeFitter(Fitter):

    def choose_fitter(self, fit_strategy):
        return fit_strategy.fit_grouped_cumulative()

