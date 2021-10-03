from functools import partial

from ScoreModel import ScoreTable
from Window import *
from tkinter import *


frame_top = 0
def new_window():
    window = Toplevel()
    window.geometry("500x500")
    window.title("Дочерняя таблица")
    global frame_top
    frame_top = LabelFrame(window, text="База данных")
    update(ScoreTable.select().get())

def update(list):
    for widget in frame_top.winfo_children():
        widget.destroy()
    frame_top.pack(side=TOP, padx=50, pady=20)

    label_id = Label(frame_top, text="id", padx=20, pady=10)
    label_id.grid(column=0, row=0)
    label_owner_id = Label(frame_top, text="owner id", padx=20, pady=10)
    label_owner_id.grid(column=1, row=0)
    label_score = Label(frame_top, text="score", padx=20, pady=10)
    label_score.grid(column=4, row=0)

    row_count = 1
    for item in list:

        label_id = Label(frame_top, text=item.id, padx=20, pady=10)
        label_id.grid(column=0, row=row_count)
        label_owner_id = Label(frame_top, text=item.owner, padx=20, pady=10)
        label_owner_id.grid(column=1, row=row_count)
        label_score = Label(frame_top, text=item.score, padx=20, pady=10)
        label_score.grid(column=2, row=row_count)
        btn = Button(frame_top, text="Delete", background="#555", foreground="#ccc",
                     padx="10", pady="4", font="16", command=partial(click_delete, item.id))
        btn.grid(column=3, row=row_count)
        row_count += 1

def click_delete(id):
    Score.delete_by_id(id)

    update(Score.select().get())