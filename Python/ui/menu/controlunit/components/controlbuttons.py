import tkinter as tk

from Python.core.controlunit.controlunit import ControlUnit
from Python.ui.menu.menu import Menu


class ControlButtons(tk.Frame):

    def __init__(self, parent: Menu, control_unit: ControlUnit):
        super().__init__(parent)

        self.control_unit = control_unit

        roll_in_button = tk.Button(self, text='Roll in', command=self.roll_in)
        roll_out_button = tk.Button(self, text='Roll out', command=self.roll_out)
        auto_roll_checkbox = tk.Checkbutton(self, text='Auto roll', command=self.auto_roll)

        roll_in_button.grid(row=0, column=0)
        roll_out_button.grid(row=0, column=1)
        auto_roll_checkbox.grid(row=0, column=2)

    def roll_in(self):
        self.control_unit.screen_roll_in()

    def roll_out(self):
        self.control_unit.screen_roll_out()

    def auto_roll(self):
        pass



