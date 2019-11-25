import numpy as np
from matplotlib import pyplot as plt

from src.data.data_repository import DataRepository
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator
from src.domain.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator
from src.domain.models.logistic.logistic_estimator import LogisticEstimator

go = GoelOkumotoEstimator()
ds = DelayedSShapedEstimator()
log = LogisticEstimator()

agile2 = DataRepository.provide_project_data('agile-n2')
agile2_data = agile2.get_data()
agile2_cumfailures = agile2.get_cumulative_failures()
n = agile2_cumfailures[-1]

a_ds = 370.3103
b_ds = 0.0025

a_log = 309.2426
b_log = 0.0047
c_log = 580.9822

mttf_ds = ds.calculate_mttfs(n, a_ds, b_ds)
mttf_log = log.calculate_mttfs(n, a_log, b_log, c_log)

mtbf_ds = ds.calculate_mtbfs(mttf_ds)
mtbf_log = log.calculate_mtbfs(mttf_log)

failures = np.linspace(1, len(mtbf_ds), len(mtbf_ds))

ig, axes = plt.subplots()
axes.set_xlabel('Failure number')
axes.set_ylabel('Mean time between failures')
axes.set_xlim(left=0, auto=True)
axes.set_ylim(auto=True)
axes.patch.set_facecolor("#ffffff")
axes.patch.set_edgecolor('black')
axes.patch.set_linewidth('1')
axes.set_facecolor("#ffffff")
axes.grid(color='black', linestyle='--', linewidth=0.5)
axes.plot(failures, mtbf_ds,
          linewidth=1, color='#696969', linestyle='-', label='Delayed S-Shaped')
axes.plot(failures, mtbf_log,
          linewidth=2, color='#BDBDBD', linestyle='-', label='Logistic')

axes.legend()
plt.show()



