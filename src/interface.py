class Interface:

    @staticmethod
    def introduce() -> int:
        print('-------------------------------------------------------------------------\n'
              'Добро пожаловать в центр достижения мечты, где каждый получает что хочет!\n'
              'Мы предлагаем Вам пройти небольшое анкетирование по результатам которого\n'
              'Вы сможете рассмотреть ряд лучших вакансий которые подойдут Вам наилучшим\n'
              'образом и раскроют весь Ваш потенциал. Взамен просим пустяк - Вашу душу.\n'
              '-------------------------------------------------------------------------\n'
              'Если Вы согласны - введите 1. Необходимо время подумать - введите 0.')
        step = int(input())
        if step == 1: step = 2
        return step

    @staticmethod
    def user_info(info: dict) -> dict:
        """
        :return: {'name': str, 'fname': str, 'age': int}
        """
        result = {}
        print('-------------------------------------------------------------------------\n'
              'Вам необходимо будет ответить на ряд вопросов. И так первые три:')
        name = input('Введите Ваше имя: ')
        result.update({'name': name})
        fname = input('Введите Вашу фамилию: ')
        result.update({'fname': fname})
        age = input('Введите Ваш возраст: ')
        result.update({'age': age})
        print('-------------------------------------------------------------------------\n')
        return result

    @staticmethod
    def user_region() -> str:
        """
        :return: {'region': str}
        """
        return 'Москва'

    def user_request(self) -> dict:
        """
        :return: {'profession': list, 'min_salary': int, 'schedule': list, 'employment': list}
        """
        pass

    def short_vacancies(self, vacancies):
        """

        :return: 'step': int
        """
        pass

    def vacancy(self):
        """

        :return: 'step': int
        """
        pass

    def print_error(self, error_str: str):
        """

        :return: 'step': int
        """
        pass

    def show_vacancy_menu(self) -> int:
        pass
