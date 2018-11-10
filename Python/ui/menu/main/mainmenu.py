from Python.ui.menu.component.header import Header
from Python.ui.menu.main.component.controlunitselect import ControlUnitSelect
from Python.ui.menu.menu import *


class MainMenu(Menu):

    def __init__(self, parent):
        print('Initializing class MainMenu')
        super().__init__(parent, 'Main menu')

        header = Header(self.top_frame, text='Main menu')
        header.grid(row=0, column=0, sticky="ew")

        self.control_unit_select = ControlUnitSelect(self.center)
        self.control_unit_select.grid(row=0, column=0)
