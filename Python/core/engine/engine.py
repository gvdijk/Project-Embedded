from Python.core.controlunit.controlunit import ControlUnit
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

        self.__control_units = []
        self.on_control_unit_added = Engine.ControlUnitAddedEvent()
        self.on_control_unit_removed = Engine.ControlUnitRemovedEvent()

    def add_control_unit(self, control_unit: ControlUnit):
        self.__control_units.append(control_unit)
        self.on_control_unit_added.call(control_unit=control_unit)

    def remove_control_unit(self, control_unit: ControlUnit):
        self.__control_units.remove(control_unit)
        self.on_control_unit_removed.call(control_unit=control_unit)

    def tick(self):
        self.poll_control_units()

    def poll_control_units(self):
        pass  # TODO implement method
