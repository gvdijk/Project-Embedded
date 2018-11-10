from Python.core.controlunit.controlunit import ControlUnit
from Python.ui.datavisualisation.graphs.linegraph import LineGraph
from Python.ui.menu.controlunit.components.controlbuttons import ControlButtons
from Python.ui.menu.menu import *


class ControlUnitMenu(Menu):

    def __init__(self, parent, control_unit: ControlUnit):
        print('Initializing class ControlUnitMenu for control unit type ' + control_unit.type.__str__())
        super().__init__(parent, 'Control unit menu')
        self.control_unit = control_unit

        self.line_graph = LineGraph(self.center)
        self.line_graph.grid()
        self.line_graph.limit = 100

        self.control_buttons = ControlButtons(self.footer)
        self.control_buttons.grid()

        self.control_unit.data_added_event.add_listener(
            lambda event_data: self.line_graph.add_value(event_data['value'])
        )
