from Python.core.controlunit.controlunit import ControlUnit
from Python.ui.datavisualisation.graphs.linegraph import LineGraph
from Python.ui.menu.menu import *


class ControlUnitMenu(Menu):

    def __init__(self, parent: tk.Frame, control_unit: ControlUnit):
        print('Initializing class ControlUnitMenu for control unit type ' + control_unit.type.__str__())
        super().__init__(parent)
        self.control_unit = control_unit
        self.control_unit.on_data_added_listeners.append(self.update_line_graph())

        self.line_graph = LineGraph(self)
        self.line_graph.grid(row=1, column=0)

    def update_line_graph(self):
        print('test')
        pass
