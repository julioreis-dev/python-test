
class Sports:
    def __init__(self):
        pass

    def add_sports(self) -> list:
        """Function to register sports"""
        try:
            # creating the flag variable to control the flow inside the while
            flag = True
            # creating a list to store all sports registered
            list_sport = []
            while flag:
                # starting the procedure to add sports
                print('########## Add as many sports as you need ##########')
                list_sport.append(input('Enter a sport:'))
                flag = self.confirmation_sports()
        # error handling
        except Exception as err:
            raise Exception(f'Function -> ({self.add_sports.__name__}), Error -> {err}')
        else:
            return list_sport

    def confirmation_sports(self) -> bool:
        """Function responsible to control the flow of add sports"""
        try:
            # question to know if the use wants add sports
            question = input('###############################\n'
                             'Do you want add more sports???\n'
                             '------------------\n'
                             'Enter "Y" --> Yes\n'
                             'Enter "N" --> No\n'
                             '------------------\n'
                             '----> ')
            # converting the answer in lowercase
            character = question.lower()
            # procedure to confirm the answer. If "y" return True or "n" return False else
            # restart self.confirmation_sports()
            if character in ['y', 'n']:
                response_bool = {'y': True, 'n': False}
                return response_bool[character]
            else:
                # procedure to help the user. If the use choose a option different of "y" or "n"
                print('\nAnswer incorrect, Try again!!!')
                return self.confirmation_sports()
        # error handling
        except Exception as err:
            raise Exception(f'Function -> ({self.confirmation_sports.__name__}), Error -> {err}')
