from src.domain.fitters.multistage_fitter import MultistageFitter

multistage_fitter = MultistageFitter()
multistage_fitter.add_stage(0, 87, 'delayed-s-shaped')
multistage_fitter.add_stage(87, 250, 'goel-okumoto')
fit = multistage_fitter.fit('ntds')
fit.show_results(plot_mttf=True, plot_mtbf=True)