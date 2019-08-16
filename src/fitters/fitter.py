from abc import ABC, abstractmethod

from src.fitters.fit_strategy.ds_fit_strategy import DSFitStrategy
from src.fitters.fit_strategy.goel_okumoto_fit_strategy import GoelOkumotoFitStrategy
from src.fitters.fit_strategy.logistic_fit_strategy import LogisticFitStrategy
from src.plotter.plotter import Plotter
from src.result_presenter.result_presenter import ResultPresenter


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

        prr_lsq = fit_strategy.calculate_prr(*lsq_params)
        prr_ml = fit_strategy.calculate_prr(*ml_params)
        aic = fit_strategy.calculate_aic_ttf(*ml_params)

        presenter = ResultPresenter()
        presenter.display_data(project_name, model, lsq_params, ml_params, prr_lsq, prr_ml, aic)

        plotter = Plotter()
        plotter.plot(project_name, model, lsq_params, ml_params)

    @abstractmethod
    def choose_fitter(self, fit_strategy):
        pass
