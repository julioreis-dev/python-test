class Report:
    def __init__(self, tournament_address, player_address):
        # address to tournament.csv
        self.tournament_address = tournament_address
        # address to player.csv
        self.player_address = player_address
        # registration cost for each player
        self.dict_cost = {1: 1.5, 2: 3, 3: 5, 4: 7}
        # lambda function to return the cost of each level player
        self.calc_price_game = lambda skill: self.dict_cost.get(int(skill) if skill.isdigit() else '', 10)
        self.new_lines_people, self.tournament_lines = None, None

    def open_prepare_file(self) -> None:
        """
        The method is responsible to prepare the files and put in self.new_lines_people or self.tournament_lines
        :return:None
        """
        # dict_columns with column name's of tournament.csv and players.csv
        dict_columns = {0: ['Name', 'Group Stage Matches', 'Elimination Rounds', 'Sport'],
                        1: ['First name', 'Last name', 'Skill level', 'Paid', 'Team', 'Tournament']}
        # list responsible to receive all content of tournament.csv and players.csv
        list_final = []
        for key, address in enumerate([self.tournament_address, self.player_address]):
            with open(address) as fht:
                # Reading all file lines in tournaments.csv
                lines = [row.strip() for row in fht.readlines()][1:]
                # creating a list with dicts
                list_data = [{k: v for k, v in zip(dict_columns[key], line.split(','))} for line in lines]
                # added all contents stored in list_data in list_final
                list_final.append(list_data)
                fht.flush()

        # assigning to each element of list_final to self.tournament_lines and self.new_lines_people
        self.tournament_lines = list_final[0]
        self.new_lines_people = list_final[1]

    def calc_price_tournament(self, person_quote: float, name_tournament: str) -> int:
        """
        The method calculate the price by tournament
        :param person_quote: float
        :param name_tournament: str
        :return: int
        """
        try:
            # filtering by name column and name_tournament
            tournament_line = None
            for line in self.tournament_lines:
                if line['Name'] == name_tournament:
                    tournament_line = line
                    break

            # calculate the value to quote by user
            total_quote = 0
            total_quote += person_quote * int(tournament_line['Group Stage Matches'])
            total_quote += person_quote * (int(tournament_line['Elimination Rounds']) * 2)
        # error handling
        except Exception as err:
            raise Exception(f'Method error -> ({self.calc_price_tournament.__name__}), Error -> {err}')
        else:
            return total_quote

    def final_report(self) -> dict:
        """
        The method is responsible to elaborate the final resume
        :return: dict
        """
        # printing the list with dict each register
        print(self.new_lines_people)

        # creating a dict tournaments to receive all cost by team to each tournament
        tournaments = {}
        for dict_content in self.new_lines_people:
            if not dict_content['Tournament'] in tournaments.keys():
                tournaments[dict_content['Tournament']] = {}
            if not dict_content['Team'] in tournaments[dict_content['Tournament']].keys():
                tournaments[dict_content['Tournament']][dict_content['Team']] = 0

            person_quote = self.calc_price_game(dict_content['Skill level'])
            tournament_quote = self.calc_price_tournament(person_quote, dict_content['Tournament'])
            tournaments[dict_content['Tournament']][dict_content['Team']] = \
                tournaments[dict_content['Tournament']][dict_content['Team']] + tournament_quote

        return tournaments


if __name__ == '__main__':
    # creating instance of Report
    report = Report('../Assignment/data/tournaments.csv', '../Assignment/data/players.csv')
    # call the method open_prepare_file()
    report.open_prepare_file()
    # receving report of tournaments
    all_tournaments = report.final_report()
    # printing the results
    for tournament, teams in all_tournaments.items():
        for team, quote in teams.items():
            print(f"=== {tournament} === {team} => {quote} ===")
