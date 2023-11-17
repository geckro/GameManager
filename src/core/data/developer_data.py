from src.core.data.common_data import CommonData
from src.core.log import log


class DeveloperData:
    def __init__(self):
        log('info', 'initializing DeveloperData')
        self.common_data = CommonData('data/developers.json')

    def append_to_json(self, data):
        log('info', 'initializing func append_to_json in DeveloperData')
        self.common_data.append_to_data_json(data)

    def get_developers(self):
        log('info', 'initializing func get_platforms in DeveloperData')
        developers = self.common_data.open_json()
        return developers
