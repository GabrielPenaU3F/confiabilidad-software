from abc import ABC, abstractmethod
from matplotlib import pyplot as plt

from data.data_repository import DataRepository


class PlotStrategy(ABC):

    def __init__(self, project_name):
        self.project_name = project_name
        self.data = DataRepository.provide_project_data(project_name)

    @abstractmethod
    def plot(self, project_name, lsq_params, ml_params):
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
