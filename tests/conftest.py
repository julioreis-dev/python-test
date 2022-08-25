from answer.main_refactored_class import Report
import pytest


@pytest.fixture(scope='function')
def instance_class_report():
    return Report('tests/file_test/tournament_test.csv', 'tests/file_test/players_test.csv')