class Vacancy:

    def __init__(self,  vacancy_id: str = '', name: str = '', description: str = '', requirement: str = '', url: str = '', salary: int = 0):
        self.__id = vacancy_id
        self.__name = name
        self.__description = description
        self.__requirement = requirement
        self.__url = url
        self.__salary = salary

    def __str__(self):
        return f'{self.__id} | {self.__name} | {self.__salary} | {self.__description}'

    def __ge__(self, other):
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        if isinstance(other, (int, float)):
            return self.salary >= other
        return TypeError

    def __le__(self, other):
        if isinstance(other, Vacancy):
            return self.salary <= other.salary
        if isinstance(other, (int, float)):
            return self.salary <= other
        return TypeError

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, text: str):
        if isinstance(text, str):
            self.__id = text
        else:
            self.__id = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, text: str):
        if isinstance(text, str):
            self.__name = text
        else:
            self.__name = ''

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, text: str):
        if isinstance(text, str):
            self.__description = text
        else:
            self.__description = ''

    @property
    def requirement(self):
        return self.__requirement

    @requirement.setter
    def requirement(self, text: str):
        if isinstance(text, str):
            self.__requirement = text
        else:
            self.__requirement = ''

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, text: str):
        if isinstance(text, str):
            self.__url = text
        else:
            self.__url = ''

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount: str):
        try:
            amount = int(amount)
            self.__salary = amount
        except:
            self.__salary = 0

    @staticmethod
    def init_from_json_string(source_string: dict):
        vacancy = Vacancy()
        vacancy.id = source_string.get('id')
        vacancy.name = source_string.get('name')
        vacancy.description = source_string.get('snippet').get('responsibility')
        vacancy.requirement = source_string.get('snippet').get('requirement')
        vacancy.url = source_string.get('url')
        vacancy.salary = source_string.get('salary').get('from')
        return vacancy

    @staticmethod
    def set_vacancies_list_from_response_data(source_data: list):
        vacancies_list: list = []
        for i in source_data:
            vacancy = Vacancy.init_from_json_string(i)
            vacancies_list.append(vacancy)
        return vacancies_list

    @staticmethod
    def filter_vacancies(vacancies_list: list, filter_words: list) -> list:
        result: list = []
        for i in vacancies_list:
            vacancy_dict = (i.name.lower() + ' ' + i.description.lower() + ' ' + i.requirement.lower()).split()
            if set(filter_words).issubset(vacancy_dict):
                result.append(i)
        return result

    @staticmethod
    def get_vacancies_by_salary(vacancies_list: list, salary_range: list):
        result: list = []
        for i in vacancies_list:
            if i.salary >= int(salary_range[0]) and i.salary <= int(salary_range[1]):
                result.append(i)
        return result

    @staticmethod
    def sort_vacancies(vacancies_list):
        vacancies_list.sort(key=lambda vacancy: vacancy.salary, reverse=True)
        return vacancies_list

    @staticmethod
    def get_top_vacancies(vacancies_list, top_n):
        return vacancies_list[:top_n]

    @staticmethod
    def print_vacancies(vacancies_list):
        print('-----------------------------------------------------------------------------------------')
        for i in vacancies_list:
            print(i)
        print('\n')

    @staticmethod
    def vacancy_to_json(vacancy):
        data = {'id': vacancy.id,
                'name': vacancy.name,
                'description': vacancy.description,
                'requirement': vacancy.requirement,
                'salary': vacancy.salary,
                'url': vacancy.url}
        return data

    @staticmethod
    def in_json(vacancies_list):
        data: list = []
        for i in vacancies_list:
            data.append(Vacancy.vacancy_to_json(i))
        return data
