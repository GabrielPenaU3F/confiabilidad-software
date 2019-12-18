from src.data.data_repository import DataRepository
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator
from src.domain.models.logistic.logistic_estimator import LogisticEstimator
from src.domain.fitters.fitter import GroupedFPDFitter

fpd_fitter = GroupedFPDFitter()

data = DataRepository.provide_project_data('agile-n2')
x_axis_data = data.get_times()
cumulative_failures = data.get_cumulative_failures()

ds = DelayedSShapedEstimator()
log = LogisticEstimator()

'''

ds_fit = fpd_fitter.fit('delayed-s-shaped', 'agile-n2', initial_approx=(100, 0.001))
log_fit = fpd_fitter.fit('logistic', 'agile-n2', initial_approx=(8000, 0.003, 1))

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
          label='Datos reales (Proyecto Ágil #2)')
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
          label='Datos reales (Proyecto Ágil #2)')
axes.plot(x_axis_data, ds.calculate_mean_failure_numbers(x_axis_data, ds_ml_a, ds_ml_b),
          linewidth=1, color='#ca3e47', linestyle='-', label='Delayed S-Shaped')
axes.plot(x_axis_data, log.calculate_mean_failure_numbers(x_axis_data, log_ml_a, log_ml_b, log_ml_c),
          linewidth=1, color='#58b368', linestyle='-', label='Logístico')
axes.legend()

plt.show()

'''

#ds_fit_151 = fpd_fitter.fit('delayed-s-shaped', 'agile-n2', end_sample=4, initial_approx=(100, 0.001))
#log_fit_151 = fpd_fitter.fit('logistic', 'agile-n2', end_sample=4, initial_approx=(8000, 0.003, 1))

ds_fit_248 = fpd_fitter.fit('delayed-s-shaped', 'agile-n2', end_sample=5, initial_approx=(500, 0.002))
#log_fit_248 = fpd_fitter.fit('logistic', 'agile-n2', end_sample=5, initial_approx=(8000, 0.003, 1))

#ds_fit_480 = fpd_fitter.fit('delayed-s-shaped', 'agile-n2', end_sample=6, initial_approx=(100, 0.001))
#log_fit_480 = fpd_fitter.fit('logistic', 'agile-n2', end_sample=6, initial_approx=(8000, 0.003, 1))

#ds_fit_690 = fpd_fitter.fit('delayed-s-shaped', 'agile-n2', end_sample=10, initial_approx=(500, 0.002))
#log_fit_690 = fpd_fitter.fit('logistic', 'agile-n2', end_sample=10, initial_approx=(8000, 0.003, 0.001))

a=2
