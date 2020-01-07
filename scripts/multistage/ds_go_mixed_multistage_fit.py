from src.domain.fitters.multistage_fitter import MultistageFitter

multistage_fitter = MultistageFitter()
multistage_fitter.add_stage(0, 100, 'delayed-s-shaped')
multistage_fitter.add_stage(100, 209, 'goel-okumoto')
fit = multistage_fitter.fit('mixed-waterfall-agile')
fit.show_results(plot_mttf=True, plot_mtbf=True)
