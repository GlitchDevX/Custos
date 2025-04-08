from genericpath import isfile
from ntpath import join
from os import listdir

from flask import json

from app.config_reader import reload_readers_with_namespace


class ConfigSetter:
    """
    A class to manage the setting and updating of configuration files.
    This class checks for existing configuration files and provides methods to update them.
    """

    def __init__(self):
        path = "config/"
        self._existing_files = [f for f in listdir(path) if isfile(join(path, f))]

    def set_file(self, namespace, content):
        if f"{namespace}.json" in self._existing_files:
            
            self.update_file(namespace, content)
            reload_readers_with_namespace(namespace)

            return {"code": "OK"}, 200
        else:
            print(f"Tried to write config to non existent file. Filename: {namespace}.json")
            return {"code": "NAMESPACE_NOT_FOUND", "text": "Config Namespace not found" }, 404 

    def update_file(self, namespace, content):
        path = f"config/{namespace}.json"
        with open(path, "w") as file:
            file.write(json.dumps(content, indent=4))
