import json
from typing import List

class ConfigReader:
    """
    A class to read and manage configuration settings from a JSON file.

    Attributes:
        namespace (str): The namespace used to identify the configuration file.
        config (dict): The configuration settings loaded from the JSON file.

    :param namespace (str): The namespace used to locate the configuration file.
    """

    def __init__(self, namespace):
        self.namespace = namespace
        self.read_conf_file()
        instances.append(self)

    def read_conf_file(self):
        try:
            with open(f"config/{self.namespace}.json") as file:
                self.config = json.loads(file.read())
        except:
            self.config = None

    def get_all(self):
        return self.config

    def get(self, name):
        return self.config[name]

instances: List[ConfigReader] = []

def reload_readers_with_namespace(namespace):
    for instance in instances:
        if instance.namespace == namespace:
            instance.read_conf_file()