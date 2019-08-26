import unittest

from src.fitters.fitter import GroupedFailuresPerDayFitter


class LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedFailuresPerDayFitter().fit('logistic', 'mixed-waterfall-agile')

    # No se puede testear, no ajusta el metodo
    # Todo: revisar y corregir el problema si es posible
