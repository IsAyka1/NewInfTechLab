from Window import *
from ScoreModel import *

if __name__ == '__main__':
    db.create_tables([Player, ScoreTable])
    root = Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 300
    h = h - 300
    root.geometry('650x460+{}+{}'.format(w, h))
    root.resizable(width=False, height=False)
    create_window(root)

    btn_new_window = Button(text="Перейти к другой таблице", background="#555", foreground="#ccc",
                            padx="20", pady="8", font="16", command=new_window)
    btn_new_window.grid(column=0, row=1, sticky=S)

    root.mainloop()
