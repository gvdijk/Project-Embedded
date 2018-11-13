import tkinter as tk
import datetime

from Python.ui.menu.MenuStack import MenuStack


class Header(tk.Frame):

    def __init__(self, parent, text='', **kwargs):
        print('Initializing class Header')
        super().__init__(parent, kwargs)

        # Load the images for the labels
        self.back_image = tk.PhotoImage(file='ui/back_white.png')
        self.home_image = tk.PhotoImage(file='ui/home_white.png')

        # Set the background of the header
        self.config(bg='#3D4C53')

        # Add a Home label when in the main menu, else add a Back button
        if MenuStack.can_back():
            self.back_button = tk.Button(
                self, text='back', image=self.back_image, command=lambda: MenuStack.back(), bg='#3D4C53',
                relief='flat', width=60
            )
        else:
            self.back_button = tk.Label(self, text='menu', image=self.home_image, bg='#3D4C53', width=60)

        # Create labels, and accompanying text and image
        self.name_label = tk.Label(self, text=text, foreground='#EEEEEE', bg='#3D4C53', font='Verdana 16')
        self.time_text = tk.StringVar()
        self.time_image = tk.PhotoImage(file='ui/time_white.png')
        self.time_label = tk.Label(
            self, textvariable=self.time_text, foreground='#EEEEEE', bg='#3D4C53', image=self.time_image,
            compound='left', width=70, font='Serif 12 bold'
        )

        # Pack the header content
        self.back_button.pack(side='left', expand=None)
        self.name_label.pack(side='left', fill='x', expand=True)
        self.time_label.pack(side='left', expand=None)

        # Initialise the update loop for the time label
        self.update_time_loop()

    # Update the time every second
    def update_time_loop(self):
        self.time_text.set(datetime.datetime.now().strftime("%H:%M"))
        self.after(1000, self.update_time_loop)
