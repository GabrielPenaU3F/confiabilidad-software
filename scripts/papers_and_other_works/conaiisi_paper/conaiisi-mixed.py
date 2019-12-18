from src.data.data_repository import DataRepository
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator
from src.domain.models.logistic.logistic_estimator import LogisticEstimator
from src.domain.fitters.fitter import GroupedFPDFitter

fpd_fitter = GroupedFPDFitter()

data = DataRepository.provide_project_data('mixed-waterfall-agile')
x_axis_data = data.get_times()
cumulative_failures = data.get_cumulative_failures()

ds = DelayedSShapedEstimator()
log = LogisticEstimator()

'''

ds_fit = fpd_fitter.fit('delayed-s-shaped', 'mixed-waterfall-agile')
log_fit = fpd_fitter.fit('logistic', 'mixed-waterfall-agile')

ds_lsq_a = ds_fit.get_lsq_parameters()[0]
ds_lsq_b = ds_fit.get_lsq_parameters()[1]

log_lsq_a = log_fit.get_lsq_parameters()[0]
log_lsq_b = log_fit.get_lsq_parameters()[1]
log_lsq_c = log_fit.get_lsq_parameters()[2]

fig, axes = plt.subplots()
axes.set_xlabel('Tiempo (días)')
axes.set_ylabel('Numero esperado de fallas')
axes.set_xlim(left=0, auto=True)
axes.set_ylim(auto=True)
axes.patch.set_facecolor("#ffffff")
axes.patch.set_edgecolor('black')
axes.patch.set_linewidth('1')
axes.set_facecolor("#ffffff")
axes.grid(color='black', linestyle='--', linewidth=0.5)

axes.plot(x_axis_data, cumulative_failures, linewidth=1, color='#263859', linestyle='--',
          label='Datos reales (Proyecto Mixto Cascada/Ágil)')
axes.plot(x_axis_data, ds.calculate_mean_failure_numbers(x_axis_data, ds_lsq_a, ds_lsq_b),
          linewidth=1, color='#ca3e47', linestyle='-', label='Delayed S-Shaped')
axes.plot(x_axis_data, log.calculate_mean_failure_numbers(x_axis_data, log_lsq_a, log_lsq_b, log_lsq_c),
          linewidth=1, color='#58b368', linestyle='-', label='Logístico')
axes.legend()

plt.show()

ds_ml_a = ds_fit.get_ml_parameters()[0]
ds_ml_b = ds_fit.get_ml_parameters()[1]

log_ml_a = log_fit.get_ml_parameters()[0]
log_ml_b = log_fit.get_ml_parameters()[1]
log_ml_c = log_fit.get_ml_parameters()[2]

fig, axes = plt.subplots()
axes.set_xlabel('Tiempo (días)')
axes.set_ylabel('Numero esperado de fallas')
axes.set_xlim(left=0, auto=True)
axes.set_ylim(auto=True)
axes.patch.set_facecolor("#ffffff")
axes.patch.set_edgecolor('black')
axes.patch.set_linewidth('1')
axes.set_facecolor("#ffffff")
axes.grid(color='black', linestyle='--', linewidth=0.5)
axes.plot(x_axis_data, cumulative_failures, linewidth=1, color='#263859', linestyle='--',
          label='Datos reales (Proyecto Mixto Cascada/Ágil)')
axes.plot(x_axis_data, ds.calculate_mean_failure_numbers(x_axis_data, ds_ml_a, ds_ml_b),
          linewidth=1, color='#ca3e47', linestyle='-', label='Delayed S-Shaped')
axes.plot(x_axis_data, log.calculate_mean_failure_numbers(x_axis_data, log_ml_a, log_ml_b, log_ml_c),
          linewidth=1, color='#58b368', linestyle='-', label='Logístico')
axes.legend()

plt.show()

'''

#ds_fit_50 = fpd_fitter.fit('delayed-s-shaped', 'mixed-waterfall-agile', end_sample=50, initial_approx=(20, 0.002))
#log_fit_50 = fpd_fitter.fit('logistic', 'mixed-waterfall-agile', end_sample=50, initial_approx=(1000, 0.00001, 10))

#ds_fit_60 = fpd_fitter.fit('delayed-s-shaped', 'mixed-waterfall-agile', end_sample=60, initial_approx=(20, 0.002))
#log_fit_60 = fpd_fitter.fit('logistic', 'mixed-waterfall-agile', end_sample=60, initial_approx=(1000, 0.00001, 100))

#ds_fit_70 = fpd_fitter.fit('delayed-s-shaped', 'mixed-waterfall-agile', end_sample=70, initial_approx=(10, 0.01))
#log_fit_70 = fpd_fitter.fit('logistic', 'mixed-waterfall-agile', end_sample=70, initial_approx=(1000, 0.00001, 100))

ds_fit_90 = fpd_fitter.fit('delayed-s-shaped', 'mixed-waterfall-agile', end_sample=90, initial_approx=(10, 0.01))
log_fit_70 = fpd_fitter.fit('logistic', 'mixed-waterfall-agile', end_sample=90, initial_approx=(1000, 0.00001, 100))

a=2
