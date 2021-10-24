from functools import partial
from tkinter import *
from tkinter import ttk
import json


def update_struct(data, tree):
    for i in range(1, len(data)):
        country = data[i]
        tree.insert(parent='', index=i, iid=i, values=(
            country['id'],
            country['name'],
            country['region']['id'],
            country['region']['value'],
            country['longitude'],
            country['latitude']
        ))


def load_file(tree):
    data = None

    with open('country_list.json') as file:
        data = json.load(file)

    update_struct(data, tree)


def show_treeview(root):
    frame = Frame(root)
    tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6), show='headings')

    tree.heading(1, text='id')
    tree.heading(2, text='name')
    tree.heading(3, text='region id')
    tree.heading(4, text='region value')
    tree.heading(5, text='lon')
    tree.heading(6, text='lat')

    sb = Scrollbar(frame, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)

    tree.config(yscrollcommand=sb.set)

    tree.pack(expand=True)
    button = Button(frame, text='Красивое отображение данных файла', command=partial(load_file, tree))
    button.pack()

    frame.pack()
