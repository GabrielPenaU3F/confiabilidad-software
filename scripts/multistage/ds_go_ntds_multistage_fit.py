from src.domain.fitters.multistage_fitter import MultistageFitter

multistage_fitter = MultistageFitter()
multistage_fitter.add_stage(0, 98, 'delayed-s-shaped')
multistage_fitter.add_stage(98, 250, 'goel-okumoto', initial_approx=(90, 0.001))
fit = multistage_fitter.fit('ntds')
fit.show_results(plot_mttf=True, plot_mtbf=True)
