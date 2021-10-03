from peewee import *
# from BaseModel import *
from PlayerModel import *


class ScoreTable(BaseModel):
    owner = ForeignKeyField(Player, related_name="score")
    score = IntegerField()
