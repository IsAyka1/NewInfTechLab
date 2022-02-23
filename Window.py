from functools import partial
from tkinter import *
from PlayerModel import *
from main import *
from NewWindow import *
from save import save

frame_top = None


def click_add(f_name, l_name, age, score):
    Player.create(first_name=f_name.get(),
                  last_name=l_name.get(),
                  age=age.get(),
                  max_score=score.get())

    window(Player.select())


def click_delete(id):
    Player.delete_by_id(id)

    quary = ScoreTable.delete().where(ScoreTable.owner == id)
    quary.execute()
    window(Player.select())


def click_filter(value, is_direction_on):
    dict_ = {"first_name": Player.first_name, "last_name": Player.last_name, "age": Player.age,
             "max_score": Player.max_score}
    result = None
    if is_direction_on.get():
        result = Player.select().order_by(dict_[value.get()])
    else:
        result = (Player.select().order_by(dict_[value.get()].desc()))

    window(result)


def save_file(players):
    filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("xlsx files", "*.xlsx"),))
    data = {'id': [], 'first_name': [], 'last_name': [], 'age': [], 'max_score': []}
    for player in players:
        data['id'].append(player.id)
        data['first_name'].append(player.first_name)
        data['last_name'].append(player.last_name)
        data['age'].append(player.age)
        data['max_score'].append(player.max_score)
    save(data, filename)


def create_window(root):
    root.title("Windows-приложение на Python с использованием базы данных")
    global frame_top
    frame_top = LabelFrame(root, text="Результат")
    window(Player.select())
    add_db()
    filter_db()


def window(players):
    for widget in frame_top.winfo_children():
        widget.destroy()
    frame_top.grid(column=0, row=0, columnspan=2, padx=3, sticky=W + E)
    label_id = Label(frame_top, text="id", padx=20, pady=10)
    label_id.grid(column=0, row=0)
    label_f_name = Label(frame_top, text="Имя", padx=20, pady=10)
    label_f_name.grid(column=1, row=0)
    label_l_name = Label(frame_top, text="Фамилия", padx=20, pady=10)
    label_l_name.grid(column=2, row=0)
    label_age = Label(frame_top, text="Возраст", padx=20, pady=10)
    label_age.grid(column=3, row=0)
    label_score = Label(frame_top, text="Очки", padx=20, pady=10)
    label_score.grid(column=4, row=0)

    update_db(players)


def add_db():
    frame_add = LabelFrame(text="Добавление данных")
    frame_add.grid(column=0, row=1, rowspan=2, sticky=N, padx=3)
    label_f_name = Label(frame_add, text="Имя", padx=20, pady=10)
    label_f_name.grid(column=0, row=0)
    label_l_name = Label(frame_add, text="Фамилия", padx=20, pady=10)
    label_l_name.grid(column=0, row=1)
    label_age = Label(frame_add, text="Возраст", padx=20, pady=10)
    label_age.grid(column=0, row=2)
    label_score = Label(frame_add, text="Максимальный результат", padx=20, pady=10)
    label_score.grid(column=0, row=3)

    f_name = StringVar()
    entry_f_name = Entry(frame_add, textvariable=f_name)
    entry_f_name.grid(column=1, row=0)
    l_name = StringVar()
    entry_l_name = Entry(frame_add, textvariable=l_name)
    entry_l_name.grid(column=1, row=1)
    age = IntVar()
    entry_age = Entry(frame_add, textvariable=age)
    entry_age.grid(column=1, row=2)
    max_score = IntVar()
    entry_score = Entry(frame_add, textvariable=max_score)
    entry_score.grid(column=1, row=3)

    btn = Button(frame_add, text="Добавить", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=partial(click_add, f_name, l_name, age, max_score))
    btn.grid(column=1, row=4)


