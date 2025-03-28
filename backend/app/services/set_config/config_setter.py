from genericpath import isfile
from ntpath import join
from os import listdir

from flask import json


class ConfigSetter:

    def __init__(self):
        path = "config/"
        self._existing_files = [f for f in listdir(path) if isfile(join(path, f))]

    def set_file(self, filename, content):
        if f"{filename}.json" in self._existing_files:
            path = f"config/{filename}.json"
            with open(path, "w") as file:
                file.write(json.dumps(content, indent=4))
            return {"code": "OK"}, 200
        else:
            print("Tried to write config to non existent file")
            return {"code": "NOT_FOUND", "text": "Config file not found" }, 404 

