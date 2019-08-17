from src.fitters.fitter import GroupedCumulativeFitter

fitter = GroupedCumulativeFitter()
fit = fitter.fit('logistic', 'mixed-waterfall-agile')
fit.show_results()

"""
params_log_mv_fallas_por_dia = log.\
    estimate_grouped_fpd_parameters_by_maximum_likelihood(dias, fallas_por_dia, params_log_mc,
                                                          solving_method='krylov')
"""
