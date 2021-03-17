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

ntds = DataRepository.provide_project_data('ntds')
ntds_times = ntds.get_times()

a_go = 33.5994
b_go = 0.0063

a_ds = 26.7155
b_ds = 0.0212

a_log = 24.6114
b_log = 0.0413
c_log = 76.4858

a_bc = 0.3799
b_bc = 0.6450

mean_values_go = go.calculate_mean_failure_numbers(ntds_times, a_go, b_go)
mean_values_ds = ds.calculate_mean_failure_numbers(ntds_times, a_ds, b_ds)
mean_values_log = log.calculate_mean_failure_numbers(ntds_times, a_log, b_log, c_log)
mean_values_bc = bc.calculate_mean_failure_numbers(ntds_times, a_bc, b_bc)

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
axes.plot(ntds_times, ntds.get_cumulative_failures(), linewidth=1, color='black', linestyle='--',
          label='Real data (' + 'NTDS' + ')')
axes.plot(ntds_times, mean_values_go, linewidth=1, color='#8cba51', linestyle='-', label='Goel-Okumoto')
axes.plot(ntds_times, mean_values_ds, linewidth=1, color='#303960', linestyle='-', label='Delayed S-Shaped')
axes.plot(ntds_times, mean_values_log, linewidth=1, color='#ffd868', linestyle='-', label='Logistic')
axes.plot(ntds_times, mean_values_bc, linewidth=1, color='#e71414', linestyle='-', label='Our model')

axes.legend()
plt.show()
