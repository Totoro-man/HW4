class User:

    def __init__(self):
        self.info = {'name': '', 'fname': '', 'age': 0}
        self.region_to_check: str = ''
        self.request: dict = {'region': '', 'profession': [], 'min_salary': 0, 'schedule': [], 'employment': []}
        self.vacancies: list = []
        self.chosen_vacancy_id: int = 0
        self.saved_vacancies: list = []
