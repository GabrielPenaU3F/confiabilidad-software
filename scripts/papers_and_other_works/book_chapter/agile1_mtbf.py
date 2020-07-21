import numpy as np
from matplotlib import pyplot as plt

from src.data.data_repository import DataRepository
from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator
from src.domain.models.logistic.logistic_estimator import LogisticEstimator

ds = DelayedSShapedEstimator()
log = LogisticEstimator()
bc = BarrazaContagionEstimator()

agile1 = DataRepository.provide_project_data('agile-n1')
agile1_data = agile1.get_data()
agile1_cumfailures = agile1.get_cumulative_failures()
n = agile1_cumfailures[-1]
tbf = agile1.get_time_between_failures()


a_ds = 72.4203
b_ds = 0.0031

a_log = 32.3171
b_log = 0.0117
c_log = 280.7373

a_bc = 0.0239
b_bc = 1.5923

mttf_ds = ds.calculate_mttfs(n, a_ds, b_ds)
mttf_log = log.calculate_mttfs(n, a_log, b_log, c_log)
mttf_bc = bc.calculate_mttfs(agile1.get_times(), a_bc, b_bc)

mtbf_ds = ds.calculate_mtbfs(mttf_ds)
mtbf_log = log.calculate_mtbfs(mttf_log)
mtbf_bc = bc.calculate_mtbfs(mttf_bc)

failures = np.linspace(1, len(mtbf_ds), len(mtbf_ds))

ig, axes = plt.subplots()
axes.set_xlabel('Failure number')
axes.set_ylabel('Mean time between failures')
axes.set_xlim(left=0, auto=True)
axes.set_ylim(bottom=0, top=50)
axes.patch.set_facecolor("#ffffff")
axes.patch.set_edgecolor('black')
axes.patch.set_linewidth('1')
axes.set_facecolor("#ffffff")
axes.grid(color='black', linestyle='--', linewidth=0.5)
axes.plot(failures, tbf, linewidth=1, color='black', linestyle='--',
          label='Real data (' + 'Agile #1' + ')')
axes.plot(failures, mtbf_ds,
          linewidth=1, color='#696969', linestyle='-', label='Delayed S-Shaped')
axes.plot(failures, mtbf_log,
          linewidth=2, color='#BDBDBD', linestyle='-', label='Logistic')
axes.plot(failures, mtbf_bc,
          linewidth=2, color='#595959', linestyle='-', label='Our model')

axes.legend()
plt.show()



