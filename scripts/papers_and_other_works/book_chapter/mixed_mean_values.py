from src.data.data_repository import DataRepository
from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator
from src.domain.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator
from src.domain.models.logistic.logistic_estimator import LogisticEstimator

from matplotlib import pyplot as plt

go = GoelOkumotoEstimator()
ds = DelayedSShapedEstimator()
log = LogisticEstimator()
bc = BarrazaContagionEstimator()

mixed = DataRepository.provide_project_data('mixed-waterfall-agile')
mixed_times = mixed.get_times()

a_go = 1416.9139
b_go = 0.0048

a_ds = 893.6389
b_ds = 0.0218

a_log = 835.4106
b_log = 0.0307
c_log = 75.8011

a_bc = 21.0424
b_bc = 0.7869

mean_values_go = go.calculate_mean_failure_numbers(mixed_times, a_go, b_go)
mean_values_ds = ds.calculate_mean_failure_numbers(mixed_times, a_ds, b_ds)
mean_values_log = log.calculate_mean_failure_numbers(mixed_times, a_log, b_log, c_log)
mean_values_bc = bc.calculate_mean_failure_numbers(mixed_times, a_bc, b_bc)

fig, axes = plt.subplots()
axes.set_xlabel('Time (days)')
axes.set_ylabel('Number of failures')
axes.set_xlim(left=0, auto=True)
axes.set_ylim(auto=True)
axes.patch.set_facecolor("#ffffff")
axes.patch.set_edgecolor('black')
axes.patch.set_linewidth('1')
axes.set_facecolor("#ffffff")
axes.grid(color='black', linestyle='--', linewidth=0.5)
axes.plot(mixed_times, mixed.get_cumulative_failures(), linewidth=1, color='black', linestyle='--',
          label='Real data (' + 'Mixed Waterfall-Agile' + ')')
axes.plot(mixed_times, mean_values_go, linewidth=1, color='#949494', linestyle='-', label='Goel-Okumoto')
axes.plot(mixed_times, mean_values_ds, linewidth=1, color='#696969', linestyle='-', label='Delayed S-Shaped')
axes.plot(mixed_times, mean_values_log, linewidth=2, color='#BDBDBD', linestyle='-', label='Logistic')
axes.plot(mixed_times, mean_values_bc, linewidth=2, color='#595959', linestyle='-', label='Our model')

axes.legend()
plt.show()
