from src.core.data.common_data import CommonData
from src.core.log import log


class EngineData:
    def __init__(self):
        log('info', 'initializing EngineData')
        self.common_data = CommonData('data/engines.json')

    def append_to_json(self, data):
        log('info', 'initializing func append_to_json in EngineData')
        self.common_data.append_to_data_json(data)

    def get_engines(self):
        log('info', 'initializing func get_engines in EngineData')
        engines = self.common_data.open_json()
        return engines
