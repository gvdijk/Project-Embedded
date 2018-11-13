import math
import tkinter as tk

from Python.core.controlunit.controlunit import ControlUnit
from Python.event.event import Event
from Python.ui.menu.MenuStack import MenuStack
from Python.ui.menu.controlunit.controlunitmenu import ControlUnitMenu


class ControlUnitSelect(tk.Frame):

    def __init__(self, parent: tk.Frame):
        print('Initializing class ControlUnitSelect')
        super().__init__(parent)

        # Create and pack the main container and basic components
        self.pack(fill='both', expand=True)
        self.unit_box = tk.Frame(self, bg='#4DB3B3', padx=10, pady=10, width=500, height=300)
        self.title_label = tk.Label(self.unit_box, padx=10, pady=10, text='Aangesloten Eenheden', foreground='#EEEEEE', bg='#4DB3B3', font='Serif 10 bold')
        self.unit_box.pack(fill='both', expand=True)
        self.title_label.pack()

        # Create empty lists for data
        self.control_units = []
        self.unit_frames = []
        self.distance_texts = {}

        # Event is called when a unit is connected
        Event.events['control_unit_added'].add_listener(
            lambda data: self.add_option(data['control_unit'])
        )

        # Event is called when a unit is disconnected
        Event.events['control_unit_removed'].add_listener(
            lambda data: self.remove_option(data['control_unit'])
        )

    # Navigate to the control screen when a list unit is clicked
    def on_list_box_select(self, event):
        if event.widget.winfo_class() == 'Frame':
            MenuStack.next(ControlUnitMenu(MenuStack.root, event.widget.control_unit))
        else:
            MenuStack.next(ControlUnitMenu(MenuStack.root, event.widget.master.control_unit))

    # Update the list view of connected units
    def redo_unit_frames(self):
        # Delete all current frames
        for frame in self.unit_frames:
            frame.pack_forget()
            frame.destroy()

        self.unit_frames = []

        # Add new frames for each connected unit
        for unit in self.control_units:

            # Create and pack the frame body
            unit_frame = tk.Frame(
                self.unit_box, borderwidth=1, relief="solid", bg='#3D4C53', width=300, height=180, cursor='crosshair'
            )
            unit_frame.pack(fill='x')
            unit_frame.control_unit = unit

            # Name the unit based of type
            if unit.type.__str__() == 'Type.TEMPERATURE':
                name = "Temperatuur Eenheid"
            elif unit.type.__str__() == 'Type.LIGHT':
                name = "Lichtsintensiteit Eenheid"

            # Variable to store the distance for the label
            self.distance_texts[unit] = tk.StringVar()

            # Update and format the distance value
            def update_distance_text(percentage, unit):
                val = (round(percentage / 10)) * 10
                self.distance_texts[unit].set('{}%'.format(val))

            # Update the distance value whenever its value changes
            unit.rolled_percentage_changed_event.add_listener(
                lambda event_data: update_distance_text(event_data['percentage'], unit)
            )

            # Create labels and image
            unit_frame.unit_image = tk.PhotoImage(file='ui/arduino.png')
            unit_frame.image_label = tk.Label(
                unit_frame, width=100, bg='#3D4C53', cursor='crosshair', image=unit_frame.unit_image, padx=25, pady=15
            )
            unit_frame.type_label = tk.Label(
                unit_frame, width=20, bg='#3D4C53', cursor='crosshair', font='Serif 12 bold', foreground='#EEEEEE',
                text=name
            )
            unit_frame.status_label = tk.Label(
                unit_frame, width=20, bg='#3D4C53', cursor='crosshair', font='Serif 12 bold', foreground='#EEEEEE',
                textvariable=self.distance_texts[unit]
            )

            # Pack the labels
            unit_frame.image_label.pack(side='left')
            unit_frame.type_label.pack(side='left')
            unit_frame.status_label.pack(side='left')

            unit_frame.bindtags(('tagger',) + unit_frame.bindtags())
            for child in unit_frame.children.values():
                child.bindtags(('tagger',) + child.bindtags())

            self.bind_class('tagger', '<Button-1>', self.on_list_box_select)

            self.unit_frames.append(unit_frame)

    # Add an unit to the list and update the screen
    def add_option(self, control_unit: ControlUnit):
        self.control_units.append(control_unit)
        self.redo_unit_frames()

    # Remove an unit from the list and update the screen
    def remove_option(self, control_unit: ControlUnit):
        self.control_units.remove(control_unit)
        self.redo_unit_frames()
