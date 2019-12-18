from src.domain.fitters.fitter import TTFFitter

ttf_fitter = TTFFitter()
fit = ttf_fitter.fit('gompertz', 'ntds')
fit.show_results()
