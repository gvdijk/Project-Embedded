import tkinter as tk

from Python.core.engine.engine import Engine
from Python.ui.menu.MenuStack import MenuStack
from Python.ui.menu.main.mainmenu import MainMenu

# The main Frame for the application
class Application(tk.Frame):
    def __init__(self, tk_root):
        super().__init__(tk_root)

        # Bind an Engine to this Application
        self.engine = Engine()

        # Bin a MenuStack to thiis Application, and add a MainMenu
        self.menu_stack = MenuStack(tk_root)
        self.menu_stack.next(MainMenu(MenuStack.root))

        # Start the Engine
        self.engine.start()


if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(fill='both', expand=True)
    root.mainloop()
