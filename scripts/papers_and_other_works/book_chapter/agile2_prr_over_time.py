from src.domain.fitters.fitter import GroupedFPDFitter

fpd_fitter = GroupedFPDFitter()

ds_fit_151 = fpd_fitter.fit('delayed-s-shaped', 'agile-n2', end_sample=4, initial_approx=(100, 0.001))
log_fit_151 = fpd_fitter.fit('logistic', 'agile-n2', end_sample=4, initial_approx=(8000, 0.003, 1))
bc_fit_151 = fpd_fitter.fit('barraza-contagion', 'agile-n2', end_sample=4)


ds_fit_248 = fpd_fitter.fit('delayed-s-shaped', 'agile-n2', end_sample=5, initial_approx=(500, 0.002))
#log_fit_248 = fpd_fitter.fit('logistic', 'agile-n2', end_sample=5, initial_approx=(8000, 0.003, 1))
bc_fit_248 = fpd_fitter.fit('barraza-contagion', 'agile-n2', end_sample=5)


ds_fit_480 = fpd_fitter.fit('delayed-s-shaped', 'agile-n2', end_sample=6, initial_approx=(100, 0.001))
log_fit_480 = fpd_fitter.fit('logistic', 'agile-n2', end_sample=6, initial_approx=(8000, 0.003, 1))
bc_fit_480 = fpd_fitter.fit('barraza-contagion', 'agile-n2', end_sample=6)


ds_fit_690 = fpd_fitter.fit('delayed-s-shaped', 'agile-n2', end_sample=10, initial_approx=(500, 0.002))
#log_fit_690 = fpd_fitter.fit('logistic', 'agile-n2', end_sample=10, initial_approx=(8000, 0.003, 0.001))
bc_fit_690 = fpd_fitter.fit('barraza-contagion', 'agile-n2', end_sample=10)

a=2
