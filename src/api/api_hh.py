from src.api.api_abc import JobsAPI
import requests


class HhAPI(JobsAPI):

    def __init__(self):
        """
        Используемые параметры:
        region_name - хотя бы 3 буквы
        region_id - получаем из справочников по API
        keywords - должно приходить организованной строкой, слова разделены запятой
        vacancies_amount - не должно превышать 100
        """
        self.params: dict = {}

    def set_param(self, param: dict):

        self.params.update(param)

    def get_region_id(self) -> (bool, list | str):

        command = 'suggests/areas/'
        params = {'text':self.params.get('region_name')}
        result = self.make_request(command, params)
        answer = result.json()

        if result.status_code != 200:
            return False, answer['errors']

        if len(answer['items']) == 0:
            return False, 'Ничего не найдено\n'

        if result.status_code == 200:
            return True, answer['items']

    def get_vacancies(self):

        command = 'vacancies/'
        params = {'page': 0,
                  'only_with_salary': True,
                  'area': self.params.get('region_id'),
                  'text': self.params.get('keywords'),
                  'per_page': self.params.get('vacancies_amount')}
        result = self.make_request(command, params)
        answer = result.json()

        if result.status_code != 200:
            return False, answer['errors']

        if answer['found'] == 0:
            return False, 'Ничего не найдено\n'

        if result.status_code == 200:
            return True, answer['items']

    def make_request(self, command:str, params: dict) -> object:

        result = requests.get(f'https://api.hh.ru/{command}', params=params)
        return result
