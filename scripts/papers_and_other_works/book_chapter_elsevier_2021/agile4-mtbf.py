# Agile Project #2 in the book

import numpy as np

from src.data.data_repository import DataRepository
from src.domain.fitters.model_fitter import ModelFitter
from matplotlib import pyplot as plt
from matplotlib import rc
import matplotlib.font_manager

rc('font', **{'family': 'serif', 'serif': ['CMU Sans Serif']})
plt.rcParams['font.family'] = 'Calibri'

ttf_fitter = ModelFitter()
ds_fit = ttf_fitter.fit('delayed-s-shaped', 'agile-n4', initial_approx=(100, 0.001),
                        lsq_only=True, mt_formula='regular')
log_fit = ttf_fitter.fit('logistic', 'agile-n4', initial_approx=(30, 0.03, 300),
                         lsq_only=True, mt_formula='regular')
bc_fit = ttf_fitter.fit('barraza-contagion', 'agile-n4',
                        lsq_only=True, mt_formula='conditional')

data = DataRepository.provide_project_data('agile-n4')
real_tbf = data.get_time_between_failures()
x_axis_data = np.linspace(1, len(real_tbf), len(real_tbf))

ds_mtbf = ds_fit.get_all_mtbf()
log_mtbf = log_fit.get_all_mtbf()
bc_mtbf = bc_fit.get_all_mtbf()

fig, axes = plt.subplots(figsize=(6, 4))
axes.set_xlabel('Failure number', fontsize=12)
axes.xaxis.set_tick_params(labelsize=10)
axes.xaxis.labelpad = 4
axes.set_ylabel('Mean time between failures', fontsize=12)
axes.yaxis.set_tick_params(labelsize=10)
axes.yaxis.labelpad = 8
axes.set_xlim(left=0, auto=True)
axes.set_ylim(auto=True)
axes.patch.set_facecolor("#ffffff")
axes.patch.set_edgecolor('black')
axes.patch.set_linewidth('1')
axes.set_facecolor("#ffffff")
axes.grid(color='black', linestyle='--', linewidth=0.5)
axes.scatter(x_axis_data, real_tbf, linewidth=1, color='#263859', s=4.0,
          label='Real data (Project #2)')
axes.plot(x_axis_data, ds_mtbf,
          linewidth=1, color='#ca3e47', linestyle='-', label='Delayed S-shaped')
axes.plot(x_axis_data, log_mtbf,
          linewidth=1, color='#58b368', linestyle='-', label='Logistic')
axes.plot(x_axis_data, bc_mtbf,
          linewidth=1, color='#4a47a3', linestyle='-', label='Linear contagion')
axes.legend(fontsize=12)

plt.savefig('fig2.tiff', dpi=300)
