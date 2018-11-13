import tkinter as tk


class Menu(tk.Frame):

    def __init__(self, root: tk.Frame, name: str, base_layout=True):
        print('Initializing class Menu')
        super().__init__(root)

        self.base_layout = base_layout

        if not base_layout:
            return

        # Create all of the main containers
        self.top_frame = tk.Frame(root, bg='#3D4C53', width=450, height=50, pady=3)
        self.center = tk.Frame(root, bg='#EEEEEE', width=450, height=450, pady=3)
        self.footer = tk.Frame(root, bg='#E6772E', width=450, height=50, pady=3)

    # Open this instance of the menu
    def open(self):
        if not self.base_layout:
            return

        # Packing the main containers
        self.top_frame.pack(fill='x', expand=False)
        self.center.pack(fill='both', expand=True)
        self.footer.pack(fill='x', expand=False, anchor='s')

    # Close this instance of the menu
    def close(self):
        if not self.base_layout:
            return

        self.top_frame.pack_forget()
        self.center.pack_forget()
        self.footer.pack_forget()

    # Actions to do when this Menu is deleted. Currently not applicable
    def on_delete(self):
        pass
