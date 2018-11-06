from Python.core.controlunit.controlunit import ControlUnit


class Engine:

    def __init__(self):
        print('Initializing class Engine')

        self.control_units = []
        self.control_units.append(ControlUnit(ControlUnit.Type.LIGHT))
        self.control_units.append(ControlUnit(ControlUnit.Type.TEMPERATURE))

    def add_control_unit(self, control_unit: ControlUnit):
        self.control_units.append(control_unit)

    def remove_control_unit(self, control_unit: ControlUnit):
        self.control_units.remove(control_unit)

    def tick(self):
        self.poll_control_units()

    def poll_control_units(self):
        pass # TODO implement method