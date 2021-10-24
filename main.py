from tkinter import *
from ShowResponse import show_response
from ShowNewStruct import show_new_struct
from ShowTreeView import show_treeview


def main(root):
    show_response(root)
    show_treeview(root)
    show_new_struct(root)


if __name__ == '__main__':
    root = Tk()
    main(root)
    root.mainloop()
