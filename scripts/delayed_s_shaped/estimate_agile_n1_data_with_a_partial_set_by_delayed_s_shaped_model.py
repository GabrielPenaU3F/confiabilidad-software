from src.domain.fitters.model_fitter import ModelFitter

ttf_fitter = ModelFitter()
fit = ttf_fitter.fit('delayed-s-shaped', 'agile-n1', end_sample=20)

fit.show_results()
