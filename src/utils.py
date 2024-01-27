import json

from src.interface import Interface
from src.user_request import UserRequest
from src.user import User
from datetime import date

user = User()
user_interface = Interface()
user_requests = UserRequest()


def introduce() -> int:
    step = user_interface.introduce()
    return step


def user_info() -> int:
    result = user_interface.user_info(user.info)
    user.info['name'] = result['name']
    user.info['fname'] = result['fname']
    user.info['age'] = result['age']
    return 3


def user_region() -> int:
    user.region_to_check = user_interface.user_region()
    print(f'{user.info["name"]}\n'
          f'{user.info["fname"]}\n'
          f'{user.info["age"]}\n'
          f'{user.region_to_check}')
    return 0


def check_region() -> int:
    is_ok, result = user_requests.check_region(user.region_to_check)
    if is_ok:
        user.request['region'] = result
        step = 5
    else:
        user_interface.print_error(result)
        step = 3
    return step


def user_request() -> int:
    request = user_interface.user_request()
    user.request['profession'] = request['profession']
    user.request['min_salary'] = request['min_salary']
    user.request['schedule'] = request['schedule']
    user.request['employment'] = request['employment']
    return 6


def get_vacancies() -> int:
    is_ok, result = user_requests.get_vacancies(user.request)
    if is_ok:
        user.vacancies = result
        step = 7
    else:
        user_interface.print_error(result)
        step = 5
    return step


def short_vacancies() -> int:
    result = user_interface.short_vacancies(user.vacancies)
    if result > 0:
        user.chosen_vacancy_id = result
        step = 8
    else:
        step = result
    return step


def vacancy() -> int:
    step = user_interface.vacancy()
    return step


def save_vacancy() -> int:
    file_name: str = str(date.today()) + str(hash(user.info))
    try:
        with open(f'data/{file_name}.json', 'a', encoding='utf-8') as f:
            json.dump(user.saved_vacancies[user.chosen_vacancy_id], f)
    except Exception as e:
        user_interface.print_error(f'{e}')
    return 11


def show_saved_vacancies() -> int:
    vacancies = user.saved_vacancies
    result = user_interface.short_vacancies(vacancies)
    if result > 0:
        user.chosen_vacancy_id = result
        step = 8
    else:
        step = result
    return step


def show_vacancy_menu() -> int:
    step = user_interface.show_vacancy_menu()
    return step
