from src.domain.fitters.model_fitter import ModelFitter

ttf_fitter = ModelFitter()
fit = ttf_fitter.fit('gompertz', 'agile-n1')
fit.show_results()
