import sys
from src.utils import *


def main():

    user_step = 1

    while user_step > 0:

        if user_step == 1:
            user_step = introduce()
        if user_step == 2:
            user_step = user_info()
        if user_step == 3:
            user_step = user_region()
        if user_step == 4:
            user_step = check_region()
        if user_step == 5:
            user_step = user_request()
        if user_step == 6:
            user_step = get_vacancies()
        if user_step == 7:
            user_step = short_vacancies()
        if user_step == 8:
            user_step = vacancy()
        if user_step == 9:
            user_step = save_vacancy()
        if user_step == 10:
            user_step = show_saved_vacancies()
        if user_step == 11:
            user_step = show_vacancy_menu()
        if user_step == 0:
            sys.exit()


if __name__ == '__main__':
    main()
