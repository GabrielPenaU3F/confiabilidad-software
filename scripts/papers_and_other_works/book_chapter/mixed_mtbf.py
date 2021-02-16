import numpy as np
from matplotlib import pyplot as plt

from src.data.data_repository import DataRepository
from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator
from src.domain.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator
from src.domain.models.logistic.logistic_estimator import LogisticEstimator

go = GoelOkumotoEstimator()
ds = DelayedSShapedEstimator()
log = LogisticEstimator()
bc = BarrazaContagionEstimator()

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

a_bc = 21.0424
b_bc = 0.7869

mttf_go = go.calculate_mttfs(n, a_go, b_go)[0:97]
mttf_ds = ds.calculate_mttfs(n, a_ds, b_ds)[0:99]
mttf_log = log.calculate_mttfs(n, a_log, b_log, c_log)[0:99]
mttf_bc = bc.calculate_mttfs(mixed.get_times(), a_bc, b_bc)


mtbf_go = go.calculate_regular_mtbfs(mttf_go)
mtbf_go.extend([0.1645, 0.1712, 0.1785, 0.1865, 0.1953, 0.205, 0.2155, 0.2273, 0.2405, 0.2553, 0.2672,
                0.2910, 0.3130, 0.3390])
mtbf_ds = ds.calculate_regular_mtbfs(mttf_ds)
mtbf_ds.extend([0.1459, 0.1407, 0.1399, 0.1422, 0.1470, 0.1545, 0.1651, 0.1793, 0.1985,
                0.2250, 0.2640, 0.3240, 0.4330, 0.6860])
mtbf_log = log.calculate_regular_mtbfs(mttf_log)
mtbf_log.extend([0.2661, 0.215, 0.1864, 0.1699, 0.1570, 0.1566, 0.1572, 0.1628, 0.1743, 0.1943, 0.2242,
                 0.2980, 0.4760, 0.7410])
mtbf_bc = bc.calculate_regular_mtbfs(mttf_bc)[0:160]

failures_go = list(np.linspace(1, 98, 98))
failures_ds = list(np.linspace(1, 100, 100))
failures_log = list(np.linspace(1, 100, 100))
failures_wolf = list(np.arange(150, 800, 50))
failures_go.extend(failures_wolf)
failures_ds.extend(failures_wolf)
failures_log.extend(failures_wolf)
failures_bc = mixed.get_cumulative_failures()[0:160]


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
axes.plot(failures_go, mtbf_go,
          linewidth=1, color='#949494', linestyle='-', label='Goel-Okumoto')
axes.plot(failures_ds, mtbf_ds,
          linewidth=1, color='#696969', linestyle='-', label='Delayed S-Shaped')
axes.plot(failures_log, mtbf_log,
          linewidth=2, color='#BDBDBD', linestyle='-', label='Logistic')
axes.plot(failures_bc, mtbf_bc,
          linewidth=2, color='#595959', linestyle='-', label='Our model')

axes.legend()
plt.show()



