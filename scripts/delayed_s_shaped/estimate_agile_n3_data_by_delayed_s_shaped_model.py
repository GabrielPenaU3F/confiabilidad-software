from src.domain.fitters.model_fitter import ModelFitter

ttf_fitter = ModelFitter()
fit = ttf_fitter.fit('delayed-s-shaped', 'agile-n3', initial_approx=(100, 0.001))
fit.show_results(plot_mttf=True, plot_mtbf=True)
