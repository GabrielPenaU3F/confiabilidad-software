from src.fitters.fitter import TTFFitter

ttf_fitter = TTFFitter()
fit = ttf_fitter.fit('gompertz', 'ntds', lsq_only=True)
fit.show_results()
