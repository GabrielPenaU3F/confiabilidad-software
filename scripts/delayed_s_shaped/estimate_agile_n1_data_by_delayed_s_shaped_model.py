from src.fitters.fitter import TTFFitter

ttf_fitter = TTFFitter()
fit = ttf_fitter.fit('delayed-s-shaped', 'agile-n1')
fit.show_results()
