from src.fitters.fitter import TTFFitter

ttf_fitter = TTFFitter()
fit = ttf_fitter.fit('poisson', 'ntds', mts=False)
fit.show_results()
