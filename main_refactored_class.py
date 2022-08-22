class Report:
    def __init__(self, tournament_address, player_address):
        self.tournament_address = tournament_address
        self.player_address = player_address
        self.dict_cost = {1: 1.5, 2: 3, 3: 5, 4: 7}
        self.new_lines_people, self.tournament_lines = None, None

    def open_prepare_file(self) -> None:
        """
        The method is responsible to prepare the files and put in self.new_lines_people or self.tournament_lines
        :return:None
        """
        try:
            dict_columns = {0: ['Name', 'Group Stage Matches', 'Elimination Rounds', 'Sport'],
                            1: ['First name', 'Last name', 'Skill level', 'Paid', 'Team', 'Tournament']}
            list_final = []
            for key, address in enumerate([self.tournament_address, self.player_address]):
                with open(address) as fht:
                    # Reading all file lines in tournaments.csv
                    lines = [row.strip() for row in fht.readlines()][1:]
                    # creating a list with dicts where the keys are elements in list_file1 or list_file2
                    list_data = [{k: v for k, v in zip(dict_columns[key], line.split(','))}
                                 for line in lines]
                    list_final.append(list_data)
                    fht.flush()
        except Exception as err:
            raise Exception(f'Method error -> ({self.open_prepare_file.__name__}), Error -> {err}')
        else:
            self.tournament_lines = list_final[0]
            self.new_lines_people = list_final[1]

    def calc_price_tournament(self, person_quote: float, tournament: str) -> int:
        """
        The method calculate the price by tournament
        :param person_quote: float
        :param tournament: str
        :return: int
        """
        try:
            tournament_line = None
            for line in self.tournament_lines:
                if line['Name'] == tournament:
                    tournament_line = line

            total_quote = 0
            total_quote += person_quote * int(tournament_line['Group Stage Matches'])
            total_quote += person_quote * (int(tournament_line['Elimination Rounds']) * 2)
        except Exception as err:
            raise Exception(f'Method error -> ({self.calc_price_tournament.__name__}), Error -> {err}')
        else:
            return total_quote

    def main(self) -> dict:
        """
        The method main responsible to run the script
        :return: dict
        """
        try:
            print(self.new_lines_people)
            calc_price_game = lambda skill_level: self.dict_cost.get('' if skill_level == '' else int(skill_level), 10)

            tournaments = {}
            for dict_content in self.new_lines_people:
                if not dict_content['Tournament'] in tournaments.keys():
                    tournaments[dict_content['Tournament']] = {}
                if not dict_content['Team'] in tournaments[dict_content['Tournament']].keys():
                    tournaments[dict_content['Tournament']][dict_content['Team']] = 0

                person_quote = calc_price_game(dict_content['Skill level'])
                tournament_quote = self.calc_price_tournament(person_quote, dict_content['Tournament'])
                tournaments[dict_content['Tournament']][dict_content['Team']] = \
                    tournaments[dict_content['Tournament']][dict_content['Team']] + tournament_quote
        except Exception as err:
            raise Exception(f'Method error -> ({self.main.__name__}), Error -> {err}')
        else:
            return tournaments


if __name__ == '__main__':
    report = Report('Assignment/data/tournaments.csv', 'Assignment/data/players.csv')
    report.open_prepare_file()
    all_tournaments = report.main()
    for tournament, teams in all_tournaments.items():
        for team, quote in teams.items():
            print(f"=== {tournament} === {team} => {quote} ===")
