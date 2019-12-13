from abc import ABC, abstractmethod
import scipy.special as sp
import numpy as np


class GammaStrategy(ABC):

    gamma = None
    augmenting_factor = 100000

    def __init__(self, k, min_decimals):
        self.k = k
        if min_decimals is not None:
            self.augmenting_factor = 10 ** min_decimals

    def get_gamma(self):
        return self.gamma

    @abstractmethod
    def denormalize_lower_incomplete_gamma(self, normalized_lower_incomplete_gamma):
        pass

    def lower_incomplete_gamma(self, upper_limit):
        normalized_lower_incomplete_gamma = sp.gammainc(self.k, upper_limit)
        return self.denormalize_lower_incomplete_gamma(normalized_lower_incomplete_gamma)


class ExactGammaStrategy(GammaStrategy):

    def __init__(self, k, min_decimals):
        super().__init__(k, min_decimals)
        self.gamma = sp.gamma(k)

    def denormalize_lower_incomplete_gamma(self, normalized_lower_incomplete_gamma):
        return self.gamma * normalized_lower_incomplete_gamma


class LargeKApproximationGammaStrategy(GammaStrategy):

    def __init__(self, k, min_decimals):
        super().__init__(k, min_decimals)
        # Factorial approximation for the gamma function
        self.gamma = np.math.factorial(np.math.floor(k - 1))

    def denormalize_lower_incomplete_gamma(self, normalized_lower_incomplete_gamma):
        normalized_lower_incomplete_gamma_augmented = int(normalized_lower_incomplete_gamma * self.augmenting_factor)
        return np.floor_divide(self.gamma * normalized_lower_incomplete_gamma_augmented, self.augmenting_factor)

