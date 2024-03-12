from abc import ABC, abstractmethod


class JobsAPI(ABC):
    @abstractmethod
    def set_param(self):
        pass

    @abstractmethod
    def get_region_id(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def make_request(self):
        pass
