from src.domain.fitters.fitter import TTFFitter

ttf_fitter = TTFFitter()

bc_fit_217 = ttf_fitter.fit('barraza-contagion', 'agile-n1', end_sample=9)

bc_fit_314 = ttf_fitter.fit('barraza-contagion', 'agile-n1', end_sample=17)

a=2
