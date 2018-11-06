import tkinter as tk

from Python.core.engine.engine import Engine
from Python.ui.menu.main.mainmenu import MainMenu


class Application(tk.Frame):

    def __init__(self, tk_root):
        super().__init__(tk_root)
        self.engine = Engine()
        self.after(10, self.engine.tick())
        self.main_menu = MainMenu(self)
        self.main_menu.pack(side="top", fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
