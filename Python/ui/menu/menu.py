import tkinter as tk


class Menu(tk.Frame):

    def __init__(self, root: tk.Frame, name: str, base_layout=True):
        print('Initializing class Menu')
        super().__init__(root)

        self.base_layout = base_layout

        if not base_layout:
            return

        # create all of the main containers
        self.top_frame = tk.Frame(root, bg='#3D4C53', width=450, height=50, pady=3)
        self.center = tk.Frame(root, bg='#EEEEEE', width=450, height=450, pady=3)
        self.footer = tk.Frame(root, bg='#E6772E', width=450, height=50, pady=3)

        # layout all of the main containers
        # root.grid_rowconfigure(1, weight=1)
        # root.grid_columnconfigure(0, weight=1)

        # create the self.self.center widgets
        # self.center.grid_rowconfigure(0, weight=1)
        # self.center.grid_columnconfigure(1, weight=1)

    def open(self):
        if not self.base_layout:
            return

        self.top_frame.pack(fill='x', expand=False)
        self.center.pack(fill='both', expand=True)
        self.footer.pack(fill='x', expand=False, anchor='s')

    def close(self):
        if not self.base_layout:
            return

        self.top_frame.pack_forget()
        self.center.pack_forget()
        self.footer.pack_forget()

    def on_delete(self):
        pass
