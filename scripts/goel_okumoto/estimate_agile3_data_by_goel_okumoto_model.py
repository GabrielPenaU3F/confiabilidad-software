from src.domain.fitters.model_fitter import ModelFitter

ttf_fitter = ModelFitter()
fit = ttf_fitter.fit('goel-okumoto', 'agile-n3', initial_approx=(20, 0.5))
fit.show_results(plot_mttf=True, plot_mtbf=True)
