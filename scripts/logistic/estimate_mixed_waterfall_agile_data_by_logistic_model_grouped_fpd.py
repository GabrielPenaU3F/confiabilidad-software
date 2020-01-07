from src.domain.fitters.model_fitter import ModelFitter

fitter = ModelFitter()
fit = fitter.fit('logistic', 'mixed-waterfall-agile', initial_approx=(1000, 0.001, 100))
fit.show_results(plot_mttf=True, plot_mtbf=True)