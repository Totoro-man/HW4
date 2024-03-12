class Interface:

    @staticmethod
    def introduce() -> int:
        print('-------------------------------------------------------------------------\n'
              'Добро пожаловать в центр достижения мечты, где каждый получает что хочет!\n'
              'Мы предлагаем Вам пройти небольшое анкетирование по результатам которого\n'
              'Вы сможете рассмотреть ряд лучших вакансий которые подойдут Вам наилучшим\n'
              'образом и раскроют весь Ваш потенциал. Взамен просим пустяк - Вашу душу.\n'
              '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n'
              'Если Вы согласны - введите 1. Необходимо время подумать - введите 0.')
        step = int(input())
        return step

    @staticmethod
    def user_info() -> dict:
        """
        :return: {'name': str, 'f_name': str, 'age': int}
        """
        result = {}
        print('-------------------------------------------------------------------------\n'
              'Вам необходимо будет ответить на ряд вопросов. И так первые три:')
        name = input('Введите Ваше имя: ')
        result.update({'name': name})
        f_name = input('Введите Вашу фамилию: ')
        result.update({'f_name': f_name})
        age = input('Введите Ваш возраст: ')
        result.update({'age': age})
        print('-------------------------------------------------------------------------\n')
        return result

    @staticmethod
    def user_region() -> str:
        """
        :return: {'region': str}
        """
        region = input('Введите город для поиска: ')
        print('-------------------------------------------------------------------------\n')
        return region

    def user_request(self) -> dict:
        """
        :return: {'keywords': str, 'min_salary': int, 'schedule': list, 'employment': list}
        """
        keywords = input('Введите слова связанные с искомой профессией (вводите слова через пробел):\n')
        vacancies_amount = input('Введите кол-во получаемых вакансий (макс = 100):\n')
        print(int(vacancies_amount))
        if not int(vacancies_amount) in range(0, 100):
            vacancies_amount = '100'
        keywords_list = keywords.split(' ')
        keywords = ",".join(keywords_list)
        return {'keywords': keywords, 'vacancies_amount': vacancies_amount}

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
        print(error_str)
        pass

    def show_vacancy_menu(self) -> int:
        print('-------------------------------------------------------------------------\n'
              ' 1 - Показать вакансии | 2 - Сохраненные вакансии | 3 - Выход')

    @staticmethod
    def chose_region(regions: list) -> int:
        print('Необходимо уточнение, выберите из списка:')
        i = 1
        for region in regions:
            print(f'{i} - {region["text"]}')
            i += 1
        print('0 - Ввести название заново')
        selected = int(input())
        if selected == 0 or selected > len(regions):
            print('-------------------------------------------------------------------------\n')
            return 0
        result = regions[selected - 1]
        print(f'Выбран вариант - {result["text"]}')
        print('-------------------------------------------------------------------------\n')
        return result
