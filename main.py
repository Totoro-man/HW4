import sys
from src.processor import *


def main():

    user_step = 'get_region'

    while user_step != 'exit':

        if user_step == 'intro':
            user_step = introduce()
        if user_step == 'get_info':
            user_step = user_info()
        if user_step == 'get_region':
            user_step = user_region()
        if user_step == 'check_region':
            user_step = check_region()
        if user_step == 'get_request':
            user_step = user_request()
        if user_step == 'get_vacancies':
            user_step = get_vacancies()
        if user_step == 'show_vacancies':
            user_step = short_vacancies()
        if user_step == 'show_chosen_vacancy':
            user_step = vacancy()
        if user_step == 'save_vacancy':
            user_step = save_vacancy()
        if user_step == 'show_saved_vacancies':
            user_step = show_saved_vacancies()
        if user_step == 'show_menu':
            user_step = show_vacancy_menu()
        if user_step == 'chose_region':
            user_step = chose_region()
        if user_step == 'hw4':
            user_step = hw4()
        if user_step == 'exit':
            sys.exit()


if __name__ == '__main__':
    main()
