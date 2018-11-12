import tkinter as tk

from Python.core.controlunit.controlunit import ControlUnit
from Python.event.event import Event
from Python.ui.menu.MenuStack import MenuStack
from Python.ui.menu.controlunit.controlunitmenu import ControlUnitMenu


class ControlUnitSelect(tk.Frame):

    def __init__(self, parent: tk.Frame):
        print('Initializing class ControlUnitSelect')
        super().__init__(parent)

        self.pack(fill='both', expand=True)
        self.unit_box = tk.Frame(self, bg='#4DB3B3', padx=10, pady=10, width=500, height=300)
        self.unit_box.pack(fill='both', expand=True)
        self.title_label = tk.Label(self.unit_box, padx=10, pady=10, text='Aangesloten Eenheden', foreground='#EEEEEE',
                                    bg='#4DB3B3', font='Serif 10 bold')
        self.title_label.pack()

        self.control_units = []
        self.unit_frames = []
        self.distance_texts = {}

        Event.events['control_unit_added'].add_listener(
            lambda data: self.add_option(data['control_unit'])
        )

        Event.events['control_unit_removed'].add_listener(
            lambda data: self.remove_option(data['control_unit'])
        )

    def on_list_box_select(self, event):
        if event.widget.winfo_class() == 'Frame':
            MenuStack.next(ControlUnitMenu(MenuStack.root, event.widget.control_unit))
        else:
            MenuStack.next(ControlUnitMenu(MenuStack.root, event.widget.master.control_unit))

    def redo_unit_frames(self):
        for frame in self.unit_frames:
            frame.pack_forget()
            frame.destroy()

        self.unit_frames = []
        for unit in self.control_units:
            print(unit)
            unit_frame = tk.Frame(self.unit_box, borderwidth=1, relief="solid", bg='#3D4C53', width=300, height=180,
                                  cursor='crosshair')
            unit_frame.pack(fill='x')

            unit_frame.control_unit = unit

            if unit.type.__str__() == 'Type.TEMPERATURE':
                name = "Temperatuur Eenheid"
            elif unit.type.__str__() == 'Type.LIGHT':
                name = "Lichtsintensiteit Eenheid"

            self.distance_texts[unit] = tk.StringVar()

            def update_distance_text(percentage, unit):
                self.distance_texts[unit].set('{}%'.format(percentage))

            unit.rolled_percentage_changed_event.add_listener(
                lambda event_data: update_distance_text(event_data['percentage'], unit)
            )

            unit_frame.unit_image = tk.PhotoImage(file='ui/arduino.png')
            unit_frame.image_label = tk.Label(unit_frame, width=100, image=unit_frame.unit_image, bg='#3D4C53', padx=25,
                                              pady=15, cursor='crosshair')
            unit_frame.type_label = tk.Label(unit_frame, width=20, text=name, foreground='#EEEEEE', bg='#3D4C53',
                                             font='Serif 12 bold', cursor='crosshair')

            unit_frame.status_label = tk.Label(unit_frame, width=20, textvariable=self.distance_texts[unit], foreground='#EEEEEE',
                                               bg='#3D4C53', font='Serif 12 bold', cursor='crosshair')

            unit_frame.image_label.pack(side='left')
            unit_frame.type_label.pack(side='left')
            unit_frame.status_label.pack(side='left')

            unit_frame.bindtags(('tagger',) + unit_frame.bindtags())
            for child in unit_frame.children.values():
                child.bindtags(('tagger',) + child.bindtags())

            self.bind_class('tagger', '<Button-1>', self.on_list_box_select)

            self.unit_frames.append(unit_frame)

    def add_option(self, control_unit: ControlUnit):
        print(control_unit)
        self.control_units.append(control_unit)
        self.redo_unit_frames()

    def remove_option(self, control_unit: ControlUnit):
        self.control_units.remove(control_unit)
        self.redo_unit_frames()
        pass
