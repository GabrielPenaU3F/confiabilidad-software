from src.data.data_repository import DataRepository
from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator
from src.domain.models.logistic.logistic_estimator import LogisticEstimator

from matplotlib import pyplot as plt

ds = DelayedSShapedEstimator()
log = LogisticEstimator()
bc = BarrazaContagionEstimator()

agile2 = DataRepository.provide_project_data('agile-n2')
agile2_times = agile2.get_formated_times()

a_ds = 370.3103
b_ds = 0.0025

a_log = 309.2426
b_log = 0.0047
c_log = 580.9822

a_bc = 0.2221
b_bc = 1.0479

mean_values_ds = ds.calculate_mean_failure_numbers(agile2_times, a_ds, b_ds)
mean_values_log = log.calculate_mean_failure_numbers(agile2_times, a_log, b_log, c_log)
mean_values_bc = bc.calculate_mean_failure_numbers(agile2_times, a_bc, b_bc)

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
axes.plot(agile2_times, agile2.get_cumulative_failures(), linewidth=1, color='black', linestyle='--',
          label='Real data (' + 'Agile #2' + ')')
axes.plot(agile2_times, mean_values_ds, linewidth=1, color='#696969', linestyle='-', label='Delayed S-Shaped')
axes.plot(agile2_times, mean_values_log, linewidth=2, color='#BDBDBD', linestyle='-', label='Logistic')
axes.plot(agile2_times, mean_values_bc, linewidth=2, color='#595959', linestyle='-', label='Our model')

axes.legend()
plt.show()
