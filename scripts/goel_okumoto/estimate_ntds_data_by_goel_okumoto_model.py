from src.fitters.fitter import TTFFitter

ttf_fitter = TTFFitter()
fit = ttf_fitter.fit('goel-okumoto', 'ntds')
fit.show_results()
