import tkinter as tk

from Python.event.event import Event


class ControlUnitSelect(tk.Frame):

    def __init__(self, parent: tk.Frame):
        super().__init__(parent)
        Event.events['control_unit_added'].add_listener(lambda x: print('hii'))
