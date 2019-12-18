from src.domain.fitters.fitter import Fitter

fpd_fitter = Fitter()

#fit_go_50 = fpd_fitter.fit('goel-okumoto', 'mixed-waterfall-agile', end_sample=49, lsq_only=True)
#fit_bc_50 = fpd_fitter.fit('barraza-contagion', 'mixed-waterfall-agile', end_sample=49, lsq_only=True)

#fit_go_60 = fpd_fitter.fit('goel-okumoto', 'mixed-waterfall-agile', end_sample=59, lsq_only=True)
#fit_bc_60 = fpd_fitter.fit('barraza-contagion', 'mixed-waterfall-agile', end_sample=59, lsq_only=True)

#fit_go_70 = fpd_fitter.fit('goel-okumoto', 'mixed-waterfall-agile', end_sample=69, lsq_only=True)
#fit_bc_70 = fpd_fitter.fit('barraza-contagion', 'mixed-waterfall-agile', end_sample=69, lsq_only=True)

#fit_go_90 = fpd_fitter.fit('goel-okumoto', 'mixed-waterfall-agile', end_sample=89, lsq_only=True)
fit_bc_90 = fpd_fitter.fit('barraza-contagion', 'mixed-waterfall-agile', end_sample=89, lsq_only=True)
fit_log_90 = fpd_fitter.fit('logistic', 'mixed-waterfall-agile', end_sample=89, lsq_only=True)


a=2
