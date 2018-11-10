from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

import tkinter as tk


class LineGraph(tk.Frame):

    def __init__(self, parent):
        print('Initializing class LineGraph')
        super().__init__(parent)

        self.x_data = [0.0]
        self.y_data = [0.0]
        self.limit = 100

        figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = figure.add_subplot(1, 1, 1)

        self.canvas = FigureCanvasTkAgg(figure, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # toolbar = NavigationToolbar2Tk(canvas, self)
        # toolbar.update()
        # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.draw()

    def add_value(self, y: float):
        self.x_data.append(self.x_data[len(self.x_data) - 1] + 1)
        self.y_data.append(y)

        if self.limit is not None and len(self.x_data) > self.limit:
            self.x_data.pop(0)
            self.y_data.pop(0)

    def draw(self):
        if len(self.x_data) == 0:
            return

        from_index = len(self.x_data) - self.limit
        if from_index < 0:
            from_index = 0

        self.plot.clear()

        self.plot.plot(self.x_data[from_index: -1], self.y_data[from_index: -1], 'r')
        self.canvas.draw()
        self.after(1000, self.draw)
