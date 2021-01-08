from peewee import fn

from src.models.storage.abstract_storage import AbstractStorage
from src.models.song import Song

from typing import List


class PostgresStorage(AbstractStorage):

    def in_voted_users(self, song: Song, voted_user_id: str):
        if voted_user_id in song.voted_users:
            return True
        return False

    def get_all_songs(self):
        return Song.select()

    def save_songs(self, songs: List[dict]):
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
        if DESC:
            return Song.select().order_by(Song.voted_users.desc()).execute()
        else:
            return Song.select().order_by(Song.voted_users.asc()).execute()

    def get_song_by_id(self, id: int):
        return Song.get_by_id(id)

    def add_vote(self, song: Song, voted_user_id: str):
        song.update(
            voted_users=fn.array_append(Song.voted_users, voted_user_id)
        ).where(Song.id_music == song.id_music).execute()
        song.update(
            mark=song.mark + 1
        ).where(Song.id_music == song.id_music).execute()
    
    def remove_vote(self, song: Song, voted_user_id: str):
        song.update(
            voted_users=fn.array_remove(Song.voted_users, voted_user_id)
        ).where(Song.id_music == song.id_music).execute()
        song.update(
            mark=song.mark - 1
        ).where(Song.id_music == song.id_music).execute()
                
    def clear(self):
        Song.truncate_table(restart_identity=True)
        
    @property
    def is_any_song_in_db(self):
        return Song.select().count() != 0 