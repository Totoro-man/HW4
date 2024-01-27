class UserRequest:

    def check_region(self, region_to_check: str) -> (bool, str):
        pass

    def get_vacancies(self, request: dict) -> (bool, list | str):
        pass
