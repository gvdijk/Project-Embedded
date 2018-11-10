import tkinter as tk


class Menu(tk.Frame):

    def __init__(self, root: tk.Frame, name: str, base_layout=True):
        print('Initializing class Menu')
        super().__init__(root)

        if not base_layout:
            return

        # create all of the main containers
        self.top_frame = tk.Frame(root, bg='cyan', width=450, height=50, pady=3)
        self.center = tk.Frame(root, bg='red', width=450, height=450, pady=3)
        self.footer = tk.Frame(root, bg='pink', width=450, height=50, pady=3)

        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        self.top_frame.grid(row=0, sticky="ew")
        self.center.grid(row=1, sticky="nsew")
        self.footer.grid(row=3, sticky="ew")

        # create the self.self.center widgets
        self.center.grid_rowconfigure(0, weight=1)
        self.center.grid_columnconfigure(1, weight=1)
