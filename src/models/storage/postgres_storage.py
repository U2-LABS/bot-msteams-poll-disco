from src.models.storage.abstract_storage import AbstractStorage

from src.models.song import Song


class PostgresStorage(AbstractStorage):

    def get_all_songs(self):
        return Song.select()