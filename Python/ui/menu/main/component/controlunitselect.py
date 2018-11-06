import tkinter as tk

from Python.core.controlunit.controlunit import ControlUnit
from Python.event.event import Event


class ControlUnitSelect(tk.Frame):

    def __init__(self, parent: tk.Frame):
        print('Initializing class ControlUnitSelect')
        super().__init__(parent)
        self.options = {}

        Event.events['control_unit_added'].add_listener(
            lambda data: self.add_option(data['control_unit'])
        )
        Event.events['control_unit_removed'].add_listener(
            lambda data: self.remove_option(data['control_unit'])
        )

    def add_option(self, control_unit: ControlUnit):
        label = tk.Label(self, text=control_unit.type.__str__())
        label.grid(row=len(self.options) + 1, column=1)
        self.options[control_unit] = label

    def remove_option(self, control_unit: ControlUnit):
        pass
