from abc import ABC, abstractmethod


class PlotStrategy(ABC):

    @abstractmethod
    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        pass

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

    def show_mt_warning(self):
        pass
