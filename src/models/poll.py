from botbuilder.schema import Activity

from src.card_builder.view import AdaptiveCardView
from src.models.storage.postgres_storage import PostgresStorage


class Poll:
    """ Model that represents the controller between db logic and chat view """
    def __init__(self):
        self._activity = None  # Chat msg representation (For MS Teams it is called activity)
        self.storage = PostgresStorage()  # General Storage
        self.view = AdaptiveCardView()  # MS Teams representation

        self.isStarted = False

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, value):
        if isinstance(value, Activity):
            self._activity = value
        else:
            raise TypeError("Should be Activity obj")

    def start(self):
        """
        Create representation and start poll.
        """
        songs = self.storage.get_all_songs()

        self.view.create_card(songs)
        self.isStarted = True