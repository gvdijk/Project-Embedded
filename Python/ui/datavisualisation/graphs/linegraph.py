from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

import tkinter as tk


class LineGraph(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.x_data = [0.0]
        self.y_data = [0.0]
        self.limit = None

        figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = figure.add_subplot(1, 1, 1)

        self.canvas = FigureCanvasTkAgg(figure, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # toolbar = NavigationToolbar2Tk(canvas, self)
        # toolbar.update()
        # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def add_value(self, y: float):
        self.x_data.append(self.x_data[len(self.x_data) - 1] + 1)
        self.y_data.append(y)

        if self.limit is not None and len(self.x_data) > self.limit:
            self.x_data.pop(0)
            self.y_data.pop(0)

        self.plot.plot(self.x_data, self.y_data, 'r')
        self.canvas.draw()
