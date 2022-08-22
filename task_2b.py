from sports import Sports
from records import Records


def main():
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
    except Exception as err:
        raise Exception(f'Aplication Error: {err}')


if __name__ == '__main__':
    main()
