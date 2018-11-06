import tkinter as tk
import datetime


class Header(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.name_label = tk.Label(self, text='Header Text')

        self.time_text = tk.StringVar()
        self.time_label = tk.Label(self, textvariable=self.time_text)

        self.name_label.grid(row=1, column=1)
        self.time_label.grid(row=1, column=2)

        self.update_time_loop()

    def update_time_loop(self):
        self.time_text.set(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.after(1000, self.update_time_loop)
