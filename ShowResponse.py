from functools import partial
from random import randint
from tkinter import *
import requests
import json


def get_request_json(text_box):
    response = requests.get(f'http://numbersapi.com/{randint(0, 100)}/math?json')

    text = None

    if response.status_code == 200:
        text = json.loads(str(response.json()).replace('\'', '"').replace('True', 'true').replace('False', 'false'))
        text = json.dumps(text, indent=4, sort_keys=True)
        print(text)
    else:
        print("Error " + str(response.text))
        text = '{}'

    text_box.config(state='normal')
    text_box.delete(1.0, END)
    text_box.insert(END, text)
    text_box.config(state='disabled')


def show_response(root):
    frame = Frame(root)
    text_box = Text(frame)
    text_box.pack(expand=True)
    button = Button(frame, text='Получить json от api', command=partial(get_request_json, text_box))
    button.pack()

    frame.pack()