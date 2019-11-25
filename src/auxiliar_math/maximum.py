import numpy as np
import scipy.optimize


def find_maximum(function, initial_approx, *args):
    return scipy.optimize.minimize_scalar(lambda x: -function(x, *args), bounds=((1, 1000),))
