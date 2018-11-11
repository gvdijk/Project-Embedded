from Python.core.controlunit.controlunit import ControlUnit
from Python.ui.datavisualisation.graphs.linegraph import LineGraph
from Python.ui.menu.component.header import Header
from Python.ui.menu.controlunit.components.controlbuttons import ControlButtons
from Python.ui.menu.menu import *


class ControlUnitMenu(Menu):

    def __init__(self, parent, control_unit: ControlUnit):
        print('Initializing class ControlUnitMenu for control unit type ' + control_unit.type.__str__())
        super().__init__(parent, 'Control unit menu')
        self.control_unit = control_unit

        self.time_05_image =tk.PhotoImage(file='ui/time_5_white.png')
        self.time_10_image =tk.PhotoImage(file='ui/time_10_white.png')
        self.time_30_image =tk.PhotoImage(file='ui/time_30_white.png')

        header = Header(self.top_frame, text='Control unit menu')
        header.pack(fill='x')

        x_data = []
        y_data = []
        for i in control_unit.recorded_data:
            x_data.append(i)
            y_data.append(control_unit.recorded_data[i])

        self.line_graph = LineGraph(self.center, x_data=x_data, y_data=y_data)
        self.line_graph.pack(fill='both', expand=True)
        self.line_graph.limit = 100

        button_wrapper = tk.Frame(self.center)
        time_05_button = tk.Button(button_wrapper, bg='#3D4C53', foreground='#EEEEEE', text='5 min', image=self.time_05_image, compound='left', command=self.time_05_click, width=100, relief='ridge')
        time_10_button = tk.Button(button_wrapper, bg='#3D4C53', foreground='#EEEEEE', text='10 min', image=self.time_10_image, compound='left', command=self.time_10_click, width=100, relief='ridge')
        time_30_button = tk.Button(button_wrapper, bg='#3D4C53', foreground='#EEEEEE', text='30 min', image=self.time_30_image, compound='left', command=self.time_30_click, width=100, relief='ridge')

        button_wrapper.pack()
        time_05_button.pack(side='left')
        time_10_button.pack(side='left')
        time_30_button.pack(side='left')

        self.control_buttons = ControlButtons(self.footer, control_unit)
        self.control_buttons.pack()

        self.control_unit.data_added_event.add_listener(
            lambda event_data: self.add_data(event_data['datetime'], event_data['value'])
        )

    def add_data(self, date_time, value):
        if self.control_unit.type == ControlUnit.Type.LIGHT:
            perc = (value / 1023) * 100
            self.line_graph.add_value(date_time, perc)
        elif self.control_unit.type == ControlUnit.Type.TEMPERATURE:
            self.line_graph.add_value(date_time, value)



    def time_05_click(self):
        self.line_graph.limit = int(3600 / 40)

    def time_10_click(self):
        self.line_graph.limit = int(86400 / 40)

    def time_30_click(self):
        self.line_graph.limit = int(604800 / 40)
