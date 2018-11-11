import tkinter as tk

from Python.core.controlunit.controlunit import ControlUnit


class InfoBar(tk.Frame):

    def __init__(self, parent, control_unit: ControlUnit):
        super().__init__(parent)

        self.control_unit = control_unit

        type_label = tk.Label(self, text='Control unit type: ' + control_unit.type.__str__().split('.')[1].lower())
        type_label.pack(side="left")

        self.rolled_perc_text = tk.StringVar()
        self.distance_perc_label = tk.Label(self, textvariable=self.rolled_perc_text)
        self.distance_perc_label.pack(side="left")

        control_unit.rolled_percentage_changed_event.add_listener(
            lambda event_data: self.update_text()
        )

    def update_text(self):
        self.rolled_perc_text.set(self.get_text())

    def get_text(self) -> str:
        return 'Rolled: {}%'.format(self.control_unit.rolled_percentage)
