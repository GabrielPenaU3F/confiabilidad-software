from src.domain.fitters.multistage_fitter import MultistageFitter

log_mo_fitter = MultistageFitter()
log_mo_fitter.add_stage(0, 110, 'logistic', initial_approx=(800, 0.001, 100))
log_mo_fitter.add_stage(110, 209, 'musa-okumoto', initial_approx=(90, 0.001))
log_mo_fit = log_mo_fitter.fit('mixed-waterfall-agile')
log_mo_fit.show_results()
