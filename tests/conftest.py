import pytest

import tests.utils as utils
from src.rasa_model_report.controllers.CsvController import CsvController
from src.rasa_model_report.controllers.JsonController import JsonController


def pytest_generate_tests(metafunc):
    metafunc.fixturenames.append('rasa_path')
    metafunc.parametrize('rasa_path', ["tests/rasa_mock/rasa_2", "tests/rasa_mock/rasa_3"])


@pytest.fixture(autouse=True)
def execute_before_each_test(rasa_path):
    json_controller = JsonController(rasa_path, "./tests", "test-project", "0.0.0")
    csv_controller = CsvController(rasa_path, "./tests", "test-project", "0.0.0")
    pytest.json_controller = json_controller
    pytest.csv_controller = csv_controller
    pytest.file_name = "test.csv"
    yield
    utils.remove_generated_files(rasa_path)
