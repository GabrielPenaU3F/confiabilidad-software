from src.domain.fitters.fitter import TTFFitter

ttf_fitter = TTFFitter()

#fit_go_10 = ttf_fitter.fit('goel-okumoto', 'ntds', end_sample=9, lsq_only=True)
#fit_ds_10 = ttf_fitter.fit('delayed-s-shaped', 'ntds', end_sample=9, lsq_only=True)
#fit_log_10 = ttf_fitter.fit('logistic', 'ntds', end_sample=9, lsq_only=True)
#fit_bc_10 = ttf_fitter.fit('barraza-contagion', 'ntds', end_sample=9, lsq_only=True)

#fit_go_20 = ttf_fitter.fit('goel-okumoto', 'ntds', end_sample=14, lsq_only=True)
#fit_ds_20 = ttf_fitter.fit('delayed-s-shaped', 'ntds', end_sample=14, lsq_only=True)
#fit_log_20 = ttf_fitter.fit('logistic', 'ntds', end_sample=14, lsq_only=True)
fit_bc_20 = ttf_fitter.fit('barraza-contagion', 'ntds', end_sample=14, lsq_only=True)

a=2
