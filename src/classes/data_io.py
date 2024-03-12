import json
from abc import ABC, abstractmethod
import os

class Data_IO(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def append_string(self):
        pass

    @abstractmethod
    def delete_string(self):
        pass

    @abstractmethod
    def update_string(self):
        pass

    @abstractmethod
    def print(self):
        pass

class Json_IO(Data_IO):

    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        if os.path.isfile(f'data/{self.file_name}.json'):
            f = open(f'data/{self.file_name}.json')
            return json.load(f)

    def write(self, data: list):
        with open(f'data/{self.file_name}.json', "w") as outfile:
            json.dump(data, outfile, indent=4)

    def append_string(self, data_string: dict):
        data = self.read()
        data.append(data_string)
        self.write(data)
    def delete_string(self, data_string: dict):
        data = self.read()
        for i, string in enumerate(data):
            if string['id'] == data_string['id']:
                del data[i]
        self.write(data)

    def update_string(self, data_string: dict):
        data = self.read()
        for i, string in enumerate(data):
            if string['id'] == data_string['id']:
                data[i] = data_string
        self.write(data)

    def print(self):
        data = self.read()
        print('-----------------------------------------------------------------------------------------')
        for i in data:
            print(i)

