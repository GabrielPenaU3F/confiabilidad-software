from src.plotter.plotter import Plotter
from src.result_presenter.result_presenter import ResultPresenter


class Fit:

    project_name = None

    def __init__(self, project_name, model_name, fit_strategy, lsq_params, ml_params, **kwargs):
        if project_name is not None:
            self.project_name = project_name
            self.model = model_name
            self.fit_strategy = fit_strategy
            self.lsq_params = lsq_params
            self.ml_params = ml_params
            self.prr_lsq = fit_strategy.calculate_prr(*lsq_params)
            self.prr_ml = fit_strategy.calculate_prr(*ml_params)
            self.aic = fit_strategy.calculate_aic(*ml_params)

    def show_results(self):
        if self.project_name is not None:
            presenter = ResultPresenter()
            presenter.display_data(self.project_name, self.model,
                                   self.lsq_params, self.ml_params, self.prr_lsq, self.prr_ml, self.aic)

            plotter = Plotter()
            plotter.plot(self.project_name, self.model, self.lsq_params, self.ml_params)

    def get_lsq_parameters(self):
        return self.lsq_params

    def get_ml_parameters(self):
        return self.ml_params

    def get_prr_lsq(self):
        return self.prr_lsq

    def get_prr_ml(self):
        return self.prr_ml

    def get_aic(self):
        return self.aic
