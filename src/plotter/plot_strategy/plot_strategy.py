from abc import ABC, abstractmethod
from matplotlib import pyplot as plt

from src.data.data_repository import DataRepository


class PlotStrategy(ABC):

    def __init__(self, project_name):
        self.project_name = project_name
        self.data = DataRepository.provide_project_data(project_name)

    @abstractmethod
    def plot(self, project_name, lsq_params, ml_params):
        pass

    def plot_real_data(self, axes, x_data, cumulative_failures, project_title):
        axes.plot(x_data, cumulative_failures, linewidth=1, color='#263859', linestyle='--',
                  label='Real data (' + project_title + ')')

    @abstractmethod
    def plot_least_squares(self, axes, model, x_data, lsq_params):
        pass

    @abstractmethod
    def plot_maximum_likelihood(self, axes, model, x_data, ml_params):
        pass

    def do_plot_format(self, axes):
        axes.set_xlabel('Time (days)')
        axes.set_ylabel('Number of failures')
        axes.set_xlim(left=0, auto=True)
        axes.set_ylim(auto=True)
        axes.patch.set_facecolor("#ffffff")
        axes.patch.set_edgecolor('black')
        axes.patch.set_linewidth('1')
        axes.set_facecolor("#ffffff")
        axes.grid(color='black', linestyle='--', linewidth=0.5)
        axes.legend()
        plt.show()
