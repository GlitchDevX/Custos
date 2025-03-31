import json
from typing import List

class ConfigReader:

    def __init__(self, namespace):
        self.namespace = namespace
        self.read_conf_file()
        instances.append(self)

    def read_conf_file(self):
        with open(f"config/{self.namespace}.json") as file:
            self.config = json.loads(file.read())

    def get(self, name):
        return self.config[name]

instances: List[ConfigReader] = []

def reload_readers_with_namespace(namespace):
    for instance in instances:
        if instance.namespace == namespace:
            instance.read_conf_file()