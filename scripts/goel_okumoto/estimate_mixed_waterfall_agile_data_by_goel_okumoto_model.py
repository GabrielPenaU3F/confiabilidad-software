from src.domain.fitters.model_fitter import ModelFitter

fitter = ModelFitter()
fit = fitter.fit('goel-okumoto', 'mixed-waterfall-agile')
fit.show_results(plot_mttf=True, plot_mtbf=True)
