import json


class EmployeeModel:
    def __init__(self, file_path):
        self.employees_data = self.read_json(file_path)

    def read_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
