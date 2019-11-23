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

ntds = DataRepository.provide_project_data('ntds')
ntds_data = ntds.get_data()
ntds_cumfailures = ntds.get_cumulative_failures()
n = ntds_cumfailures[-1]

a_go = 33.5994
b_go = 0.0063

a_ds = 26.7155
b_ds = 0.0212

a_log = 24.6114
b_log = 0.0413
c_log = 76.4858

a_bc = 0.3799
b_bc = 0.6450

mttf_go = go.calculate_mttfs(n, a_go, b_go)
mttf_ds = ds.calculate_mttfs(n, a_ds, b_ds)
mttf_log = log.calculate_mttfs(n, a_log, b_log, c_log)
mttf_bc = bc.calculate_mttfs(ntds_data, a_bc, b_bc)

mtbf_go = go.calculate_mtbfs(mttf_go)
mtbf_ds = ds.calculate_mtbfs(mttf_ds)
mtbf_log = log.calculate_mtbfs(mttf_log)
mtbf_bc = bc.calculate_mtbfs(mttf_bc)

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
axes.plot(failures, mtbf_bc,
          linewidth=2, color='#595959', linestyle='-', label='Our model')

axes.legend()
plt.show()



