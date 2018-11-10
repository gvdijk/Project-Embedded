import tkinter as tk

from Python.ui.menu.menu import Menu


class ControlButtons(tk.Frame):

    def __init__(self, parent: Menu):
        super().__init__(parent)

        roll_in_button = tk.Button(self, text='Roll in')
        roll_out_button = tk.Button(self, text='Roll out')
        auto_roll_checkbox = tk.Checkbutton(self, text='Auto roll')

        roll_in_button.grid(row=0, column=0)
        roll_out_button.grid(row=0, column=1)
        auto_roll_checkbox.grid(row=0, column=2)


