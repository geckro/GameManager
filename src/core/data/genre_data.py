from src.core.data.common_data import CommonData
from src.core.log import log


class GenreData:
    def __init__(self):
        log('info', 'initializing GenreData')
        self.common_data = CommonData('data/genres.json')

    def append_to_json(self, data):
        log('info', 'initializing func append_to_json in GenreData')
        self.common_data.append_to_data_json(data)

    def get_genres(self):
        log('info', 'initializing func get_platforms in GenreData')
        genres = self.common_data.open_json()
        return genres
