import numpy as np
from matplotlib import pyplot as plt

from src.data.data_repository import DataRepository
from src.domain.plotter.plotter import Plotter


class ModelPlotter(Plotter):

    def plot_results(self, project_name, model, lsq_params, ml_params):
        data = DataRepository.provide_project_data(project_name)
        project_title = data.get_project_title()
        x_axis_data = data.get_times()
        cumulative_failures = data.get_cumulative_failures()
        fig, axes = plt.subplots()
        self.plot_real_data(axes, x_axis_data, cumulative_failures, project_title)
        plot_strategy = self.get_model_strategy(model)()
        plot_strategy.plot(axes, x_axis_data, cumulative_failures, lsq_params, ml_params)
        plt.show()

    def plot_mttf(self, mttf):
        fig, axes = plt.subplots()
        failures = np.linspace(1, len(mttf), len(mttf))
        axes.set_ylabel('MTTF')
        axes.scatter(failures, mttf, s=4.0, color='#ca3e47', label='MTTF')
        self.do_format_mt_plot(axes)

    def plot_mtbf(self, mtbf):
        fig, axes = plt.subplots()
        failures = np.linspace(1, len(mtbf), len(mtbf))
        axes.set_ylabel('MTBF')
        axes.scatter(failures, mtbf, s=4.0, color='#ca3e47', label='MTBF')
        self.do_format_mt_plot(axes)

    def show_mt_warning(self, model):
        strategy = self.get_model_strategy(model)()
        strategy.show_mt_warning()
