from src.domain.fitters.fitter import GroupedCumulativeFitter

fitter = GroupedCumulativeFitter()
fit = fitter.fit('goel-okumoto', 'mixed-waterfall-agile', cumulative=True)
fit.show_results()
