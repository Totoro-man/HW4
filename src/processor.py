import json
from src.interface import Interface
from src.api.api_hh import HhAPI
from src.classes.user import User
from src.classes.vacancy import Vacancy
from datetime import date
from src.classes.data_io import Json_IO

user = User()
user_interface = Interface()
user_requests = HhAPI()


def introduce() -> str:
    result = user_interface.introduce()
    if result == 1:
        step = 'get_info'
    elif result == 0:
        step = 'exit'
    return step


def user_info() -> str:
    result = user_interface.user_info()
    user.info['name'] = result['name']
    user.info['f_name'] = result['f_name']
    user.info['age'] = result['age']
    return 'get_region'


def user_region() -> str:
    user.region_to_check = user_interface.user_region()
    user_requests.set_param({'region_name': user.region_to_check})
    return 'check_region'


def check_region() -> str:
    is_ok, result = user_requests.get_region_id()
    if not is_ok:
        user_interface.print_error(result)
        return 'get_region'
    if len(result) > 1:
        user.regions_list = result
        return 'chose_region'
    user.region = result[0]
    user_requests.set_param({'region_id': user.region.get('id')})
    return 'get_request'


def user_request() -> str:
    request = user_interface.user_request()
    user_requests.set_param(request)
    return 'hw4'


def get_vacancies() -> str:
    is_ok, result = user_requests.get_vacancies()
    if not is_ok:
        user_interface.print_error(result)
        return 'get_request'

    vacancies = Vacancy.set_vacancies_list_from_response_data(result)
    for i in vacancies:
        print(i)
    user.vacancies = result
    save_vacancies()
    step = 'show_vacancies'

    step = 'exit'
    return step


def short_vacancies() -> str:
    result = user_interface.short_vacancies(user.vacancies)
    if result > 0:
        user.chosen_vacancy_id = result
        step = 'show_chosen_vacancy'
    else:
        step = 'get_request'
    return step


def vacancy() -> str:
    # step 1 - Просмотр списка, 2 - Сохранить в файл, 3 - Выход
    result = user_interface.vacancy()
    if result == 1:
        step = 'show_vacancies'
    elif result == 2:
        step = 'save_vacancy'
    else:
        step = 'exit'
    return step


def save_vacancy() -> str:
    file_name: str = str(date.today()) + str(hash(user.info))
    try:
        with open(f'data/{file_name}.json', 'a', encoding='utf-8') as f:
            json.dump(user.saved_vacancies[user.chosen_vacancy_id], f)
    except Exception as e:
        user_interface.print_error(f'{e}')
    return 'show_menu'


def show_saved_vacancies() -> str:
    vacancies = user.saved_vacancies
    result = user_interface.short_vacancies(vacancies)
    if result > 0:
        user.chosen_vacancy_id = result
        step = 'show_chosen_vacancy'
    else:
        step = 'menu'
    return step


def show_vacancy_menu() -> str:
    # step 1 - Просмотр списка, 2 - Просмотр сохраненных вакансий, 3 - Выход
    result = user_interface.show_vacancy_menu()
    if result == 1:
        step = 'show_vacancies'
    elif result == 2:
        step = 'show_saved_vacancies'
    else:
        step = 'exit'
    return step


def chose_region() -> str:
    result = user_interface.chose_region(user.regions_list)
    if result == 0:
        return 'get_region'

    user.region = result
    user_requests.set_param({'region_id': user.region.get('id')})
    return 'get_request'


def save_vacancies():

    with open("data/all_vacancies.json", "w") as outfile:
        json.dump(user.vacancies, outfile, indent=4)


def hw4():
    is_ok, result = user_requests.get_vacancies()
    if not is_ok:
        user_interface.print_error(result)
        return 'get_request'

    vacancies = Vacancy.set_vacancies_list_from_response_data(result)
    Vacancy.print_vacancies(vacancies)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = Vacancy.filter_vacancies(vacancies, filter_words)
    Vacancy.print_vacancies(filtered_vacancies)

    salary_range = input("Введите диапазон зарплат: ").split('-')
    ranged_vacancies = Vacancy.get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = Vacancy.sort_vacancies(ranged_vacancies)
    Vacancy.print_vacancies(sorted_vacancies)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    top_vacancies = Vacancy.get_top_vacancies(sorted_vacancies, top_n)
    Vacancy.print_vacancies(top_vacancies)

    print('Работа с данными в файле')

    test_file = Json_IO('test_vacancies')
    test_file.write(Vacancy.in_json(sorted_vacancies))
    test_file.print()
    test_vacancy = Vacancy.get_top_vacancies(sorted_vacancies,1)[0]
    test_file.delete_string(Vacancy.vacancy_to_json(test_vacancy))
    test_file.print()
    test_file.append_string(Vacancy.vacancy_to_json(test_vacancy))
    test_file.print()
    test_vacancy.name = 'test'
    test_file.update_string(Vacancy.vacancy_to_json(test_vacancy))
    test_file.print()

    return 'exit'
