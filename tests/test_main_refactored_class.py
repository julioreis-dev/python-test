import pytest


def test_open_prepare_file_method_call(instance_class_report):
    assert instance_class_report.tournament_address == 'tests/file_test/tournament_file.csv'
    assert instance_class_report.player_address == 'tests/file_test/players.csv'
    assert instance_class_report.dict_cost == {1: 1.5, 2: 3, 3: 5, 4: 7}
    assert instance_class_report.tournament_lines is None
    assert instance_class_report.new_lines_people is None


def test_open_prepare_file_method(instance_class_report):
    instance_class_report.open_prepare_file()
    assert instance_class_report.tournament_lines == [{'Elimination Rounds': '2',
                                                       'Group Stage Matches': '0',
                                                       'Name': 'Apple Tournament',
                                                       'Sport': 'Soccer'}]
    assert instance_class_report.new_lines_people == [{'First name': 'Isaac',
                                                       'Last name': 'Abbenante',
                                                       'Paid': 'Yes',
                                                       'Skill level': '2',
                                                       'Team': 'Team 5',
                                                       'Tournament': 'Apple Tournament'}]


@pytest.mark.parametrize('_input, expected', [('1', 1.5), ('2', 3), ('3', 5), ('4', 7), ('5', 10), ('', 10)])
def test_calc_price_game_method(instance_class_report, _input, expected):
    instance_class_report.open_prepare_file()
    assert instance_class_report.calc_price_game(_input) == expected


@pytest.mark.parametrize('_input, expected', [(1.5, 6), (3, 12), (5, 20), (7, 28), (10, 40)])
def test_calc_price_tournament_method(instance_class_report, _input, expected):
    instance_class_report.open_prepare_file()
    assert instance_class_report.calc_price_tournament(_input, 'Apple Tournament') == expected


def test_final_report(instance_class_report):
    instance_class_report.open_prepare_file()
    assert instance_class_report.final_report() == {'Apple Tournament': {'Team 5': 12}}


def test_raise_calc_price_game(instance_class_report):
    with pytest.raises(Exception) as err:
        instance_class_report.open_prepare_file()
        instance_class_report.calc_price_game()
    assert "<lambda>() missing 1 required positional argument: 'skill'" == str(err.value)


@pytest.mark.parametrize('_input', ['', '2'])
def test_raise_calc_price_tournament_method(instance_class_report, _input):
    with pytest.raises(Exception) as err:
        instance_class_report.open_prepare_file()
        instance_class_report.calc_price_tournament(_input, 'Apple Tournament')
    assert "Method error -> (calc_price_tournament), Error -> unsupported operand type(s) for +=: 'int' and 'str'" \
           == str(err.value)
