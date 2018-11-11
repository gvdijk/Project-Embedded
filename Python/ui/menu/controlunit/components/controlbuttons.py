import tkinter as tk

from Python.core.controlunit.controlunit import ControlUnit
from Python.ui.menu.menu import Menu


class ControlButtons(tk.Frame):

    def __init__(self, parent: Menu, control_unit: ControlUnit):
        super().__init__(parent)
        self.control_unit = control_unit

        # Images for the footer buttons and labels.
        self.collapse_image = tk.PhotoImage(file='ui/collapse_white.png')
        self.retract_image =tk.PhotoImage(file='ui/retract_white.png')
        self.toggle_off =tk.PhotoImage(file='ui/toggle_off_white.png')
        self.toggle_on =tk.PhotoImage(file='ui/toggle_on_white.png')

        # Configuring the footer buttons.
        self.roll_in_button = tk.Button(self, bg='#E6772E', foreground='#EEEEEE', state='disabled', text='Rol in', image=self.retract_image, compound='left', command=self.roll_in, width=100, relief='ridge')
        self.roll_out_button = tk.Button(self, bg='#E6772E', foreground='#EEEEEE', state='disabled', text='Rol uit', image=self.collapse_image, compound='left', command=self.roll_out, width=100, relief='ridge')
        self.auto_roll_toggle = tk.Button(self, bg='#E6772E', foreground='#EEEEEE', text='Automatisch', image=self.toggle_on, compound='left', command=self.auto_roll, width=120, relief='ridge')

        # Packing the footer buttons.
        self.roll_in_button.pack(side='left')
        self.roll_out_button.pack(side='left')
        self.auto_roll_toggle.pack(side='left')

    # Send a roll in command to the ControlUnit.
    def roll_in(self):
        self.control_unit.screen_roll_in()

    # Send a roll out command to the ControlUnit.
    def roll_out(self):
        self.control_unit.screen_roll_out()

    # Toggle the auto roll. Disable the manual controls if enabled.
    def auto_roll(self):
        result = self.control_unit.toggle_sensor_auto_roll()
        if result:
            self.auto_roll_toggle.config(image=self.toggle_on)
            self.roll_in_button.config(state='disabled')
            self.roll_out_button.config(state='disabled')
        else:
            self.auto_roll_toggle.config(image=self.toggle_off)
            self.roll_in_button.config(state='normal')
            self.roll_out_button.config(state='normal')
