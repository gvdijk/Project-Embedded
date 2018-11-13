from Python.core.controlunit.controlunit import ControlUnit
from Python.ui.datavisualisation.graphs.linegraph import LineGraph
from Python.ui.menu.MenuStack import MenuStack
from Python.ui.menu.component.header import Header
from Python.ui.menu.controlunit.components.controlbuttons import ControlButtons
from Python.ui.menu.controlunit.components.settingspanel import Settingspanel
from Python.ui.menu.controlunit.components.infobar import InfoBar
from Python.ui.menu.menu import *


class ControlUnitMenu(Menu):

    def __init__(self, parent, control_unit: ControlUnit):
        print('Initializing class ControlUnitMenu for control unit type ' + control_unit.type.__str__())
        super().__init__(parent, 'Control unit menu')
        self.control_unit = control_unit

        # Get the images for the UI
        self.time_05_image = tk.PhotoImage(file='ui/time_5_white.png')
        self.time_10_image = tk.PhotoImage(file='ui/time_10_white.png')
        self.time_30_image = tk.PhotoImage(file='ui/time_30_white.png')

        # Add the Header to this Menu
        header = Header(self.top_frame, text='Control unit menu')
        header.pack(fill='x')

        # Label for the y axis of the graph
        y_label = 'Temperatuur in celcius' if control_unit.type == ControlUnit.Type.TEMPERATURE else 'Licht intensiteit'

        # Add and configure the graph
        self.line_graph = LineGraph(self.center, y_label)
        self.line_graph.pack(fill='both', expand=True)
        self.time_range_set(5)

        # Add an information bar to the header
        info_bar = InfoBar(self.top_frame, control_unit)
        info_bar.pack(fill='x')

        button_wrapper = tk.Frame(self.center)

        # Configure the graph buttons
        time_05_button = tk.Button(button_wrapper, bg='#3D4C53', foreground='#EEEEEE', text='5 min',
                                   image=self.time_05_image, compound='left', command=self.time_05_click, width=100,
                                   relief='ridge')
        time_10_button = tk.Button(button_wrapper, bg='#3D4C53', foreground='#EEEEEE', text='10 min',
                                   image=self.time_10_image, compound='left', command=self.time_10_click, width=100,
                                   relief='ridge')
        time_30_button = tk.Button(button_wrapper, bg='#3D4C53', foreground='#EEEEEE', text='30 min',
                                   image=self.time_30_image, compound='left', command=self.time_30_click, width=100,
                                   relief='ridge')

        # Pack the buttons
        button_wrapper.pack()
        time_05_button.pack(side='left')
        time_10_button.pack(side='left')
        time_30_button.pack(side='left')

        # Add the control buttons for this unit
        self.control_buttons = ControlButtons(self.footer, control_unit)
        self.control_buttons.pack()

        # Add the settings panel for this unit
        self.setting_buttons = Settingspanel(self.footer, control_unit)
        self.setting_buttons.pack()

        # Drop out of this Menu when connection with its unit is lost
        self.control_unit.disconnect_event.add_listener(
            lambda event_data: MenuStack.back()
        )

        # Add the data when a package is received from the unit through the enginge
        self.control_unit.data_added_event.add_listener(
            lambda event_data: self.add_data(event_data['datetime'], event_data['value'])
        )

    # Add data to the graph
    def add_data(self, date_time, value):
        self.line_graph.add_value(date_time, value)

    # Actions to do when this Menu is deleted. Currently not applicable
    def on_delete(self):
        pass

    # Set the graph range to 5 minutes
    def time_05_click(self):
        self.time_range_set(5)

    # Set the graph range to 10 minutes
    def time_10_click(self):
        self.time_range_set(10)

    # Set the graph range to 30 minutes
    def time_30_click(self):
        self.time_range_set(30)

    # Set the graph x axis range based on minutes
    def time_range_set(self, minutes):
        x_data = []
        y_data = []
        for i in self.control_unit.recorded_data:
            x_data.append(i)
            y_data.append(self.control_unit.recorded_data[i])

        self.line_graph.set_time_range(minutes, _x=x_data, _y=y_data)
