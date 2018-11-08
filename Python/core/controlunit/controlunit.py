from enum import Enum

from Python.core.controlunit.connection import Connector


class ControlUnit:
    pass

    class Type(Enum):
        LIGHT = 1
        TEMPERATURE = 2

    class Instruction(Enum):
        READ_SENSOR_TYPE = 0
        READ_SENSOR_DATA = 1
        READ_SENSOR_THRESHOLD = 2
        READ_DISTANCE = 3
        READ_MIN_DISTANCE = 4
        READ_MAX_DISTANCE = 5
        SCREEN_ROLL_OUT = 6
        SCREEN_ROLL_IN = 7
        SCREEN_STOP_ROLL = 8
        TOGGLE_SENSOR_AUTO_ROLL = 9
        SET_MIN_DISTANCE = 10
        SET_MAX_DISTANCE = 11
        SET_SENSOR_THRESHOLD = 12

    def __init__(self, unit_type: Type, serial_number: str):
        print('Initializing class Control unit of type ' + unit_type.__str__())
        self.type = unit_type
        self.id = id
        self.data = []
        self.connection = Connector(serial_number)

    def add_data(self, value):
        self.data.append(value)

    def __send_instruction(self, instruction: Instruction):
        pass  # TODO Implement
