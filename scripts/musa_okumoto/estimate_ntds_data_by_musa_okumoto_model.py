from src.domain.fitters.model_fitter import ModelFitter

ttf_fitter = ModelFitter()
fit = ttf_fitter.fit('musa-okumoto', 'ntds')
fit.show_results(plot_mttf=True, plot_mtbf=True)
