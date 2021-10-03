from peewee import *

db = SqliteDatabase("mydatabase1.db")

class BaseModel(Model):
    class Meta:
        database = db