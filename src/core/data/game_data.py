from src.core.data.common_data import CommonData
from src.core.log import log


class GameData:
    def __init__(self):
        log('info', 'initializing GameData')
        self.common_data = CommonData('data/data.json')

    def get_game_keys(self):
        json_data = self.common_data.open_json()
        if json_data:
            first_item = json_data[0]
            keys = list(first_item.keys())
            return keys
        else:
            return None

    def append_to_json(self, data):
        log('info', 'initializing func append_to_json in GameData')
        self.common_data.append_to_data_json(data)
