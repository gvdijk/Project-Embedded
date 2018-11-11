import tkinter as tk
import datetime

from Python.ui.menu.MenuStack import MenuStack


class Header(tk.Frame):

    def __init__(self, parent, text='', **kwargs):
        print('Initializing class Header')
        super().__init__(parent, kwargs)

        self.back_image = tk.PhotoImage(file='ui/back_white.png')
        self.home_image = tk.PhotoImage(file='ui/home_white.png')

        self.config(bg='#3D4C53')

        self.columnconfigure(0, weight=2)

        if MenuStack.can_back():
            self.back_button = tk.Button(self, text='back', image=self.back_image, command=lambda: MenuStack.back(), bg='#3D4C53', relief='flat', width=60)
        else:
            self.back_button = tk.Label(self, text='menu', image=self.home_image, bg='#3D4C53', width=60)

        self.back_button.pack(side='left', expand=False)


        self.name_label = tk.Label(self, text=text, foreground='#EEEEEE', bg='#3D4C53', font='Verdana 16')

        self.time_text = tk.StringVar()
        self.time_label = tk.Label(self, textvariable=self.time_text, foreground='#EEEEEE', bg='#3D4C53', width=6, font='Serif 12 bold')

        self.name_label.pack(side='left', fill='x', expand=True)
        self.time_label.pack(side='left', expand=False)

        self.update_time_loop()

    def update_time_loop(self):
        self.time_text.set(datetime.datetime.now().strftime("%H:%M"))
        self.after(1000, self.update_time_loop)
