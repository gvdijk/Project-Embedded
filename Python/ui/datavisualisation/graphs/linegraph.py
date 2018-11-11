import datetime
import tkinter as tk

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
import matplotlib.dates as mdates


class LineGraph(tk.Frame):

    def __init__(self, parent, y_data=[]):
        print('Initializing class LineGraph')
        super().__init__(parent)

        self.x_data = []
        self.y_data = y_data
        self.limit = 100

        self.figure = Figure(figsize=(6, 6), dpi=100)
        self.plot = self.figure.add_subplot(1, 1, 1)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # toolbar = NavigationToolbar2Tk(canvas, self)
        # toolbar.update()
        # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.draw()

    def add_value(self, y: float):
        # x_value = 0 if len(self.x_data) == 0 else self.x_data[-1] + 1
        self.x_data.append(datetime.datetime.now())
        self.y_data.append(y)

    def draw(self):
        self.after(1000, self.draw)

        if len(self.x_data) == 0:
            return

        from_index = len(self.x_data) - self.limit
        if from_index < 0:
            from_index = 0

        self.plot.clear()

        self.plot.plot_date(self.x_data[from_index: -1], self.y_data[from_index: -1], 'r')

        self.figure.autofmt_xdate()

        # myFmt = mdates.DateFormatter('%D:%H:%M')
        # self.plot.xaxis.set_major_formatter(myFmt)

        self.canvas.draw()

