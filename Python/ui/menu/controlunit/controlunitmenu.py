from threading import Thread

from Python.core.controlunit.controlunit import ControlUnit
from Python.ui.datavisualisation.graphs.linegraph import LineGraph
from Python.ui.menu.menu import *


class ControlUnitMenu(Menu):

    def __init__(self, parent, control_unit: ControlUnit):
        print('Initializing class ControlUnitMenu for control unit type ' + control_unit.type.__str__())
        super().__init__(parent)
        self.control_unit = control_unit

        self.line_graph = LineGraph(self)
        self.line_graph.grid(row=1, column=0)
        self.line_graph.limit = 100

        self.poll_data()

    def poll_data(self):
        value = self.control_unit.connector.readDistance()
        self.line_graph.add_value(value)
        self.after(100, self.poll_data)
