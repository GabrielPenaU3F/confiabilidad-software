from src.data.data_repository import DataRepository
from src.domain.fitters.model_fitter import ModelFitter
from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator
import numpy as np


import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

bc = BarrazaContagionEstimator()

ntds = DataRepository.provide_project_data('ntds')
ntds_times = ntds.get_times()
ntds_cf = ntds.get_cumulative_failures()

ttf_fitter = ModelFitter()
ntds_fit = ttf_fitter.fit('barraza-contagion', 'ntds')

a_bc, b_bc = ntds_fit.get_lsq_parameters()
mean_values_bc = bc.calculate_mean_failure_numbers(ntds_times, a_bc, b_bc)
coef_r2 = np.var(mean_values_bc)/np.var(ntds_cf)

print("rho: ", a_bc)
print("gamma: ", b_bc * a_bc)
print("gamma/rho: ", b_bc)
print("r2: ", coef_r2)

plt.style.use('bmh')

fig, axes = plt.subplots(figsize=(8, 5))
axes.set_xlabel('Time (days)')
axes.set_ylabel('Number of failures')
axes.set_xlim(left=0, auto=True)
axes.set_ylim(auto=True)
axes.patch.set_facecolor("#ffffff")
#axes.patch.set_edgecolor('black')
#axes.patch.set_linewidth('1')
#axes.set_facecolor("#ffffff")
#axes.grid(color='black', linestyle='--', linewidth=0.5)
axes.plot(ntds_times, ntds_cf, linewidth=1, color='black', linestyle='-',
          label='Real data (' + 'NTDS' + ')')
axes.plot(ntds_times, mean_values_bc, linewidth=1, color='#e71414', linestyle='-', label='Proposed model')

axes.legend(prop={'size': 13})
plt.show()
