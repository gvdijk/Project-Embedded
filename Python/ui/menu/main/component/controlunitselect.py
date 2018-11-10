import tkinter as tk

from Python.core.controlunit.controlunit import ControlUnit
from Python.event.event import Event
from Python.ui.menu.MenuStack import MenuStack
from Python.ui.menu.controlunit.controlunitmenu import ControlUnitMenu


class ControlUnitSelect(tk.Frame):

    def __init__(self, parent: tk.Frame):
        print('Initializing class ControlUnitSelect')
        super().__init__(parent)

        list_box = tk.Listbox(self, width=50, height=4, font=("Helvetica", 12))
        list_box.bind('<<ListboxSelect>>', self.on_list_box_select)
        self.list_box = list_box
        self.list_box.pack()

        self.control_units = []

        Event.events['control_unit_added'].add_listener(
            lambda data: self.add_option(data['control_unit'])
        )

        Event.events['control_unit_removed'].add_listener(
            lambda data: self.remove_option(data['control_unit'])
        )

    def on_list_box_select(self, event):
        index = event.widget.curselection()[0]
        MenuStack.next(ControlUnitMenu(MenuStack.root, self.control_units[index]))

    def add_option(self, control_unit: ControlUnit):
        self.control_units.append(control_unit)
        self.list_box.insert(tk.END, control_unit.type.__str__())

    def remove_option(self, control_unit: ControlUnit):
        index = self.control_units.index(control_unit)
        self.control_units.remove(control_unit)
        self.list_box.delete(index)
        pass
