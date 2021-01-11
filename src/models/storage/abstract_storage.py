from abc import abstractmethod, ABC


class AbstractStorage(ABC):
    
    @property
    def is_any_song_in_db(self):
        pass

    @abstractmethod
    def in_voted_users(self, song, voted_user_id):
        pass

    @abstractmethod
    def get_all_songs(self):
        pass

    @abstractmethod
    def save_songs(self, songs):
        pass

    @abstractmethod
    def sort_songs(self, DESC):
        pass

    @abstractmethod
    def get_song_by_id(self, id):
        pass

    @abstractmethod
    def add_vote(self, song, voted_user_id):
        pass

    @abstractmethod
    def remove_vote(self, song, voted_user_id):
        pass

    @abstractmethod
    def nullify_song_votes(self, song):
        pass

    @abstractmethod
    def clear(self):
        pass