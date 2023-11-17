import json
import pathlib
import os

from src.core.log import log


class CommonData:
    def __init__(self, path=None):
        self.data_file_path = pathlib.Path(path) if path else None
        self.data_file_path.parent.mkdir(parents=True, exist_ok=True)

    def open_json(self):
        if self.data_file_path and self.data_file_path.exists():
            with open(self.data_file_path, 'r') as file:
                json_data = json.load(file)
        else:
            json_data = []

        return json_data

    def append_to_data_json(self, data):
        if not self.data_file_path:
            log('error', 'No file path for JSON data')

        json_data = self.open_json()
        json_data.append(data)

        with open(self.data_file_path, 'w') as data_file:
            json.dump(json_data, data_file)
