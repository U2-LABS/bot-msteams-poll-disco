from botbuilder.schema import Activity

from src.utilities.songs_functions import get_songs_form_source

from src.card_builder.view import AdaptiveCardView
from src.models.storage.postgres_storage import PostgresStorage

from src.config import SOURCE_NUMBER_OF_SONGS


class Poll:
    """ Model that represents the controller between db logic and chat view """
    def __init__(self, id, owner_id, isStarted, isSongUploaded):
        self.id = id
        self.owner_id = owner_id  # id of the user that started the poll
        self._activity = None  # Chat msg representation (For MS Teams it is called activity)
        self.storage = PostgresStorage()  # General Storage
        self.view = AdaptiveCardView()  # MS Teams representation

        self.isStarted = isStarted
        self.isSongUploaded = isSongUploaded

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, value):
        if not isinstance(value, Activity):
            raise TypeError("Should be Activity obj")
        self._activity = value
        
    def start(self):
        """
        Create representation and start poll.
        """

        # Check if there are no songs in the db.
        if not self.storage.is_any_song_in_db:
            new_songs = get_songs_form_source(SOURCE_NUMBER_OF_SONGS)
            self.storage.save_songs(new_songs)

        songs = self.storage.get_all_songs()

        self.view.create_card(songs, self.id)
        self.isStarted = True

    def vote_for_song(self, song_id:int, voted_user_id: str):
        """ Handle voting for the song. """
        song = self.storage.get_song_by_id(song_id)

        if self.storage.in_voted_users(song, voted_user_id):
            self.storage.remove_vote(song, voted_user_id)
        else:
            self.storage.add_vote(song, voted_user_id)

    def finish(self):
        """ Finish poll. Get winner song. """
        winner = list(self.storage.sort_songs())[0]

        self.storage.clear()
        self.isStarted = False
        return winner