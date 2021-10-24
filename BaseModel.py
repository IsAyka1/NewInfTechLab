from peewee import *
from playhouse.migrate import *

db = SqliteDatabase("mydatabase.db")
migrator = SqliteMigrator(db)

# migrate(
#         migrator.add_column('player', 'test', CharField(default='', null=True))
#     )
migrate(
        migrator.drop_column('player', 'test', CharField(default='', null=True))
    )

class BaseModel(Model):
    class Meta:
        database = db
