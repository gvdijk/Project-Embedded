import tkinter as tk

from Python.core.controlunit.controlunit import ControlUnit
from Python.core.engine.engine import Engine
from Python.ui.menu.MenuStack import MenuStack
from Python.ui.menu.main.mainmenu import MainMenu
from Python.ui.menu.menu import Menu


class Application(Menu):

    def __init__(self, tk_root):
        print('Initializing class Application')
        super().__init__(tk_root, header=False)

        self.engine = Engine()
        self.menu_stack = MenuStack(self)

        self.menu_stack.next(MainMenu(self))

        self.fake_data()

    def fake_data(self):
        self.engine.add_control_unit(ControlUnit(ControlUnit.Type.TEMPERATURE))
        self.engine.add_control_unit(ControlUnit(ControlUnit.Type.LIGHT))


if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
