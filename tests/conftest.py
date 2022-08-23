from main_refactored_class import Report
import pytest


@pytest.fixture(scope='function')
def instance_class_report():
    return Report('tests/file_test/tournament_file.csv', 'tests/file_test/players.csv')