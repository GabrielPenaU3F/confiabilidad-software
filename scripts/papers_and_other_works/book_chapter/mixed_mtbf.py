import numpy as np
from matplotlib import pyplot as plt

from src.data.data_repository import DataRepository
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator
from src.domain.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator
from src.domain.models.logistic.logistic_estimator import LogisticEstimator

go = GoelOkumotoEstimator()
ds = DelayedSShapedEstimator()
log = LogisticEstimator()

mixed = DataRepository.provide_project_data('mixed-waterfall-agile')
mixed_data = mixed.get_data()
mixed_cumfailures = mixed.get_cumulative_failures()
n = mixed_cumfailures[-1]

a_go = 1416.9139
b_go = 0.0048

a_ds = 893.6389
b_ds = 0.0218

a_log = 835.4106
b_log = 0.0307
c_log = 75.8011

mttf_go = go.calculate_mttfs(n, a_go, b_go)
mttf_ds = ds.calculate_mttfs(n, a_ds, b_ds)
mttf_log = log.calculate_mttfs(n, a_log, b_log, c_log)

mtbf_go = go.calculate_mtbfs(mttf_go)
mtbf_ds = ds.calculate_mtbfs(mttf_ds)
mtbf_log = log.calculate_mtbfs(mttf_log)

failures = np.linspace(1, len(mtbf_go), len(mtbf_go))

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
axes.plot(failures, mtbf_go,
          linewidth=1, color='#949494', linestyle='-', label='Goel-Okumoto')
axes.plot(failures, mtbf_ds,
          linewidth=1, color='#696969', linestyle='-', label='Delayed S-Shaped')
axes.plot(failures, mtbf_log,
          linewidth=2, color='#BDBDBD', linestyle='-', label='Logistic')

axes.legend()
plt.show()



