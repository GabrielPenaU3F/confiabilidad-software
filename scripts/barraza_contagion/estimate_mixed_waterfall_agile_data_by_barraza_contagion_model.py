from src.domain.fitters.model_fitter import ModelFitter

fpd_fitter = ModelFitter()
fit = fpd_fitter.fit('barraza-contagion', 'mixed-waterfall-agile')
fit.show_results()
