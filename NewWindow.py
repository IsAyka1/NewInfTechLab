from functools import partial
from tkinter import messagebox

from ScoreModel import ScoreTable
from Window import *
from tkinter import *


frame_top = 0
this_window = 0
def new_window():
    global this_window
    this_window = Toplevel()
    this_window.geometry("500x500")
    this_window.title("Дочерняя таблица")
    global frame_top
    frame_top = LabelFrame(this_window, text="База данных")
    update(ScoreTable.select())
    add_item()
    filter_item()


def update(list):
    for widget in frame_top.winfo_children():
        widget.destroy()
    frame_top.pack(side=TOP, padx=50, pady=20)

    label_id = Label(frame_top, text="id", padx=20, pady=10)
    label_id.grid(column=0, row=0)
    label_owner_id = Label(frame_top, text="owner id", padx=20, pady=10)
    label_owner_id.grid(column=1, row=0)
    label_score = Label(frame_top, text="score", padx=20, pady=10)
    label_score.grid(column=2, row=0)


    row_count = 1
    for item in list:
        label_id = Label(frame_top, text=item.id, padx=20, pady=10)
        label_id.grid(column=0, row=row_count)
        label_owner_id = Label(frame_top, text=item.owner, padx=20, pady=10)
        label_owner_id.grid(column=1, row=row_count)
        label_score = Label(frame_top, text=item.score, padx=20, pady=10)
        label_score.grid(column=2, row=row_count)
        btn_delete = Button(frame_top, text="Delete", background="#555", foreground="#ccc",
                     padx="10", pady="4", font="16", command=partial(click_delete, item.id))
        btn_delete.grid(column=3, row=row_count)

        btn_change = Button(frame_top, text="Change", background="#555", foreground="#ccc",
                     padx="10", pady="4", font="16", command=partial(click_change, item.id))
        btn_change.grid(column=4, row=row_count)
        row_count += 1


def click_delete(id):
    ScoreTable.delete_by_id(id)

    update(ScoreTable.select())

def add_item():
    frame_add = LabelFrame(this_window, text="Добавление данных")
    frame_add.pack(side=LEFT, padx=50, pady=20)
    label_f_name = Label(frame_add, text="owner id", padx=20, pady=10)
    label_f_name.grid(column=0, row=0)
    label_score = Label(frame_add, text="score", padx=20, pady=10)
    label_score.grid(column=0, row=1)

    owner_id = StringVar()
    entry_f_name = Entry(frame_add, textvariable=owner_id)
    entry_f_name.grid(column=1, row=0)
    score = StringVar()
    entry_score = Entry(frame_add, textvariable=score)
    entry_score.grid(column=1, row=1)

    btn = Button(frame_add, text="Add", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=partial(click_add, owner_id, score))
    btn.grid(column=1, row=2)

def click_add(owner, score):
    tmp = Player.select().where(Player.id == owner.get())
    value = tmp.execute()

    if value:
        ScoreTable.create(owner=owner.get(), score=score.get())
    else:
        messagebox.showinfo("Неправильное значение", "Такого id не существует")
    update(ScoreTable.select())


def click_save_changes(id, owner, score, window):
    tmp = Player.select().where(Player.id == owner.get())
    value = tmp.execute()

    if value:
        quary = ScoreTable.update({ScoreTable.owner: owner.get(), ScoreTable.score: score.get()}).where(
            ScoreTable.id == id)
        quary.execute()
        window.destroy()
        update(ScoreTable.select())
    else:
        messagebox.showinfo("Неправильное значение", "Такого id не существует")



def click_change(id):
    window = Toplevel()
    window.geometry("400x400")
    window.title("Изменить запись")

    item = ScoreTable.get_by_id(id)

    label_owner_id = Label(window, text="owner id", padx=20, pady=10)
    label_owner_id.grid(column=1, row=1)
    label_score = Label(window, text="score", padx=20, pady=10)
    label_score.grid(column=2, row=1)

    owner_id = IntVar()
    owner_id.set(item.owner)
    entry_owner_id = Entry(window, textvariable=owner_id)
    entry_owner_id.grid(column=1, row=2)
    score = IntVar()
    score.set(item.score)
    entry_score = Entry(window, textvariable=score)
    entry_score.grid(column=2, row=2)

    btn = Button(window, text="Save", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=partial(click_save_changes, item.id, owner_id, score, window))
    btn.grid(column=1, row=4)

def click_filter(value, is_direction_on):
    dict_ = {"owner": ScoreTable.owner, "score": ScoreTable.score}
    result = None
    if is_direction_on.get():
        result = ScoreTable.select().order_by(dict_[value.get()])
    else:
        result = (ScoreTable.select().order_by(dict_[value.get()].desc()))

    update(result)

def filter_item():
    frame_filter = LabelFrame(this_window, text="Фильтрация данных")
    frame_filter.pack(side=RIGHT, padx=50, pady=20)
    frame_f = LabelFrame(frame_filter)
    frame_f.pack(side=TOP)
    value = StringVar()
    value.set('score')
    owner_id_check = Radiobutton(frame_f, text="owner id", value="owner", variable=value, padx=15, pady=10)
    owner_id_check.grid(row=1, column=0, sticky=W)
    score_check = Radiobutton(frame_f, text="score", value="score", variable=value, padx=15, pady=10)
    score_check.grid(row=2, column=0, sticky=W)

    frame_n = LabelFrame(frame_filter)
    frame_n.pack()
    is_direction_on = BooleanVar()
    direction_on_chek = Radiobutton(frame_n, text="По-возрастанию", value=True, variable=is_direction_on, padx=15, pady=10)
    direction_on_chek.grid(row=1, column=0)
    direction_off_chek = Radiobutton(frame_n, text="По-убыванию", value=False, variable=is_direction_on, padx=15,
                                    pady=10)
    direction_off_chek.grid(row=2, column=0)

    btn = Button(frame_filter, text="Filter", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=partial(click_filter, value, is_direction_on))
    btn.pack(side=BOTTOM)

