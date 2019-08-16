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
        fit_strategy = self.get_model_strategy(model)(project_name)
        lsq_params, ml_params = fit_strategy.fit_ttf()

        plotter = Plotter()
        plotter.plot(project_name, model, lsq_params, ml_params)

        prr = fit_strategy.calculate_prr()

        #presenter = ResultPresenter()
        #presenter.display_data(model, lsq_params, ml_params, prr, aic)



