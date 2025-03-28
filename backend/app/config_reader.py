import json


class ConfigReader:

    def __init__(self, file):
        with open(f"config/{file}.json") as file:
            self.config = json.loads(file.read())

    def get(self, name):
        return self.config[name]
