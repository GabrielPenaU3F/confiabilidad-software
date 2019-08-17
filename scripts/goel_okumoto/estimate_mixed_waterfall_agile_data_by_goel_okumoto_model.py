from src.fitters.fitter import GroupedCumulativeFitter

fitter = GroupedCumulativeFitter()
fit = fitter.fit('goel-okumoto', 'mixed-waterfall-agile')
fit.show_results()

"""
params_go_mv_fallas_por_dia = go.\
    estimate_grouped_fpd_parameters_by_maximum_likelihood(dias, fallas_por_dia, params_go_mc,
                                                          solving_method='krylov')
"""
