from src.fitters.fitter import GroupedFPDFitter

fpd_fitter = GroupedFPDFitter()
fit = fpd_fitter.fit('logistic', 'agile-n2', initial_approx=(300, 0.001, 2000))
fit.show_results(plot_mttf=True, plot_mtbf=True)
