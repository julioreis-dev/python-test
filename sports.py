
class Sports:
    def __init__(self):
        pass

    def add_sports(self) -> list:
        """Function to receive and add sports"""
        try:
            flag = True
            list_sport = []
            while flag:
                print('########## Add as many sports as you need ##########')
                list_sport.append(input('Enter a sport:'))
                flag = self.confirmation_sports()
        except Exception as err:
            raise Exception(f'Function -> ({self.add_sports.__name__}), Error -> {err}')
        else:
            return list_sport

    def confirmation_sports(self) -> bool:
        """Function responsible to control the flow of add sports"""
        try:
            question = input('###############################\n'
                             'Do you want add more sports???\n'
                             '------------------\n'
                             'Enter "Y" --> Yes\n'
                             'Enter "N" --> No\n'
                             '------------------\n'
                             '--> ')
            character = question.lower()
            if character in ['y', 'n']:
                response_bool = {'y': True, 'n': False}
                return response_bool[character]
            else:
                print('\nAnswer incorrect, Try again!!!')
                return self.confirmation_sports()
        except Exception as err:
            raise Exception(f'Function -> ({self.confirmation_sports.__name__}), Error -> {err}')