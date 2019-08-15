from src.fitters.ttf_fitter import TTFFitter

ttf_fitter = TTFFitter()
ttf_fitter.fit('logistic', 'ntds')

"""

print(Fore.BLUE + ('a = ' + params_log_mc[0].__str__() + ' (Mínimos cuadrados)'))
print(Fore.BLUE + ('b = ' + params_log_mc[1].__str__() + ' (Mínimos cuadrados)'))
print(Fore.BLUE + ('c = ' + params_log_mc[2].__str__() + ' (Mínimos cuadrados)'))
print(Fore.BLUE + ('a = ' + params_log_mv[0].__str__() +
                   '(Máxima verosimilitud, tiempo hasta la falla)'))
print(Fore.BLUE + ('b = ' + params_log_mv[1].__str__() +
                   '(Máxima verosimilitud, tiempo hasta la falla)'))
print(Fore.BLUE + ('c = ' + params_log_mv[2].__str__() +
                   '(Máxima verosimilitud, tiempo hasta la falla)'))

prr_mc = log.calcular_prr(ttf, fallas_acumuladas, params_log_mc[0], params_log_mc[1], params_log_mc[2])
prr_mv = log.calcular_prr(ttf, fallas_acumuladas, params_log_mv[0], params_log_mv[1], params_log_mv[2])
print(Fore.GREEN + ('PRR - Mínimos cuadrados: ' + prr_mc.__str__()))
print(Fore.GREEN + ('PRR - Máxima verosimilitud: ' + prr_mv.__str__()))

aic_mv = log.calcular_aic_tiempo_hasta_la_falla(ttf_sin_cero, n_fallas, params_log_mv[0], params_log_mv[1],
                                                params_log_mv[2])
print(Fore.GREEN + ('AIC (Tiempo hasta la falla): ' + aic_mv.__str__()))

"""
