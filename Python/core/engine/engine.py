import time
from threading import Thread

from Python.core.controlunit.controlunit import ControlUnit
from Python.core.engine.controlunitfinder import ControlUnitFinder
from Python.event.event import Event


class Engine:
    class ControlUnitAddedEvent(Event):
        def __init__(self):
            super().__init__('control_unit_added')

    class ControlUnitRemovedEvent(Event):
        def __init__(self):
            super().__init__('control_unit_removed')

    def __init__(self):
        print('Initializing class Engine')

        self.running = False
        self.__control_units = []
        self.control_unit_finder = ControlUnitFinder()
        self.control_unit_finder.control_unit_found_event.add_listener(self.on_control_unit_found)

        # Bind events to this Engine
        self.on_control_unit_added = Engine.ControlUnitAddedEvent()
        self.on_control_unit_removed = Engine.ControlUnitRemovedEvent()

    def on_control_unit_found(self, event_data):
        control_unit: ControlUnit = event_data['control_unit']
        control_unit.connection_lost_event.add_listener(
            lambda event_data: self.remove_control_unit(event_data['control_unit'])
        )
        self.add_control_unit(control_unit)

    # Add a control unit to this Engine
    def add_control_unit(self, control_unit: ControlUnit):
        self.__control_units.append(control_unit)
        self.on_control_unit_added.call(control_unit=control_unit)

    # Remove a control unit from this Engine
    def remove_control_unit(self, control_unit: ControlUnit):
        self.__control_units.remove(control_unit)
        self.on_control_unit_removed.call(control_unit=control_unit)

    # Start the engine on its own thread
    def start(self):
        self.running = True
        thread = Thread(target=self.tick)
        thread.start()

    # Engine tick, perform tasks based on tick count
    def tick(self):
        counter = 0
        while self.running:
            if counter % 10 == 0:
                self.control_unit_finder.poll()

            for control_unit in self.__control_units:
                if not control_unit.still_connected():
                    self.remove_control_unit(control_unit)
                    self.control_unit_finder.remove_control_unit(control_unit)
                    control_unit.disconnect()
                    continue

                if counter % 1 == 0:
                    control_unit.update_rolled_percentage()

                if counter % 2 == 0:
                    if control_unit.type == ControlUnit.Type.LIGHT:
                        control_unit.add_data(control_unit.get_light_percentage())

                    if control_unit.type == ControlUnit.Type.TEMPERATURE:
                        control_unit.add_data(control_unit.get_temperature())

            time.sleep(1)

            counter += 1
