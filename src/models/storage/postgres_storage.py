from peewee import fn

from src.models.storage.abstract_storage import AbstractStorage
from src.models.song import Song

from typing import List


class PostgresStorage(AbstractStorage):

    @property
    def is_any_song_in_db(self):
        return Song.select().count() != 0 

    def in_voted_users(self, song: Song, voted_user_id: str):
        """ Check if the user is already in the voted users. """
        if voted_user_id in song.voted_users:
            return True
        return False

    def get_all_songs(self):
        """ Get list of all songs. """
        return Song.select().execute()

    def save_songs(self, songs: List[dict]):
        """ Save songs in the db. """
        for song in songs:
            Song.create(
                title=song.get('title'),
                author=song.get('author'),
                link=song.get('link'),
                pos=song.get('pos'),
                mark=song.get('mark'),
                voted_users=song.get('voted_users')
            )

    def sort_songs(self, DESC=True):
        """ Sort songs in the db. """
        if DESC:
            return Song.select().order_by(Song.voted_users.desc()).execute()
        else:
            return Song.select().order_by(Song.voted_users.asc()).execute()

    def get_song_by_id(self, id: int):
        return Song.get_by_id(id)

    def add_vote(self, song: Song, voted_user_id: str):
        """ Add user id in voted users. Also update mark. """
        song.update(
            voted_users=fn.array_append(Song.voted_users, voted_user_id)
        ).where(Song.id_music == song.id_music).execute()
        song.update(
            mark=song.mark + 1
        ).where(Song.id_music == song.id_music).execute()
    
    def remove_vote(self, song: Song, voted_user_id: str):
        """ Remove user id from voted users. Also update mark. """
        song.update(
            voted_users=fn.array_remove(Song.voted_users, voted_user_id)
        ).where(Song.id_music == song.id_music).execute()
        song.update(
            mark=song.mark - 1
        ).where(Song.id_music == song.id_music).execute()

    def nullify_song_votes(self, song: Song):
        """ Clear song voted users and mark. """
        song.update(
            mark=0
        ).where(Song.id_music == song.id_music).execute()
        song.update(
            voted_users=[]
        ).where(Song.id_music == song.id_music).execute()

    def clear(self):
        """ Delete all songs form db. """
        Song.delete().execute()