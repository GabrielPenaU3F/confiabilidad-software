from src.domain.plotter.plotter import Plotter


class StagePlotter(Plotter):

    def plot_results(self, stage, axes):
        plot_strategy = self.get_model_strategy(stage.get_model())()
        plot_strategy.plot(axes, stage.get_lsq_params(), stage.get_ml_params())

    def plot_mttf(self, *args):
        pass

    def plot_mtbf(self, *args):
        pass
