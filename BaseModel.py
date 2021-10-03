from peewee import *

db = SqliteDatabase("mydatabase.db")


class BaseModel(Model):
    class Meta:
        database = db