import copy
from botbuilder.core import CardFactory
from src.card_builder.blocks import MAIN_BLOCK, SONG_ROW
from src.models.storage.postgres_storage import Song


class AdaptiveCardView:
    """
    Model that represents poll view.
    In MS Teams, poll is created with adaptive cards
    """
    def __init__(self):
        self._cards = []

    @property
    def cards(self):
        return list(map(CardFactory.adaptive_card, self._cards))

    def _append_row(self, card: dict, song: Song):
        row = copy.deepcopy(SONG_ROW)

        song_details = ' '.join([song.title, '---', song.author])

        row['columns'][0]['items'][0]['text'] = song_details
        row['columns'][1]['items'][0]['actions'][0]['data']['song_id'] = song.id_music 

        card['body'].append(row)

    def create_card(self, songs: list):
        card = copy.deepcopy(MAIN_BLOCK)

        # Add song rows
        for song in songs:
            self._append_row(card, song)

        self._cards.append(card)

