from src.data.data_repository import DataRepository
from src.domain.fitters.model_fitter import ModelFitter
from matplotlib import pyplot as plt

DataRepository.load_project_data_from_file(path="../../../test_resource_files/covid_data_by_date/esp-22-04.ods")

fitter = ModelFitter()

data = DataRepository.provide_project_data('corona1-esp-22-04')

fits = {}
fits[35] = fitter.fit('barraza-contagion', 'corona1-esp-22-04', mts=False, end_sample=35)
fits[45] = fitter.fit('barraza-contagion', 'corona1-esp-22-04', mts=False, end_sample=45)
fits[50] = fitter.fit('barraza-contagion', 'corona1-esp-22-04', mts=False, end_sample=50)
fits[55] = fitter.fit('barraza-contagion', 'corona1-esp-22-04', mts=False, end_sample=55)
fits[60] = fitter.fit('barraza-contagion', 'corona1-esp-22-04', mts=False, end_sample=60)
fits[65] = fitter.fit('barraza-contagion', 'corona1-esp-22-04', mts=False, end_sample=65)
fits[70] = fitter.fit('barraza-contagion', 'corona1-esp-22-04', mts=False, end_sample=70)
fits[75] = fitter.fit('barraza-contagion', 'corona1-esp-22-04', mts=False, end_sample=75)
fits[len(data.get_data())] = bc_fit = fitter.fit('barraza-contagion', 'corona1-esp-22-04', mts=False)

a_params = []
b_params = []
keys = sorted(fits.keys())
for k in keys:
    params = fits[k].get_lsq_parameters()
    a_params.append(params[0])
    b_params.append(params[1])

fig, axes = plt.subplots(1, 2)

times = keys

axes[0].plot(times, a_params, linewidth=2, color='blue',
                  label='Parametro a en función del tiempo - Datos de España 1/2/20 al 22/4/20')
axes[1].plot(times, b_params, linewidth=2, color='red',
                  label='Parametro b en función del tiempo - Datos de España 1/2/20 al 22/4/20')

for ax in axes:
    ax.set_xlim(left=0, auto=True)
    ax.set_ylim(bottom=0, auto=True)
    ax.patch.set_facecolor("#ffffff")
    ax.patch.set_edgecolor('black')
    ax.patch.set_linewidth('1')
    ax.set_facecolor("#ffffff")
    ax.grid(color='black', linestyle='--', linewidth=0.5)
    ax.set_xlabel('Dia')
    ax.legend()

plt.show()