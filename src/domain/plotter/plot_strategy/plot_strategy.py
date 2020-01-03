from abc import ABC, abstractmethod


class PlotStrategy(ABC):

    def __init__(self):
        self.estimator = None

    @abstractmethod
    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        self.plot_least_squares(axes, self.estimator, times, lsq_params)
        self.plot_maximum_likelihood(axes, self.estimator, times, ml_params)
        self.do_plot_format(axes)

    def plot_maximum_likelihood(self, axes, go, x_data, ml_params):
        if ml_params is not None:
            axes.plot(x_data, go.calculate_mean_failure_numbers(x_data, *ml_params),
                      linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood')

    def plot_least_squares(self, axes, go, x_data, lsq_params):
        axes.plot(x_data, go.calculate_mean_failure_numbers(x_data, *lsq_params),
                  linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')

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
