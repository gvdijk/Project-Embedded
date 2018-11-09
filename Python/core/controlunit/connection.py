import time

import serial


class Connector():

    def __init__(self, serialport):
        self.ser = serial.Serial(
            port=serialport,
            baudrate=19200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=2
        )
        self.commands = {
            '0': self.readSensorType,
            '1': self.readSensorData,
            '2': self.readSensorThreshold,
            '3': self.readDistance,
            '4': self.readMinDistance,
            '5': self.readMaxDistance,
            '6': self.screenRollOut,
            '7': self.screenRollIn,
            '8': self.screenStopRoll,
            '9': self.toggleSensorAutoRoll,

            '10': self.setMinDistance,
            '11': self.setMaxDistance,
            '12': self.setSensorThreshold
        }

    def __sendCommand(self, command, bytes=1):
        if not self.ser.isOpen():
            self.ser.open()

        print('a')
        self.ser.write(command)
        print('b')
        while self.ser.isOpen():
            time.sleep(.010)
            result = self.ser.read(bytes)

            if result == b'':
                return b'\x00'
            elif result != b'\x00':
                return result
        else:
            return b'\x00'

    def __hexBoolConvert(self, hex):
        if hex == b'\xff':
            return True
        elif hex == b'\x0f':
            return False
        else:
            return None

    def __getByte(self, value, pos):
        if pos == 'high':
            return bytes.fromhex('{:02x}'.format((int(value) >> 8)))
        elif pos == 'low':
            return bytes.fromhex('{:02x}'.format((int(value) & 255)))
        else:
            return None

    def __sendCommandAndValue(self, command, value, bytes=1):
        if not self.ser.isOpen():
            self.ser.open()
        self.ser.write(command)
        time.sleep(.010)
        if self.ser.read(1) == b'\xf0':
            self.ser.write(self.__getByte(value, 'low'))
        if bytes == 2 and self.ser.read(1) == b'\xf0':
            self.ser.write(self.__getByte(value, 'high'))
        return self.ser.read(1)

    def readSensorType(self):
        result = int(self.__sendCommand(b'\x81', 1).hex(), 16)
        if result == 97:
            return 1
        elif result == 98:
            return 2
        else:
            return None

    def readSensorData(self):
        return int(self.__sendCommand(b'\x82', 2).hex(), 16)

    def readSensorThreshold(self):
        return int(self.__sendCommand(b'\x83', 2).hex(), 16)

    def readDistance(self):
        return int(self.__sendCommand(b'\x91').hex(), 16)

    def readMinDistance(self):
        return int(self.__sendCommand(b'\x92').hex(), 16)

    def readMaxDistance(self):
        return int(self.__sendCommand(b'\x93').hex(), 16)

    def screenRollOut(self):
        return self.__hexBoolConvert(self.__sendCommand(b'\xc1'))

    def screenRollIn(self):
        return self.__hexBoolConvert(self.__sendCommand(b'\xc2'))

    def screenStopRoll(self):
        return self.__hexBoolConvert(self.__sendCommand(b'\xc3'))

    def toggleSensorAutoRoll(self):
        return self.__hexBoolConvert(self.__sendCommand(b'\xc4'))

    def toggleTemperatureAutoRoll(self):
        return self.__hexBoolConvert(self.__sendCommand(b'\xc5'))

    def setMinDistance(self, suffix):
        return self.__hexBoolConvert(self.__sendCommandAndValue(b'\xe1', suffix))

    def setMaxDistance(self, suffix):
        return self.__hexBoolConvert(self.__sendCommandAndValue(b'\xe2', suffix))

    def setSensorThreshold(self, suffix):
        return self.__hexBoolConvert(self.__sendCommandAndValue(b'\xf1', suffix, 2))
