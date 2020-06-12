import numpy as np
from matplotlib import pyplot as plt

from src.data.data_repository import DataRepository
from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator
from src.domain.models.logistic.logistic_estimator import LogisticEstimator

ds = DelayedSShapedEstimator()
log = LogisticEstimator()
bc = BarrazaContagionEstimator()

agile2 = DataRepository.provide_project_data('agile-n2')
agile2_data = agile2.get_data()
agile2_cumfailures = agile2.get_cumulative_failures()
n = agile2_cumfailures[-1]

a_ds = 370.3103
b_ds = 0.0025

a_log = 309.2426
b_log = 0.0047
c_log = 580.9822

a_bc = 0.2221
b_bc = 1.0479

mttf_ds = ds.calculate_mttfs(n, a_ds, b_ds)
mttf_log = log.calculate_mttfs(n, a_log, b_log, c_log)
mttf_bc = bc.calculate_mttfs(agile2.get_times(), a_bc, b_bc)

'''
mtbf_ds = ds.calculate_mtbfs(mttf_ds)[0:19]
mtbf_ds.extend([4.28, 3.715, 3.4060, 3.2180, 2.9440, 2.9790, 3.1310, 3.6680, 4.8290, 6.2600, 7.9800])
mtbf_log = log.calculate_mtbfs(mttf_log)[0:99]
mtbf_log.extend([2.916, 2.7720, 3.0520, 4.7880, 7.8900, 7.8400])
mtbf_bc = bc.calculate_mtbfs(mttf_bc)

failures_ds = list(np.linspace(1, 19, 19))
failures_ds.extend([20, 30, 40, 50, 100, 120, 150, 200, 250, 280, 300])
failures_log = list(np.linspace(1, 99, 99))
failures_log.extend([120, 150, 200, 250, 280, 300])
failures_bc = np.linspace(1, len(mtbf_bc), len(mtbf_bc))
'''

mtbf_ds = ds.calculate_mtbfs(mttf_ds)
mtbf_log = log.calculate_mtbfs(mttf_log)
mtbf_bc = bc.calculate_mtbfs(mttf_bc)

failures_ds = np.linspace(1, len(mtbf_ds), len(mtbf_ds))
failures_log = np.linspace(1, len(mtbf_log), len(mtbf_log))
failures_bc = agile2.get_cumulative_failures()

fig, axes = plt.subplots()
axes.set_xlabel('Failure number')
axes.set_ylabel('Mean time between failures')
axes.set_xlim(left=0, auto=True)
axes.set_ylim(auto=True)
axes.patch.set_facecolor("#ffffff")
axes.patch.set_edgecolor('black')
axes.patch.set_linewidth('1')
axes.set_facecolor("#ffffff")
axes.grid(color='black', linestyle='--', linewidth=0.5)
axes.plot(failures_ds, mtbf_ds,
          linewidth=1, color='#696969', linestyle='-', label='Delayed S-Shaped')
axes.plot(failures_log, mtbf_log,
          linewidth=2, color='#BDBDBD', linestyle='-', label='Logistic')
axes.plot(failures_bc, mtbf_bc,
          linewidth=2, color='#595959', linestyle='-', label='Our model')
axes.legend()
plt.show()



