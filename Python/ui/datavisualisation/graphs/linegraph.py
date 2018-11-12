import datetime
import tkinter as tk

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure


class LineGraph(tk.Frame):

    def __init__(self, parent, y_label):
        super().__init__(parent)

        self.y_label = y_label

        self.x = []
        self.y = []

        self.figure = Figure(figsize=(6, 6), dpi=100)
        self.plot = self.figure.add_subplot(1, 1, 1)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.time_range = 5

        self.draw_loop()

    def add_value(self, x: datetime.datetime, y: float):
        self.x.append(x)
        self.y.append(y)

        # for index, date in enumerate(self.x):
        #     if date < datetime.datetime.now() - datetime.timedelta(minutes=30):
        #         del self.x[index]
        #         del self.y[index]

    def draw_loop(self):
        self.after(1000, self.draw_loop)
        self.draw()

    def set_time_range(self, minutes: int, _x=[], _y=[]):
        self.time_range = minutes

        x = []
        y = []

        now = datetime.datetime.now()
        past = now - datetime.timedelta(minutes=minutes)

        x.append(past)

        for index, date in enumerate(_x):
            if date > past:
                if len(y) == 0:
                    y.append(_y[index])

                x.append(date)
                y.append(_y[index])

        if len(y) == 0:
            y.append(0)

        x.append(now)
        y.append(y[-1])

        self.x = x
        self.y = y

    def draw(self):
        # print(self.x)
        # print(self.y)
        # return
        self.plot.clear()

        self.plot.set_ylabel(self.y_label)

        self.plot.plot_date(self.x, self.y, 'r')
        self.figure.autofmt_xdate()
        self.canvas.draw()
