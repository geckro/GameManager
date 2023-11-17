from src.core.data.common_data import CommonData
from src.core.log import log


class PublisherData:
    def __init__(self):
        log('info', 'initializing PublisherData')
        self.common_data = CommonData('data/publishers.json')

    def append_to_json(self, data):
        log('info', 'initializing func append_to_json in PublisherData')
        self.common_data.append_to_data_json(data)

    def get_publishers(self):
        log('info', 'initializing func get_platforms in PublisherData')
        publishers = self.common_data.open_json()
        return publishers
