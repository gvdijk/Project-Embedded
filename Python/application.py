import tkinter as tk

from Python.core.controlunit.controlunit import ControlUnit
from Python.core.engine.engine import Engine
from Python.ui.menu.MenuStack import MenuStack
from Python.ui.menu.main.mainmenu import MainMenu
from Python.ui.menu.menu import Menu


class Application(tk.Frame):

    def __init__(self, tk_root):
        super().__init__(tk_root)

        self.engine = Engine()

        self.menu_stack = MenuStack(tk_root)
        self.menu_stack.next(MainMenu(MenuStack.root))

        self.engine.start()



if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(fill='both')
    root.mainloop()
