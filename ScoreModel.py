from peewee import *
from PlayerModel import *


class ScoreTable(BaseModel):
    id = AutoField(primary_key=True)
    owner = ForeignKeyField(Player)
    score = IntegerField()
