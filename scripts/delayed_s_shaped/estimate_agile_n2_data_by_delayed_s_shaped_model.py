from src.domain.fitters.model_fitter import ModelFitter

fpd_fitter = ModelFitter()
fit = fpd_fitter.fit('delayed-s-shaped', 'agile-n2', initial_approx=(10, 0.01))
fit.show_results(plot_mttf=True, plot_mtbf=True)
