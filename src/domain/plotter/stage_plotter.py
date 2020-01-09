from src.domain.plotter.plotter import Plotter


class StagePlotter(Plotter):

    def plot_results(self, axes, stage, times, cumulative_failures, **kwargs):
        plot_strategy = self.get_model_strategy(stage.get_model())()
        initial_sample = self.determine_initial_sample(times, stage.get_initial_t())
        end_sample = self.determine_end_sample(times, stage.get_end_t())
        times = times[initial_sample:end_sample + 1]
        cumulative_failures = cumulative_failures[initial_sample:end_sample]
        plot_strategy.plot(axes, times, cumulative_failures, stage.get_lsq_params(), stage.get_ml_params(), **kwargs)

    def plot_mttf(self, *args):
        pass

    def plot_mtbf(self, *args):
        pass

    def determine_end_sample(self, times, end_t):
        for i in range(len(times)):
            if times[i] > end_t:
                return i - 1
        return len(times) - 1

    def determine_initial_sample(self, times, initial_t):
        for i in range(len(times)):
            if times[i] >= initial_t:
                return i
