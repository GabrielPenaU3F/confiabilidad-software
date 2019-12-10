import numpy as np
import scipy.optimize as opt


def find_maximum(function, initial_guess, *args):
    return opt.minimize(lambda x: -function(x, *args), x0=initial_guess, bounds=((0, 10000),)).x[0]
