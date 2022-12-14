from sports import Sports  # importing Sport class
from records import Records  # importing Records class


def main():
    """Dear user, run this module to have a interactive way to create tournament_file.csv"""
    try:
        # creating Sport instance
        instance_sports = Sports()
        # storing in sports variable all sports that will be used
        sports = instance_sports.add_sports()
        # creating a dict with all sports
        dict_all_sports = {key + 1: value for key, value in enumerate(sports)}
        # creating Records instance
        instance_records = Records(dict_all_sports)
        # call the method create_content()
        instance_records.create_content()
    # error handling
    except Exception as err:
        raise Exception(f'Aplication Error: {err}')


if __name__ == '__main__':
    main()
