import tkinter as tk
import datetime

from Python.ui.menu.MenuStack import MenuStack


class Header(tk.Frame):

    def __init__(self, parent, text='', **kwargs):
        print('Initializing class Header')
        super().__init__(parent, kwargs)

        if MenuStack.can_back():
            back_button = tk.Button(text='back', command=lambda: MenuStack.back())
            back_button.grid(column=0, row=0)

        self.name_label = tk.Label(self, text=text)

        self.time_text = tk.StringVar()
        self.time_label = tk.Label(self, textvariable=self.time_text)

        self.name_label.grid(row=0, column=1)
        self.time_label.grid(row=0, column=2)

        self.update_time_loop()

    def update_time_loop(self):
        self.time_text.set(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.after(1000, self.update_time_loop)
