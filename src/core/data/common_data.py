import json
import pathlib

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

    def delete_entry(self, data):
        with open(self.data_file_path, 'r') as data_file:
            json_raw = json.load(data_file)

        json_data_new = []

        for x in json_raw:
            if data[0] not in x['title'] or data[2] not in x['platforms']:
                json_data_new.append(x)

        if json_data_new:
            with open(self.data_file_path, 'w') as data_file:
                json.dump(json_data_new, data_file)