def filter_db():
    frame_filter = LabelFrame(text="Сортировка данных")
    frame_filter.grid(column=1, row=1, sticky=E)
    frame_f = LabelFrame(frame_filter)
    frame_f.grid(column=0, row=0)
    value = IntVar()
    value.set('max_score')
    f_name_check = Radiobutton(frame_f, text="Имя", value="first_name", variable=value, padx=15, pady=10)
    f_name_check.grid(row=0, column=0, sticky=W)
    l_name_check = Radiobutton(frame_f, text="Фамилия", value="last_name", variable=value, padx=15, pady=10)
    l_name_check.grid(row=1, column=0, sticky=W)
    age_check = Radiobutton(frame_f, text="Возраст", value="age", variable=value, padx=15, pady=10)
    age_check.grid(row=2, column=0, sticky=W)
    score_check = Radiobutton(frame_f, text="Максимальный результат", value="max_score", variable=value, padx=15,
                              pady=10)
    score_check.grid(row=3, column=0, sticky=W)

    frame_n = LabelFrame(frame_filter)
    frame_n.grid(column=0, row=1)
    is_direction_on = BooleanVar()
    direction_on_chek = Radiobutton(frame_n, text="По-возрастанию", value=True, variable=is_direction_on, padx=15,
                                    pady=10)
    direction_on_chek.grid(row=1, column=0)
    direction_off_chek = Radiobutton(frame_n, text="По-убыванию", value=False, variable=is_direction_on, padx=15,
                                     pady=10)
    direction_off_chek.grid(row=2, column=0)

    btn = Button(frame_filter, text="Сортировка", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=partial(click_filter, value, is_direction_on))
    btn.grid(column=0, row=2)


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
        btn_delete = Button(frame_top, text="Удалить", background="#555", foreground="#ccc",
                            padx="10", pady="4", font="16", command=partial(click_delete, player.id))
        btn_delete.grid(column=5, row=row_count)
        btn_change = Button(frame_top, text="Обновить", background="#555", foreground="#ccc",
                            padx="10", pady="4", font="16", command=partial(click_change, player.id))
        btn_change.grid(column=6, row=row_count)
        row_count += 1
    btn_save = Button(frame_top, text="Сохранить в excel", background="#555", foreground="#ccc",
                      padx="10", pady="4", font="16", command=lambda: save_file(players.select()))
    btn_save.grid(column=5, columnspan=2, row=0)


def click_save_changes(id, f_name, l_name, age, max_score, this_window):
    quary = Player.update({Player.first_name: f_name.get(), Player.last_name: l_name.get(), Player.age: age.get(),
                           Player.max_score: max_score.get()}).where(Player.id == id)
    quary.execute()
    this_window.destroy()
    window(Player.select())


def click_change(id):
    window = Toplevel()
    window.geometry("400x400")
    window.title("Изменить запись")

    item = Player.get_by_id(id)

    label_f_name = Label(window, text="Имя", padx=20, pady=10)
    label_f_name.grid(column=0, row=0)
    label_l_name = Label(window, text="Фамилия", padx=20, pady=10)
    label_l_name.grid(column=0, row=1)
    label_age = Label(window, text="Возраст", padx=20, pady=10)
    label_age.grid(column=0, row=2)
    label_score = Label(window, text="Максимальный результат", padx=20, pady=10)
    label_score.grid(column=0, row=3)

    f_name = StringVar()
    f_name.set(item.first_name)
    entry_f_name = Entry(window, textvariable=f_name)
    entry_f_name.grid(column=1, row=0)
    l_name = StringVar()
    l_name.set(item.last_name)
    entry_l_name = Entry(window, textvariable=l_name)
    entry_l_name.grid(column=1, row=1)
    age = StringVar()
    age.set(item.age)
    entry_age = Entry(window, textvariable=age)
    entry_age.grid(column=1, row=2)
    max_score = StringVar()
    max_score.set(item.max_score)
    entry_score = Entry(window, textvariable=max_score)
    entry_score.grid(column=1, row=3)

    btn = Button(window, text="Сохранить", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16",
                 command=partial(click_save_changes, item.id, f_name, l_name, age, max_score, window))
    btn.grid(column=1, row=4)
