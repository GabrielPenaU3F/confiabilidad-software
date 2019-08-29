from abc import ABC, abstractmethod

from colorama import Back, Fore

from src.domain.fit import Fit
from src.fitters.fit_strategy.ds_fit_strategy import DSFitStrategy
from src.fitters.fit_strategy.goel_okumoto_fit_strategy import GoelOkumotoFitStrategy
from src.fitters.fit_strategy.logistic_fit_strategy import LogisticFitStrategy
from src.fitters.format_strategy.grouped_cumulative_format_strategy import GroupedCumulativeFormatStrategy
from src.fitters.format_strategy.grouped_fpd_format_strategy import GroupedFPDFormatStrategy
from src.fitters.format_strategy.ttf_format_strategy import TTFFormatStrategy


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
            format_strategy = self.choose_format_strategy(fit_strategy.get_data(), fit_strategy.get_model())
            lsq_params, ml_params = fit_strategy.fit_model(format_strategy, **kwargs)
            return Fit(project_name, model, fit_strategy, lsq_params, ml_params, **kwargs)
        except TypeError as error:
            print(Back.LIGHTYELLOW_EX + Fore.RED + str(error))
            return Fit(None, None, None, None, None)

    @abstractmethod
    def choose_format_strategy(self, data, model):
        pass


class TTFFitter(Fitter):

    def choose_format_strategy(self, data, model):
        return TTFFormatStrategy(data, model)


class GroupedCumulativeFitter(Fitter):

    def choose_format_strategy(self, data, model):
        return GroupedCumulativeFormatStrategy(data, model)


class GroupedFailuresPerDayFitter(Fitter):

    def choose_format_strategy(self, data, model):
        return GroupedFPDFormatStrategy(data, model)
