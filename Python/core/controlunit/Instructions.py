class Instruction:
    def __init__(self, command, bytes: int):
        self.command = command
        self.bytes = bytes


READ_SENSOR_TYPE = Instruction(b'\x81', 1)
READ_SENSOR_DATA = Instruction(b'\x82', 2)
READ_SENSOR_THRESHOLD = Instruction(b'\x83', 2)
READ_DISTANCE = Instruction(b'\x91', 1)
READ_MIN_DISTANCE = Instruction(b'\x92', 1)
READ_MAX_DISTANCE = Instruction(b'\x93', 1)

SET_MIN_DISTANCE = Instruction(b'\xe1', 1)
SET_MAX_DISTANCE = Instruction(b'\xe2', 1)
SET_SENSOR_THRESHOLD = Instruction(b'\xf1', 2)

TOGGLE_AUTO_ROLL = Instruction(b'\xc4', 1)
SCREEN_ROLL_OUT = Instruction(b'\xc1', 1)
SCREEN_ROLL_IN = Instruction(b'\xc2', 1)
