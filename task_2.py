import pandas as pd  # import pandas library


def confirmation_sports() -> bool:
    """Function responsible to control the flow of add sports"""
    try:
        question = input('###############################\n'
                         'Choose one option, as below:\n'
                         '----------------------\n'
                         'Enter "Y" --> Yes\n'
                         'Enter "N" --> No\n'
                         '----------------------\n'
                         'Do you want add more sports???')
        character = question.lower()
        if character in ['y', 'n']:
            response_bool = {'y': True, 'n': False}
            return response_bool[character]
        else:
            print('\nAnswer incorrect, Try again!!!')
            return confirmation_sports()
    except Exception as err:
        raise Exception(f'Function -> ({confirmation_sports.__name__}), Error -> {err}')


def confirmation_records() -> bool:
    """Function responsible to control the flow of add lines in final file"""
    try:
        question = input('###############################\n'
                         'Choose one option, as below:\n'
                         '----------------------\n'
                         'Enter "Y" --> Yes\n'
                         'Enter "N" --> No\n'
                         '----------------------\n'
                         'Do you want add more lines???')
        character = question.lower()
        if character in ['y', 'n']:
            response_bool = {'y': True, 'n': False}
            return response_bool[character]
        else:
            print('\nAnswer incorrect, Try again!!!')
            return confirmation_records()
    except Exception as err:
        raise Exception(f'Function -> ({confirmation_records.__name__}), Error -> {err}')


def add_sports() -> list:
    """Function to receive and add sports"""
    try:
        flag = True
        list_sport = []
        while flag:
            print('###############################')
            list_sport.append(input('Enter a sport:'))
            flag = confirmation_sports()
        return list_sport
    except Exception as err:
        raise Exception(f'Function -> ({add_sports.__name__}), Error -> {err}')


def verify_number_answer(opt: int, answer: str) -> object:
    """Function responsible to verify the answer is a number or string"""
    try:
        if opt == 1:
            if int(answer) in [0, 3]:
                return answer
            else:
                response = input('Answer incorrect, Try again!!!\nEnter with number group, e.g.(0 or 3):')
                return verify_answer(1, response)
        else:
            if int(answer) in [2, 3, 4]:
                return answer
            else:
                response = input('Answer incorrect, Try again!!!\nEnter with the list_elimination, e.g.(2, 3 or 4):')
                return verify_answer(2, response)
    except Exception as err:
        raise Exception(f'Function -> ({verify_number_answer.__name__}), Error -> {err}')


def verify_answer(opt: int, answer: str) -> object:
    """Function responsible to verify if the answer is a number or string"""
    try:
        if answer.isdigit():
            return verify_number_answer(opt, answer)
        elif opt == 1:
            response = input('Answer incorrect, Try again!!!\nEnter with number group, e.g.(0 or 3):')
            return verify_answer(1, response)
        elif opt == 2:
            response = input('Answer incorrect, Try again!!!\nEnter with the list_elimination, e.g.(2, 3 or 4):')
            return verify_answer(2, response)
    except Exception as err:
        raise Exception(f'Function -> ({verify_answer.__name__}), Error -> {err}')


def choose_modality(dict_sport: dict) -> bool:
    """Function to show all sports options to user"""
    try:
        flag = True
        response = None
        while flag:
            print('###############################')
            print('Choose one option, as below:')
            print('----------------------')
            for key, value in dict_sport.items():
                print(f'Enter "{key}" -> {value}')
            print('----------------------')
            sport = input(f'Enter sport number:')
            response = dict_sport.get(int(sport), 'incorrect')
            if response == 'incorrect':
                print('Answer incorrect, Try again!!!')
            else:
                flag = False
        return response
    except Exception as err:
        raise Exception(f'Function -> ({choose_modality.__name__}), Error -> {err}')


def create_records(dict_sport: dict) -> tuple:
    """Function responsible to create records to .csv file"""
    try:
        aux_name, aux_group, aux_elimination, aux_sport = [], [], [], []
        aux_name.append(input('###############################\nEnter with name:'))
        group = input('Enter with number group, (0 or 3):')
        aux_group.append(verify_answer(1, group))
        elimination = input('Enter with the list_elimination, (2, 3 or 4):')
        aux_elimination.append(verify_answer(2, elimination))
        sport = choose_modality(dict_sport)
        aux_sport.append(sport)
        return aux_name, aux_group, aux_elimination, aux_sport
    except Exception as err:
        raise Exception(f'Function -> ({create_records.__name__}), Error -> {err}')


def create_file(**kwargs: object) -> None:
    """Function to create the file tournament_file.csv"""
    try:
        data = {
            'Name': kwargs.get('name'),
            'Group Stage Matches': kwargs.get('group'),
            'Elimination Matches': kwargs.get('elimination'),
            'Sport': kwargs.get('sport')
        }
        tournament_df = pd.DataFrame(data)
        tournament_df.to_csv('tournament_file.csv', index=False)
    except Exception as err:
        raise Exception(f'Function -> ({create_file.__name__}), Error -> {err}')


def create_content(dict_sport: dict) -> None:
    """Function responsible to receive all information to each column in file .csv"""
    try:
        flag = True
        list_name, list_group, list_elimination, list_sport = [], [], [], []
        while flag:
            response = create_records(dict_sport)
            list_name.extend(response[0])
            list_group.extend(response[1])
            list_elimination.extend(response[2])
            list_sport.extend(response[3])
            flag = confirmation_records()
        create_file(name=list_name, group=list_group, elimination=list_elimination, sport=list_sport)
    except Exception as err:
        raise Exception(f'Function -> ({create_content.__name__}), Error -> {err}')


def main():
    try:
        sports = add_sports()
        dict_all_sports = {key + 1: value for key, value in enumerate(sports)}
        create_content(dict_all_sports)
    except Exception as err:
        raise Exception(f'Aplication Error: {err}')


if __name__ == '__main__':
    main()
