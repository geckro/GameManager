from src.core.data.common_data import CommonData
from src.core.log import log


class PlatformData:
    def __init__(self):
        log('info', 'initializing PlatformData')
        self.common_data = CommonData('data/platforms.json')

    def append_to_json(self, data):
        log('info', 'initializing func append_to_json in PlatformData')
        self.common_data.append_to_data_json(data)

    def get_platforms(self):
        log('info', 'initializing func get_platforms in PlatformData')
        platforms = self.common_data.open_json()
        return platforms
