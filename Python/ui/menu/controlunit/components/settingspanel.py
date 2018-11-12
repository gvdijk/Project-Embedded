import tkinter as tk

from Python.core.controlunit.controlunit import ControlUnit
from Python.ui.menu.menu import Menu


class Settingspanel(tk.Frame):

    def __init__(self, parent: Menu, control_unit: ControlUnit):
        super().__init__(parent)
        self.control_unit = control_unit

        self.config(bg='#3D4C53')

        # Images for the footer buttons and labels.
        self.collapse_image = tk.PhotoImage(file='ui/collapse_white.png')
        self.retract_image =tk.PhotoImage(file='ui/retract_white.png')
        self.toggle_off =tk.PhotoImage(file='ui/toggle_off_white.png')
        self.toggle_on =tk.PhotoImage(file='ui/toggle_on_white.png')

        # Configuring the footer buttons.
        self.min_dis_label = tk.Label(self, text='Min Afstand', foreground='#EEEEEE', bg='#3D4C53', font='Serif 10', width=10)
        self.max_dis_label = tk.Label(self, text='Max Afstand', foreground='#EEEEEE', bg='#3D4C53', font='Serif 10', width=10)
        self.threshold_label = tk.Label(self, text='Sensor', foreground='#EEEEEE', bg='#3D4C53', font='Serif 10', width=10)

        self.min_dis_entry = tk.Entry(self)
        self.max_dis_entry = tk.Entry(self)
        self.threshold_entry = tk.Entry(self)

        threshold_val = self.control_unit.get_sensor_thresh_hold()
        if self.control_unit.get_sensor_type().__str__() == 'Type.TEMPERATURE':
            threshold_val = round((threshold_val * 4.8828125) / 10)
        elif self.control_unit.get_sensor_type().__str__() == 'Type.LIGHT':
            threshold_val = round((threshold_val / 1023) * 100)
        else:
            print('Undefined Type')

        self.min_dis_entry.insert(0, self.control_unit.get_min_distance())
        self.max_dis_entry.insert(0, self.control_unit.get_max_distance())
        self.threshold_entry.insert(0, threshold_val)


        self.min_dis_button = tk.Button(self, bg='#3D4C53', foreground='#EEEEEE', text='Set', command=self.getMinDis, width=20, relief='ridge')
        self.max_dis_button = tk.Button(self, bg='#3D4C53', foreground='#EEEEEE', text='Set', command=self.getMaxDis, width=20, relief='ridge')
        self.threshold_button = tk.Button(self, bg='#3D4C53', foreground='#EEEEEE', text='Set', command=self.getThreshold, width=20, relief='ridge')

        # Packing the footer buttons.
        self.min_dis_label.pack(side='left')
        self.min_dis_entry.pack(side='left')
        self.min_dis_button.pack(side='left')
        self.max_dis_label.pack(side='left')
        self.max_dis_entry.pack(side='left')
        self.max_dis_button.pack(side='left')
        self.threshold_label.pack(side='left')
        self.threshold_entry.pack(side='left')
        self.threshold_button.pack(side='left')

    def getMinDis(self):
        try:
            if int(self.min_dis_entry.get()) in range(1, 180):
                self.control_unit.set_min_distance(self.min_dis_entry.get())
        except:
            print('Invalid input')

    def getMaxDis(self):
        try:
            if int(self.min_dis_entry.get()) in range(1, 180):
                self.control_unit.set_max_distance(self.max_dis_entry.get())
        except:
            print('Invalid input')

    def getThreshold(self):
        try:
            print(self.control_unit.get_sensor_type())
            if self.control_unit.get_sensor_type().__str__() == 'Type.TEMPERATURE':
                input = int(self.threshold_entry.get())
                if 30 > input > 10:
                    value = str(int(round(int(input / 4.8828125 * 10))))
                    self.control_unit.set_sensor_threshold(value)
                else:
                    print('Out of Range Temperature')
            elif self.control_unit.get_sensor_type().__str__() == 'Type.LIGHT':
                input = int(self.threshold_entry.get())
                if 100 > input > 0:
                    value = str(int(round(int(input * 1023 / 100))))
                    print(value)
                    self.control_unit.set_sensor_threshold(value)
                else:
                    print('Out of Range Light')
            else:
                print('Undefined Type')
        except:
            print('Invalid input')

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
