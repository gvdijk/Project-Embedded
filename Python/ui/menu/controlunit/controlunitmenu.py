from Python.core.controlunit.controlunit import ControlUnit
from Python.ui.datavisualisation.graphs.linegraph import LineGraph
from Python.ui.menu.menu import *


class ControlUnitMenu(Menu):

    def __init__(self, parent: tk.Frame, control_unit: ControlUnit):
        super().__init__(parent)
        self.control_unit = control_unit
        self.line_graph = LineGraph(self)
        self.line_graph.grid(row=1, column=0)
