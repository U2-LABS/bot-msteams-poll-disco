from abc import abstractmethod, ABC


class AbstractStorage(ABC):
    
    @property
    def is_any_song_in_db(self):
        pass

    @abstractmethod
    def save_songs(self):
        pass

    @abstractmethod
    def get_all_songs(self):
        pass