import tkinter as tk

from Python.core.controlunit.controlunit import ControlUnit
from Python.core.engine.engine import Engine
from Python.ui.menu.MenuStack import MenuStack
from Python.ui.menu.main.mainmenu import MainMenu
from Python.ui.menu.menu import Menu


class Application(Menu):

    def __init__(self, tk_root):
        print('Initializing class Application')
        super().__init__(tk_root)

        self.engine = Engine()
        self.menu_stack = MenuStack(self)

        self.menu_stack.next(MainMenu(self))
        self.menu_stack.back()

        self.fake_data()

    def fake_data(self):
        self.engine.add_control_unit(ControlUnit(ControlUnit.Type.TEMPERATURE))

if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
