from src.domain.fitters.fitter import GroupedFPDFitter

fpd_fitter = GroupedFPDFitter()
fit = fpd_fitter.fit('barraza-contagion', 'mixed-waterfall-agile')
fit.show_results()
