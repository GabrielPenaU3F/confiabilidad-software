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
    def fit(self, model, project_name, **kwargs):

        fit_strategy = self.get_model_strategy(model)(project_name)
        try:
            lsq_params, ml_params = self.choose_fitter(fit_strategy, **kwargs)
            return Fit(project_name, model, fit_strategy, lsq_params, ml_params, **kwargs)
        except TypeError:
            return Fit(None, None, None, None, None)

    @abstractmethod
    def choose_fitter(self, fit_strategy, **kwargs):
        pass


class TTFFitter(Fitter):

    def choose_fitter(self, fit_strategy, **kwargs):
        return fit_strategy.fit_ttf(**kwargs)


class GroupedCumulativeFitter(Fitter):

    def choose_fitter(self, fit_strategy, **kwargs):
        return fit_strategy.fit_grouped_cumulative(**kwargs)


class GroupedFailuresPerDayFitter(Fitter):

    def choose_fitter(self, fit_strategy, **kwargs):
        return fit_strategy.fit_grouped_fpd(**kwargs)
