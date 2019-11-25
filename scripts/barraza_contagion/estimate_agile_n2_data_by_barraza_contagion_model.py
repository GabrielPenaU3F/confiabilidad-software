from src.fitters.fitter import GroupedFPDFitter

fpd_fitter = GroupedFPDFitter()
fit = fpd_fitter.fit('barraza-contagion', 'agile-n2')
fit.show_results()
