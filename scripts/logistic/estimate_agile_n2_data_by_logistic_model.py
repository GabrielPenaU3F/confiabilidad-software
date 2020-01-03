from src.domain.fitters.model_fitter import ModelFitter

fpd_fitter = ModelFitter()
fit = fpd_fitter.fit('logistic', 'agile-n2')
fit.show_results(plot_mttf=True, plot_mtbf=True)
