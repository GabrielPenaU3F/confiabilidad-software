from src.domain.fitters.fitter import TTFFitter

ttf_fitter = TTFFitter()
fit = ttf_fitter.fit('delayed-s-shaped', 'agile-n1', end_sample=20)

fit.show_results()
