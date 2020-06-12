import os
import unittest

from src.data.data_repository import DataRepository
from src.domain.fitters.model_fitter import ModelFitter


class TestReadDataFromOdsFile(unittest.TestCase):

    agile1_repo_fit = None
    agile1_file_fit = None

    #   This test will only work if executed directly, not from a higher level directory
    @classmethod
    def setUpClass(cls):
        DataRepository.load_project_data_from_file(path="../../test_resource_files/agile_n1_data.ods")
        fitter = ModelFitter()
        cls.agile1_repo_fit = fitter.fit('delayed-s-shaped', 'agile-n1')
        cls.agile1_file_fit = fitter.fit('delayed-s-shaped', 'agile-n1-fromfile')

    def test_fit_parameters_must_be_equal(self):
        a_repo = self.agile1_repo_fit.get_ml_parameters()[0]
        b_repo = self.agile1_repo_fit.get_ml_parameters()[1]
        a_file = self.agile1_file_fit.get_ml_parameters()[0]
        b_file = self.agile1_file_fit.get_ml_parameters()[1]
        self.assertEqual(a_repo, a_file)
        self.assertEqual(b_repo, b_file)
