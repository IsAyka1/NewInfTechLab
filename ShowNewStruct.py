from functools import partial
from tkinter import *
import json


def update_struct(data):
    new_data = {}
    # new_data = {
    #     'id':
    #         {
    #             'name': '',
    #             'region':
    #                 {
    #                     'id': '',
    #                     'value': '',
    #                     'geo':
    #                         {
    #                             'lon': '',
    #                             'lat': ''
    #                         }
    #                 }
    #         }
    # }

    for country in data:
        new_data.update({
            country['id']:
                {
                    'name': country['name'],
                    'region':
                        {
                            'id': country['region']['id'],
                            'value': country['region']['value'],
                            'geo':
                                {
                                    'lon': country['longitude'],
                                    'lat': country['latitude']
                                }
                        }
                }
        }
    )

    return json.dumps(new_data, indent=4, sort_keys=True)


def load_file(text_box):
    data = None

    with open('country_list.json') as file:
        data = json.load(file)

    data = update_struct(data)

    text_box.config(state='normal')
    text_box.delete(1.0, END)
    text_box.insert(END, data)
    text_box.config(state='disabled')


def show_new_struct(root):
    frame = Frame(root)
    text_box = Text(frame)
    text_box.pack(expand=True)
    button = Button(frame, text='Получить новый json из файла', command=partial(load_file, text_box))
    button.pack()

    frame.pack()
