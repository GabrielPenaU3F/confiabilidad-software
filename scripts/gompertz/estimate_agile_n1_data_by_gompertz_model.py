from src.domain.fitters.fitter import TTFFitter

ttf_fitter = TTFFitter()
fit = ttf_fitter.fit('gompertz', 'agile-n1')
fit.show_results()
