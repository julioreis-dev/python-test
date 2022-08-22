import pandas as pd  # import pandas library


class Records:
    def __init__(self, dict_sport):
        self.dict_sport = dict_sport
        self.list_name, self.list_group, self.list_elimination, self.list_sport = [], [], [], []

    def create_records(self) -> None:
        """Function responsible to create records to .csv file"""
        try:
            # starting the procedure of fill up each row
            print('########## Add as many register as you need ##########')
            # question to column 1
            self.list_name.append(input('Enter with tournament name:'))
            # question to column 2
            group = input('Enter with number group, e.g.(0 or 3):')
            self.list_group.append(self.verify_answer(1, group))
            # question to column 3
            elimination = input('Enter with the list_elimination, e.g.(2, 3 or 4):')
            self.list_elimination.append(self.verify_answer(2, elimination))
            # question to column 4
            self.list_sport.append(self.choose_modality())
        except Exception as err:
            raise Exception(f'Method -> ({self.create_records.__name__}), Error -> {err}')

    def confirmation_records(self) -> bool:
        """Function responsible to control the flow of add lines in final file"""
        try:
            # question to know if the use wants add more lines in the file
            question = input('###############################\n'
                             'Do you want add more lines???\n'
                             '----------------------\n'
                             'Enter "Y" --> Yes\n'
                             'Enter "N" --> No\n'
                             '----------------------\n'
                             '----> ')
            # converting the answer in lowercase
            character = question.lower()
            # procedure to confirm the answer. If "y" return True or "n" return False else restart confirmation_records
            if character in ['y', 'n']:
                response_bool = {'y': True, 'n': False}
                return response_bool[character]
            else:
                # procedure to help the user. If the use choose a option different of "y" or "n"
                print('\nAnswer incorrect, Try again!!!')
                return self.confirmation_records()
        except Exception as err:
            raise Exception(f'Method -> ({self.confirmation_records.__name__}), Error -> {err}')

    def verify_answer(self, opt: int, answer: str) -> object:
        """Function responsible to verify the answer"""
        try:
            # verify the answer variable is a number or string
            number = int(answer) if answer.isdigit() else ''
            # verify the answer received by number group column
            if opt == 1:
                # if the number is in [0, 3] will return the number
                if number in [0, 3]:
                    return number
                else:
                    # if the answer is not in [0, 3], this part restart all procedure
                    response = input('Answer incorrect, Try again!!!\nEnter with number group, e.g.(0 or 3):')
                    return self.verify_answer(1, response)
            else:
                # verify the answer received by list_elimination column
                # if the number is in [2, 3, 4] will return the number
                if number in [2, 3, 4]:
                    return number
                else:
                    # if the answer is not in [2, 3, 4], this part restart all procedure
                    response = input(
                        'Answer incorrect, Try again!!!\nEnter with the list_elimination, e.g.(2, 3 or 4):')
                    return self.verify_answer(2, response)
        except Exception as err:
            raise Exception(f'Function -> ({self.verify_answer.__name__}), Error -> {err}')

    def choose_modality(self) -> bool:
        """Function to show all sports options to user"""
        try:
            # creating the flag variable to control the flow inside the while and response variable
            # to keep the option chosen by user
            flag = True
            response = None
            while flag:
                # starting the procedure to receive the answer about sports options
                print('###############################')
                print('Enter sport number:')
                print('--------------------------------')
                # show all options registered as sport
                for key, value in self.dict_sport.items():
                    print(f'Enter number "{key}" -> {value}')
                print('--------------------------------')
                sport = input(f'--> ')
                # extracting the value in self.dict_sport using sport variable like key. if the answer
                # in sport variable is not in self.dict_sport will return "incorrect"
                response = self.dict_sport.get(int(sport), 'incorrect')
                # if the answer is not in self.dict_sport the variable will return "incorrect" and all procedure
                # will restart
                if response == 'incorrect':
                    print('Answer incorrect, Try again!!!')
                else:
                    # if the answer stored in sport variable is in self.dict_sport the flag will receive False
                    flag = False
        except Exception as err:
            raise Exception(f'Method -> ({self.choose_modality.__name__}), Error -> {err}')
        else:
            return response

    def create_content(self) -> None:
        """Function responsible to receive all information to each column in file .csv"""
        try:
            # creating the flag variable to control the flow inside the while
            flag = True
            while flag:
                # call the method self.create_records()
                self.create_records()
                # stored in flag variable the return of self.confirmation_records()
                flag = self.confirmation_records()
            self.create_file(name=self.list_name, group=self.list_group, elimination=self.list_elimination,
                             sport=self.list_sport)
        except Exception as err:
            raise Exception(f'Method -> ({self.create_content.__name__}), Error -> {err}')

    def create_file(self, **kwargs: object) -> None:
        """Function to create the final file .csv"""
        try:
            # creating data variable to populate the final dataframe
            data = {
                'Name': kwargs.get('name'),
                'Group Stage Matches': kwargs.get('group'),
                'Elimination Matches': kwargs.get('elimination'),
                'Sport': kwargs.get('sport')
            }
            # creating dataframe with pandas library
            tournament_df = pd.DataFrame(data)
            # converting the dataframe to tournament_file.csv without index
            tournament_df.to_csv('tournament_file.csv', index=False)
        except Exception as err:
            raise Exception(f'Method -> ({self.create_file.__name__}), Error -> {err}')