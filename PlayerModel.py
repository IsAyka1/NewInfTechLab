from peewee import *
from BaseModel import *


class Player(BaseModel):
    id = AutoField(primary_key=True)
    first_name = TextField()
    last_name = TextField()
    age = IntegerField()
    max_score = IntegerField()
