import unittest

from src.fitters.fitter import GroupedCumulativeFitter


class LogisticTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedCumulativeFitter().fit('logistic', 'mixed-waterfall-agile')

    # No se puede testear, no ajusta el metodo
    # Todo: revisar y corregir el problema si es posible
