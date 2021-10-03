from functools import partial
from tkinter import *
from PlayerModel import *
from main import *
from NewWindow import *

frame_top = 0

def click_add(f_name, l_name, age, score):
    Player.create(first_name=f_name.get(),
                  last_name=l_name.get(),
                  age=age.get(),
                  max_score=score.get())

    window(Player.select().get())


def click_delete(id):
    Player.delete_by_id(id)

    window(Player.select().get())


def click_filter(value, is_direction_on=True):
    dict_ = {"first_name": Player.first_name, "last_name": Player.last_name, "age": Player.age,
             "max_score": Player.max_score}
    result = None
    if not is_direction_on:
        result = Player.select().order_by(dict_[value.get()])
    else:
        result = (Player.select().order_by(dict_[value.get()].desc()))

    window(result)


def create_window(root):
    root.title("Windows-приложение на Python с использованием базы данных")
    root.geometry("600x600")
    global frame_top
    frame_top = LabelFrame(root, text="База данных")
    window(Player.select().get())
    add_db()
    filter_db()


def window(players):
    for widget in frame_top.winfo_children():
        widget.destroy()
    frame_top.pack(side=TOP, padx=50, pady=20)
    label_id = Label(frame_top, text="id", padx=20, pady=10)
    label_id.grid(column=0, row=0)
    label_f_name = Label(frame_top, text="first name", padx=20, pady=10)
    label_f_name.grid(column=1, row=0)
    label_l_name = Label(frame_top, text="last name", padx=20, pady=10)
    label_l_name.grid(column=2, row=0)
    label_age = Label(frame_top, text="age", padx=20, pady=10)
    label_age.grid(column=3, row=0)
    label_score = Label(frame_top, text="score", padx=20, pady=10)
    label_score.grid(column=4, row=0)

    btn_new_window = Button(text="Another table", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=new_window)
    btn_new_window.pack()

    update_db(players)



def add_db():
    frame_add = LabelFrame(text="Добавление данных")
    frame_add.pack(side=LEFT, padx=50, pady=20)
    label_f_name = Label(frame_add, text="first name", padx=20, pady=10)
    label_f_name.grid(column=0, row=0)
    label_l_name = Label(frame_add, text="last name", padx=20, pady=10)
    label_l_name.grid(column=0, row=1)
    label_age = Label(frame_add, text="age", padx=20, pady=10)
    label_age.grid(column=0, row=2)
    label_score = Label(frame_add, text="max score", padx=20, pady=10)
    label_score.grid(column=0, row=3)

    f_name = StringVar()
    entry_f_name = Entry(frame_add, textvariable=f_name)
    entry_f_name.grid(column=1, row=0)
    l_name = StringVar()
    entry_l_name = Entry(frame_add, textvariable=l_name)
    entry_l_name.grid(column=1, row=1)
    age = StringVar()
    entry_age = Entry(frame_add, textvariable=age)
    entry_age.grid(column=1, row=2)
    max_score = StringVar()
    entry_score = Entry(frame_add, textvariable=max_score)
    entry_score.grid(column=1, row=3)

    btn = Button(frame_add, text="Add", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=partial(click_add, f_name, l_name, age, max_score))
    btn.grid(column=1, row=4)


def filter_db():
    frame_filter = LabelFrame(text="Фильтрация данных")
    frame_filter.pack(side=RIGHT, padx=50, pady=20)
    frame_f = LabelFrame(frame_filter)
    frame_f.pack(side=TOP)
    value = StringVar()
    f_name_check = Radiobutton(frame_f, text="first name", value="first_name", variable=value, padx=15, pady=10)
    f_name_check.grid(row=0, column=0, sticky=W)
    l_name_check = Radiobutton(frame_f, text="last name", value="last_name", variable=value, padx=15, pady=10)
    l_name_check.grid(row=1, column=0, sticky=W)
    age_check = Radiobutton(frame_f, text="age", value="age", variable=value, padx=15, pady=10)
    age_check.grid(row=2, column=0, sticky=W)
    score_check = Radiobutton(frame_f, text="max score", value="max_score", variable=value, padx=15, pady=10)
    score_check.grid(row=3, column=0, sticky=W)

    frame_n = LabelFrame(frame_filter)
    frame_n.pack()
    is_direction_on = BooleanVar()
    direction_on_chek = Radiobutton(frame_n, text="По-возрастанию", value=True, variable=is_direction_on, padx=15, pady=10)
    direction_on_chek.grid(row=1, column=0)
    direction_off_chek = Radiobutton(frame_n, text="По-возрастанию", value=False, variable=is_direction_on, padx=15,
                                    pady=10)
    direction_off_chek.grid(row=2, column=0)

    btn = Button(frame_filter, text="Filter", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=partial(click_filter, value))
    btn.pack(side=BOTTOM)


def update_db(players):
    row_count = 1

    for player in players.select():
        label_id = Label(frame_top, text=player.id, padx=20, pady=10)
        label_id.grid(column=0, row=row_count)
        label_f_name = Label(frame_top, text=player.first_name, padx=20, pady=10)
        label_f_name.grid(column=1, row=row_count)
        label_l_name = Label(frame_top, text=player.last_name, padx=20, pady=10)
        label_l_name.grid(column=2, row=row_count)
        label_age = Label(frame_top, text=player.age, padx=20, pady=10)
        label_age.grid(column=3, row=row_count)
        label_score = Label(frame_top, text=player.max_score, padx=20, pady=10)
        label_score.grid(column=4, row=row_count)
        btn = Button(frame_top, text="Delete", background="#555", foreground="#ccc",
                     padx="10", pady="4", font="16", command=partial(click_delete, player.id))
        btn.grid(column=5, row=row_count)
        row_count += 1
