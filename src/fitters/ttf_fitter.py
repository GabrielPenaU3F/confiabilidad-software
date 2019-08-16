from data.data_repository import DataRepository
from src.fitters.fitter import Fitter
from src.plotter.plotter import Plotter
from src.result_presenter.result_presenter import ResultPresenter


class TTFFitter(Fitter):

    """
    Accepted models
        Goel-Okumoto: 'goel-okumoto'
        Delayed S-Shaped: 'delayed-s-shaped'
        Logistic: 'logistic'
    """
    def fit(self, model, project_name):
        fit_strategy = self.get_model_strategy(model)
        lsq_params, ml_params = fit_strategy.fit_ttf(project_name)

        plotter = Plotter()
        plotter.plot(project_name, model, lsq_params, ml_params)

        prr = fit_strategy.calculate_prr(project_name)

        #presenter = ResultPresenter()
        #presenter.display_data(model, lsq_params, ml_params, prr, aic)



