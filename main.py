from Window import *
from ScoreModel import *


if __name__ == '__main__':
    db.create_tables([Player, ScoreTable])
    root = Tk()
    create_window(root)

    btn_new_window = Button(text="Another table", background="#555", foreground="#ccc",
                            padx="20", pady="8", font="16", command=new_window)
    btn_new_window.pack(side=BOTTOM, padx=30, pady=20)

    root.mainloop()
