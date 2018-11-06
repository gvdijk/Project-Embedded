import tkinter as tk

from Python.ui.menu.component.header import Header


class Menu(tk.Frame):

    def __init__(self, parent: tk.Frame):
        print('Initializing class Menu')
        super().__init__(parent)
        self.header = Header(self)
        self.header.grid(row=1)