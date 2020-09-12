import numpy as np

from src.data.data_repository import DataRepository
from src.domain.fitters.model_fitter import ModelFitter
from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator

import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

bc = BarrazaContagionEstimator()

agile1 = DataRepository.provide_project_data('agile-n1')
agile1_times = agile1.get_times()
agile1_cf = agile1.get_cumulative_failures()

ttf_fitter = ModelFitter()
agile1_fit = ttf_fitter.fit('barraza-contagion', 'agile-n1')

a_bc, b_bc = agile1_fit.get_lsq_parameters()
mean_values_bc = bc.calculate_mean_failure_numbers(agile1_times, a_bc, b_bc)
coef_r2 = np.var(mean_values_bc)/np.var(agile1_cf)

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
axes.plot(agile1_times, agile1_cf, linewidth=1, color='black', linestyle='-',
          label='Real data (' + 'Agile project' + ')')
axes.plot(agile1_times, mean_values_bc, linewidth=1, color='#e71414', linestyle='-', label='Proposed model')

axes.legend(prop={'size': 13})
plt.show()
