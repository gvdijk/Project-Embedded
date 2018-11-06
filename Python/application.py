import tkinter as tk

from Python.ui.menu.main.mainmenu import MainMenu


class Application(tk.Frame):

    def __init__(self, tk_root):
        super().__init__(tk_root)
        self.main_menu = MainMenu(self)
        self.main_menu.pack(side="top", fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
