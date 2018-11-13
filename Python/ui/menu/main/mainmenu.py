from Python.ui.menu.component.header import Header
from Python.ui.menu.main.component.controlunitselect import ControlUnitSelect
from Python.ui.menu.menu import *


class MainMenu(Menu):

    def __init__(self, parent):
        print('Initializing class MainMenu')
        super().__init__(parent, 'Main menu')

        # Add the Header to the Menu
        header = Header(self.top_frame, text='Main menu')
        header.pack(fill='x')

        # Load the Control Units view, this will cover the rest of the screen
        self.control_unit_select = ControlUnitSelect(self.center)
        self.control_unit_select.pack()
