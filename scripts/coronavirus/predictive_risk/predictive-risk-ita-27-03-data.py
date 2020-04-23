import numpy as np
from colorama import Fore

from src.data.data_repository import DataRepository
from src.domain.fitters.model_fitter import ModelFitter
from matplotlib import pyplot as plt

from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator

DataRepository.load_project_data_from_file(path="../../../test_resource_files/covid_data_by_date/ita-27-03.ods")

fitter = ModelFitter()
bc_fit_30 = fitter.fit('barraza-contagion', 'corona1-ita-27-03', mts=False, end_sample=30)
bc_fit_35 = fitter.fit('barraza-contagion', 'corona1-ita-27-03', mts=False, end_sample=35)
bc_fit_40 = fitter.fit('barraza-contagion', 'corona1-ita-27-03', mts=False, end_sample=40)
bc_fit_45 = fitter.fit('barraza-contagion', 'corona1-ita-27-03', mts=False, end_sample=45)
bc_fit_50 = fitter.fit('barraza-contagion', 'corona1-ita-27-03', mts=False, end_sample=50)
bc_fit_55 = fitter.fit('barraza-contagion', 'corona1-ita-27-03', mts=False, end_sample=55)
bc_fit = fitter.fit('barraza-contagion', 'corona1-ita-27-03', mts=False)

fig, axes = plt.subplots()

data = DataRepository.provide_project_data('corona1-ita-27-03')
tiempos = data.get_times()
bc = BarrazaContagionEstimator()

print(Fore.YELLOW + 'PRR - 30 datos:')
print(Fore.LIGHTRED_EX + (bc_fit_30.get_prr_lsq().__str__()))

print(Fore.YELLOW + 'PRR - 35 datos:')
print(Fore.LIGHTRED_EX + (bc_fit_35.get_prr_lsq().__str__()))

print(Fore.YELLOW + 'PRR - 40 datos:')
print(Fore.LIGHTRED_EX + (bc_fit_40.get_prr_lsq().__str__()))

print(Fore.YELLOW + 'PRR - 45 datos:')
print(Fore.LIGHTRED_EX + (bc_fit_45.get_prr_lsq().__str__()))

print(Fore.YELLOW + 'PRR - 50 datos:')
print(Fore.LIGHTRED_EX + (bc_fit_50.get_prr_lsq().__str__()))

print(Fore.YELLOW + 'PRR - 55 datos:')
print(Fore.LIGHTRED_EX + (bc_fit_55.get_prr_lsq().__str__()))

print(Fore.YELLOW + 'PRR - Full dataset:')
print(Fore.LIGHTRED_EX + (bc_fit.get_prr_lsq().__str__()))

axes.plot(data.get_times(), data.get_cumulative_failures(), linewidth=2, color='blue',
          label='Datos reales en Italia - 31/1/20 al 27/3/20')
axes.plot(tiempos, bc.calculate_mean(tiempos, *bc_fit.get_lsq_parameters()), linewidth=1, color='red',
          label='Ajuste con el dataset completo')

axes.set_xlim(left=0, auto=True)
axes.set_ylim(bottom=0, auto=True)
axes.patch.set_facecolor("#ffffff")
axes.patch.set_edgecolor('black')
axes.patch.set_linewidth('1')
axes.set_facecolor("#ffffff")
axes.grid(color='black', linestyle='--', linewidth=0.5)
axes.set_xlabel('Failure')
axes.legend()

plt.show()