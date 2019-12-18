from src.data.data_repository import DataRepository
from src.domain.fitters.optional_arguments import OptionalArguments
from src.domain.plotter.plotter import Plotter
from src.domain.result_presenter.result_presenter import ResultPresenter


class Fit:

    project_name = None
    mttf = None

    def __init__(self, project_name, model_name, fit_strategy, lsq_params, ml_params, optional_arguments):
        if project_name is not None:
            data_object = fit_strategy.get_data()
            format_strategy = fit_strategy.get_format_strategy()
            self.project_name = project_name
            self.times = self.determine_times(data_object, optional_arguments, format_strategy)
            self.data = self.determine_data(project_name, optional_arguments, format_strategy)
            self.model = model_name
            self.fit_strategy = fit_strategy
            self.lsq_params = lsq_params
            self.ml_params = ml_params
            self.prr_lsq = fit_strategy.calculate_prr(*lsq_params)
            if ml_params is not None:
                self.prr_ml = fit_strategy.calculate_prr(*ml_params)
                self.aic = fit_strategy.calculate_aic(*ml_params)
                if optional_arguments.get_mts_flag() is True:
                    self.mttf = fit_strategy.calculate_mttfs(*ml_params)
            else:
                self.prr_ml = None
                self.aic = None
                if optional_arguments.get_mts_flag() is True:
                    self.mttf = fit_strategy.calculate_mttfs(*lsq_params)
            if self.mttf is not None:
                self.mtbf = fit_strategy.calculate_mtbfs(self.mttf)

    def show_results(self, **kwargs):
        if self.project_name is not None:
            presenter = ResultPresenter()
            presenter.display_data(self.project_name, self.model,
                                   self.lsq_params, self.ml_params, self.prr_lsq, self.prr_ml, self.aic)

            plotter = Plotter()
            plotter.plot_results(self.project_name, self.model, self.lsq_params, self.ml_params)
            if kwargs.get("plot_mttf") is True:
                plotter.show_mt_warning(self.model, self.project_name)
                plotter.plot_mttf(self.mttf)
            if kwargs.get("plot_mtbf") is True:
                plotter.show_mt_warning(self.model, self.project_name)
                plotter.plot_mtbf(self.mtbf)

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

    def get_all_mttf(self):
        return self.mttf

    def get_all_mtbf(self):
        return self.mtbf

    def get_mttf(self, k):
        return self.mttf[k-1]

    def get_mtbf(self, k):
        return self.mtbf[k-1]

    def get_times(self):
        return self.times

    def get_data(self):
        return self.data

    def determine_times(self, data, optional_arguments, format_strategy):
        times = data.get_times()
        times[0] = optional_arguments.get_x0()
        return times

    def determine_data(self, project_name, optional_arguments, format_strategy):
        pass
