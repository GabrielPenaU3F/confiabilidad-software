from abc import ABC, abstractmethod


class PlotStrategy(ABC):

    def __init__(self):
        self.estimator = None

    @abstractmethod
    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        self.plot_least_squares(axes, self.estimator, times, lsq_params)
        self.plot_maximum_likelihood(axes, self.estimator, times, ml_params)
        self.do_plot_format(axes)

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
