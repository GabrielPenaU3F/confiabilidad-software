from data.data_repository import DataRepository
from src.fitters.fitter import Fitter
from src.plotter.plotter import Plotter


class TTFFitter(Fitter):

    """
    Accepted models
        Goel-Okumoto: 'goel-okumoto'
        Delayed S-Shaped: 'delayed-s-shaped'
        Logistic: 'logistic'
    """
    def fit(self, model, project_name):
        data = DataRepository.provide_observed_data_from_project(project_name)
        fit_strategy = self.get_model_strategy(model)
        lsq_params, ml_params = fit_strategy.fit_ttf(project_name, data)

        plotter = Plotter()
        plotter.plot(project_name, model, lsq_params, ml_params, data)



