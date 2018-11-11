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

        header = Header(self.top_frame, text='Control unit menu')
        header.grid(row=0, column=0, sticky="ew")

        self.line_graph = LineGraph(self.center)
        self.line_graph.grid(row=1, sticky="new")
        self.line_graph.limit = 100

        for i in control_unit.recorded_data:
            self.line_graph.add_value(i)

        button_wrapper = tk.Frame(self.center)
        hour_button = tk.Button(button_wrapper, text='Last Hour', command=self.hour_button_click)
        day_button = tk.Button(button_wrapper, text='Last Day', command=self.day_button_click)
        week_button = tk.Button(button_wrapper, text='Last Week', command=self.week_button_click)

        button_wrapper.grid(row=2)
        hour_button.grid(row=0, column=0)
        day_button.grid(row=0, column=1)
        week_button.grid(row=0, column=2)

        self.control_buttons = ControlButtons(self.footer, control_unit)
        self.control_buttons.grid()

        self.control_unit.data_added_event.add_listener(
            lambda event_data: self.line_graph.add_value(event_data['value'])
        )

    def hour_button_click(self):
        self.line_graph.limit = int(3600 / 40)

    def day_button_click(self):
        self.line_graph.limit = int(86400 / 40)

    def week_button_click(self):
        self.line_graph.limit = int(604800 / 40)
