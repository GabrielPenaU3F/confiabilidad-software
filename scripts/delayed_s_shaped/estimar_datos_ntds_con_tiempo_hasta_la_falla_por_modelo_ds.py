from src.fitters.ttf_fitter import TTFFitter

ttf_fitter = TTFFitter()
ttf_fitter.fit('delayed-s-shaped', 'ntds')

"""

print(Fore.BLUE + ('a = ' + params_ds_mc[0].__str__() + ' (Mínimos cuadrados)'))
print(Fore.BLUE + ('b = ' + params_ds_mc[1].__str__() + ' (Mínimos cuadrados)'))
print(Fore.BLUE + ('a = ' + params_ds_mv[0].__str__() +
                   '(Máxima verosimilitud, tiempo hasta la falla)'))
print(Fore.BLUE + ('b = ' + params_ds_mv[1].__str__() +
                   '(Máxima verosimilitud, tiempo hasta la falla)'))

prr_mc = ds.calcular_prr(ttf, fallas_acumuladas, params_ds_mc[0], params_ds_mc[1])
prr_mv = ds.calcular_prr(ttf, fallas_acumuladas, params_ds_mv[0], params_ds_mv[1])
print(Fore.GREEN + ('PRR - Mínimos cuadrados: ' + prr_mc.__str__()))
print(Fore.GREEN + ('PRR - Máxima verosimilitud: ' + prr_mv.__str__()))

aic_mv = ds.calcular_aic_tiempo_hasta_la_falla(ttf_sin_cero, n_fallas,  params_ds_mv[0], params_ds_mv[1])
print(Fore.GREEN + ('AIC (Tiempo hasta la falla): ' + aic_mv.__str__()))

"""

