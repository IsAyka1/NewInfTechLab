from Window import *
from ScoreModel import *



if __name__ == '__main__':
    if not db.connect():
        db.create_tables([Player, ScoreTable])
    # print(db.execute(Player.select()).fetchall())
    root = Tk()
    create_window(root)

    root.mainloop()
