from src.domain.fitters.model_fitter import ModelFitter

ttf_fitter = ModelFitter()
fit = ttf_fitter.fit('logistic', 'agile-n1')
fit.show_results(plot_mttf=True, plot_mtbf=True)
