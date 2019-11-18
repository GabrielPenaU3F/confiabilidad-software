from src.fitters.fitter import GroupedFPDFitter

fpd_fitter = GroupedFPDFitter()
fit = fpd_fitter.fit('goel-okumoto', 'agile-n2')
fit.show_results(plot_mttf=True, plot_mtbf=True)
