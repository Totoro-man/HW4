class User:

    def __init__(self):
        self.info = {'name': '', 'f_name': '', 'age': 0}
        self.region_to_check: str = ''
        self.regions_list: list = []
        self.region: dict = {}
        self.vacancies: list = []
        self.chosen_vacancy_id: int = 0
        self.saved_vacancies: list = []
