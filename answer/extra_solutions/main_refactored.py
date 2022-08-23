def open_prepare_file(status: int, address_file: str) -> list:
    """Function responsible to prepare the files"""
    list_file1 = ['Name', 'Group Stage Matches', 'Elimination Rounds', 'Sport']
    list_file2 = ['First name', 'Last name', 'Skill level', 'Paid', 'Team', 'Tournament']
    with open(address_file) as fht:
        # Reading all file lines in tournaments.csv
        lines = [row.strip() for row in fht.readlines()][1:]
        # creating a list with dicts where the keys are elements in list_file1 or list_file2
        list_data = [{k: v for k, v in zip(list_file1 if status == 1 else list_file2, line.split(','))}
                     for line in lines]
        fht.flush()
    return list_data


def calc_price_tournament(tournaments: list, person_quote: float, tournament: str) -> float:
    """This function calculate the price each tournament"""

    # calculating quote by tournament
    tournament_line = None
    for t in tournaments:
        if t['Name'] == tournament:
            tournament_line = t

    total_quote = 0
    total_quote += person_quote * int(tournament_line['Group Stage Matches'])
    total_quote += person_quote * (int(tournament_line['Elimination Rounds']) * 2)

    return total_quote


def main(tournaments_list: list, new_lines_people: list) -> None:
    print(new_lines_people)
    # cost for skill level (key: value -> skill level: cost for level)
    dict_cost = {1: 1.5, 2: 3, 3: 5, 4: 7}
    # lambda function to calculate the cost for each player. params = (data: dict, cost: dict) -> int
    calc_price_game = lambda data, cost: cost.get(0 if data['Skill level'] == '' else int(data['Skill level']), 10)

    # creating a dict with all datas by tournament
    tournaments = {}
    for dict_content in new_lines_people:
        if not dict_content['Tournament'] in tournaments.keys():
            tournaments.setdefault(dict_content['Tournament'], {dict_content['Team']: 0})
        if not dict_content['Team'] in tournaments[dict_content['Tournament']].keys():
            tournaments[dict_content['Tournament']][dict_content['Team']] = 0

        person_quote = calc_price_game(dict_content, dict_cost)
        tournament_quote = calc_price_tournament(tournaments_list, person_quote, dict_content['Tournament'])
        tournaments[dict_content['Tournament']][dict_content['Team']] = \
            tournaments[dict_content['Tournament']][dict_content['Team']] + tournament_quote

    # printing all results
    for tournament, teams in tournaments.items():
        for team, quote in teams.items():
            print(f"=== {tournament} === {team} => {str(quote)} ===")


if __name__ == '__main__':
    group_games = open_prepare_file(1, '../Assignment/data/tournaments.csv')
    lines_people = open_prepare_file(2, '../Assignment/data/players.csv')
    main(group_games, lines_people)
