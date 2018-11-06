from Python.ui.menu.main.component.controlunitselect import ControlUnitSelect
from Python.ui.menu.menu import *


class MainMenu(Menu):

    def __init__(self, parent):
        print('Initializing class MainMenu')
        super().__init__(parent)
        self.control_unit_select = ControlUnitSelect(self)
        self.control_unit_select.grid(row=2, column=1)
