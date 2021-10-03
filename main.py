from functools import partial
from sqlite3 import *
from tkinter import *
import os

db = "mydatabase.db"
frame_top = 0

def check_db(filename):
    return os.path.exists(filename)

def window(sql=0):
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

    update_db(sql)

def add_db():
    frame_add = LabelFrame(text="Добавление данных")
    frame_add.pack(side=LEFT, padx=50, pady=20)
    label_f_name = Label(frame_add, text="first name", padx=20, pady=10)
    label_f_name.grid(column=0, row=0)
    label_l_name = Label(frame_add, text="last name", padx=20, pady=10)
    label_l_name.grid(column=0, row=1)
    label_age = Label(frame_add, text="age", padx=20, pady=10)
    label_age.grid(column=0, row=2)
    label_score = Label(frame_add, text="score", padx=20, pady=10)
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
    score = StringVar()
    entry_score = Entry(frame_add, textvariable=score)
    entry_score.grid(column=1, row=3)

    btn = Button(frame_add, text="Add", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=partial(click_add, f_name, l_name, age, score))
    btn.grid(column=1, row=4)

def filter_db():
    frame_filter = LabelFrame(text="Фильтрация данных")
    frame_filter.pack(side=RIGHT, padx=50, pady=20)
    value = StringVar()
    f_name_check = Radiobutton(frame_filter, text="first name", value="first_name", variable=value, padx=15, pady=10)
    f_name_check.grid(row=0, column=0, sticky=W)
    l_name_check = Radiobutton(frame_filter, text="last name", value="last_name", variable=value, padx=15, pady=10)
    l_name_check.grid(row=1, column=0, sticky=W)
    age_check = Radiobutton(frame_filter, text="age", value="age", variable=value, padx=15, pady=10)
    age_check.grid(row=2, column=0, sticky=W)
    score_check = Radiobutton(frame_filter, text="score", value="score", variable=value, padx=15, pady=10)
    score_check.grid(row=3, column=0, sticky=W)

    btn = Button(frame_filter, text="Filter", background="#555", foreground="#ccc",
                 padx="20", pady="8",font="16", command=partial(click_filter, value))
    btn.grid(column=0, row=4)

def update_db(sql):
    conn = connect(db)
    cursor = conn.cursor()
    row_count = 1
    if sql == 0:
        sql = """
            SELECT * FROM game
            """
    list = cursor.execute(sql).fetchall()
    for i in list:
        label_id = Label(frame_top, text=i[0], padx=20, pady=10)
        label_id.grid(column=0, row=row_count)
        label_f_name = Label(frame_top, text=i[1], padx=20, pady=10)
        label_f_name.grid(column=1, row=row_count)
        label_l_name = Label(frame_top, text=i[2], padx=20, pady=10)
        label_l_name.grid(column=2, row=row_count)
        label_age = Label(frame_top, text=i[3], padx=20, pady=10)
        label_age.grid(column=3, row=row_count)
        label_score = Label(frame_top, text=i[4], padx=20, pady=10)
        label_score.grid(column=4, row=row_count)
        btn = Button(frame_top, text="Delete", background="#555", foreground="#ccc",
                     padx="10", pady="4", font="16", command=partial(click_delete, i[0]))
        btn.grid(column=5, row=row_count)
        row_count += 1

def create_db():
    if check_db(db):
        return
    conn = connect(db)
    cursor = conn.cursor()

    sql = """
    CREATE TABLE game(
    id integer primary key autoincrement not null,
    first_name text,
    last_name text,
    age int,
    score long uint
);
    """
    cursor.execute(sql)
    conn.commit()

def click_add(f_name, l_name, age, score):
    if check_db(db):
        conn = connect(db)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO game(first_name, last_name, age, score) VALUES(?, ?, ?, ?)", (f_name.get(), l_name.get(), age.get(), score.get()))
        conn.commit()
        window()

def click_delete(value):
    if check_db(db):
        conn = connect(db)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM game WHERE id = {value}")
        conn.commit()

        for widget in frame_top.winfo_children():
            widget.destroy()
        window()

def click_filter(value):
    if check_db(db):
        conn = connect(db)
        cursor = conn.cursor()
        sql = f"SELECT * FROM game ORDER BY {value.get()}"

        for widget in frame_top.winfo_children():
            widget.destroy()
    window(sql)

if __name__ == '__main__':
    root = Tk()
    root.title("Windows-приложение на Python с использованием базы данных")
    root.geometry("600x550")
    frame_top = LabelFrame(root, text="База данных")
    create_db()
    window()
    add_db()
    filter_db()
    root.mainloop()


