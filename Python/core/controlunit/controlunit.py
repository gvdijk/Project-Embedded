import asyncio
import time
from enum import Enum
from threading import Thread

import serial
import serial.tools.list_ports

from Python.core.controlunit.Instructions import *
from Python.core.controlunit.connection import Connector
from Python.event.event import Event


class ControlUnit:
    class ConnectionLostEvent(Event):
        pass

    class DataAddedEvent(Event):
        pass

    class Type(Enum):
        LIGHT = 1
        TEMPERATURE = 2
        UNIDENTIFIED = 10

    def __init__(self, port, unit_type: Type = Type.UNIDENTIFIED):
        self.port = port
        self.ser = serial.Serial(
            port=port,
            baudrate=19200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=2
        )

        self.connection_lost_event = ControlUnit.ConnectionLostEvent()
        self.data_added_event = ControlUnit.DataAddedEvent()

        self.type = unit_type
        self.id = id
        self.distance = 0

        self.recorded_data = []

    def add_data(self, value):
        self.recorded_data.append(value)
        self.data_added_event.call(value=value)

    def __still_connected(self):
        return self.port in [p.device for p in serial.tools.list_ports.comports()]

    def send_instruction(self, instruction: Instruction):
        if not self.__still_connected():
            return 0

        if not self.ser.isOpen():
            self.ser.open()

        self.ser.write(instruction.command)
        while self.ser.isOpen():
            time.sleep(.010)
            result = self.ser.read(instruction.bytes)

            if result == b'':
                return b'\x00'
            elif result != b'\x00':
                return result
        else:
            return b'\x00'

    def send_instruction_and_value(self, instruction: Instruction, value):
        if not self.__still_connected():
            return 0

        self.ser.write(instruction.command)
        time.sleep(.010)

        if self.ser.read(1) == b'\xf0':
            self.ser.write(self.__get_byte(value, 'low'))

        if instruction.bytes == 2 and self.ser.read(1) == b'\xf0':
            self.ser.write(self.__get_byte(value, 'high'))

        return self.ser.read(1)

    def get_sensor_type(self):
        response = self.send_instruction(READ_SENSOR_TYPE)

        switcher = {
            97: ControlUnit.Type.TEMPERATURE,
            98: ControlUnit.Type.LIGHT,
        }

        return switcher.get(int(response.hex(), 16), ControlUnit.Type.UNIDENTIFIED)

    def get_min_distance(self):
        response = self.send_instruction(READ_MIN_DISTANCE)
        return int(response.hex(), 16)

    def get_max_distance(self):
        response = self.send_instruction(READ_MAX_DISTANCE)
        return int(response.hex(), 16)

    def get_sensor_data(self):
        response = self.send_instruction(READ_SENSOR_DATA)
        value = int(response.hex(), 16)
        return value

    def get_temperature(self):
        return ((self.get_sensor_data() * 4.8828125) - 500)/10

    def get_sensor_thresh_hold(self):
        response = self.send_instruction(READ_SENSOR_THRESHOLD)
        return int(response.hex(), 16)

    def get_distance(self):
        response = self.send_instruction(READ_DISTANCE)
        return int(response.hex(), 16)

    def set_min_distance(self, value):
        response = self.send_instruction_and_value(SET_MIN_DISTANCE, value)
        return self.__hex_bool_convert(response)

    def set_max_distance(self, value):
        response = self.send_instruction_and_value(SET_MAX_DISTANCE, value)
        return self.__hex_bool_convert(response)

    def set_sensor_threshold(self, value):
        response = self.send_instruction_and_value(SET_SENSOR_THRESHOLD, value)
        return self.__hex_bool_convert(response)

    def toggle_sensor_auto_roll(self):
        print('toggled')
        response = self.send_instruction(TOGGLE_AUTO_ROLL)
        return self.__hex_bool_convert(response)

    def screen_roll_out(self):
        print('rolling out')
        response = self.send_instruction(SCREEN_ROLL_OUT)
        return self.__hex_bool_convert(response)

    def screen_roll_in(self):
        print('rolling in')
        response = self.send_instruction(SCREEN_ROLL_IN)
        return self.__hex_bool_convert(response)

    def __hex_bool_convert(self, hex):
        if hex == b'\xff':
            return True
        elif hex == b'\x0f':
            return False
        else:
            return None

    def __get_byte(self, value, pos):
        if pos == 'high':
            return bytes.fromhex('{:02x}'.format((int(value) >> 8)))
        elif pos == 'low':
            return bytes.fromhex('{:02x}'.format((int(value) & 255)))
        else:
            return None

    #
    # def screen_stop_roll(self):
    #     return self.__hex_bool_convert(self.__send_command(b'\xc3'))
    #
    # def toggle_sensor_auto_roll(self):
    #     return self.__hex_bool_convert(self.__send_command(b'\xc4'))
    #
    # def toggle_temperature_auto_roll(self):
    #     return self.__hex_bool_convert(self.__send_command(b'\xc5'))
