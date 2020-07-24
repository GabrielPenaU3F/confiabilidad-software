import numpy as np

from src.domain.saddlepoint_calculators.purebirth_saddlepoint_calculator import PureBirthSaddlepointCalculator


class HomogeneousPoissonSaddlepointCalculator(PureBirthSaddlepointCalculator):

    def g_second(self, x, k, upper_limit):
        pass
