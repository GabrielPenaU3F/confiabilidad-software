from src.fitters.fitter import TTFFitter

ttf_fitter = TTFFitter()
fit = ttf_fitter.fit('logistic', 'agile-n1')
fit.show_results()
