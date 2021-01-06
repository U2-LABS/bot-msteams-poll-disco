import os

from peewee import TextField, IntegerField, Model
from playhouse.postgres_ext import PostgresqlExtDatabase, ArrayField

from dotenv import load_dotenv


load_dotenv()

conn = PostgresqlExtDatabase(
    database=os.getenv("NAME_DB"),
    user=os.getenv("USER_DB", 'postgres'),
    password=os.getenv("PASSWORD_DB", 'postgres'),
    host=os.getenv("HOST_DB", 'localhost'),
    port=os.getenv("PORT_DB", 5432)
)

class BaseModel(Model):
    """ ORM peewee model for postgresql """
    class Meta:
        database = conn


class Song(BaseModel):
    """ DB model that represent song in a poll """
    title = TextField(column_name='title')
    pos = IntegerField(column_name='pos')
    link = TextField(column_name='link')
    id_music = IntegerField(column_name="id_music", primary_key=True)
    author = TextField(column_name='author')
    voted_users = ArrayField(TextField, column_name="voted_users")
    mark = IntegerField(column_name="mark")

    class Meta:
        table_name = 'music'