from src.fitters.ttf_fitter import TTFFitter

ttf_fitter = TTFFitter()
ttf_fitter.fit('goel-okumoto', 'agile-n1')

"""

print(Fore.BLUE + ('a = ' + params_go_mc[0].__str__() + ' (Mínimos cuadrados)'))
print(Fore.BLUE + ('b = ' + params_go_mc[1].__str__() + ' (Mínimos cuadrados)'))
print(Fore.BLUE + ('a = ' + params_go_mv[0].__str__() +
                   '(Máxima verosimilitud, tiempo hasta la falla)'))
print(Fore.BLUE + ('b = ' + params_go_mv[1].__str__() +
                   '(Máxima verosimilitud, tiempo hasta la falla)'))

prr_mc = go.calcular_prr(ttf, fallas_acumuladas, params_go_mc[0], params_go_mc[1])
prr_mv = go.calcular_prr(ttf, fallas_acumuladas, params_go_mv[0], params_go_mv[1])
print(Fore.GREEN + ('PRR - Mínimos cuadrados: ' + prr_mc.__str__()))
print(Fore.GREEN + ('PRR - Máxima verosimilitud: ' + prr_mv.__str__()))

aic_mv = go.calcular_aic_tiempo_hasta_la_falla(ttf, fallas_acumuladas[-1], params_go_mv[0], params_go_mv[1])
print(Fore.GREEN + ('AIC (Tiempo hasta la falla): ' + aic_mv.__str__()))

"""