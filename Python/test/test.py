import asyncio
import serial.tools.list_ports

from Python.core.controlunit.connection import Connector

ports_found = serial.tools.list_ports.comports()
ports = {}


async def __poll_control_units():
    print('polling')

    def add_port(port):
        print('adding')
        con: Connector = Connector(port.device)
        asyncio.sleep(2)

        type = con.readSensorType()
        print('type')
        print(type)
        if type is not None:
            ports[port.device] = (con, port.serial_number)
            print("Port {} successfully verified as {} with id {} \n".format(port.device, type, port.serial_number))
            print('maxDistance')
            print(con.readMinDistance())
            print('min distance')
            print(con.readMaxDistance())

    for port in ports_found:
        if port.device not in ports.keys():
            add_port(port)
        elif ports[port.device][1] != port.serial_number:
            ports[port.device][0].close()
            add_port(port)


async def test():
    await __poll_control_units()
