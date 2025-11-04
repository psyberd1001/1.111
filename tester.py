import pymodbus
from pymodbus.client import ModbusSerialClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
from pymodbus.framer import ascii
import time
import logging
import sys
import glob
import serial
import serial.tools.list_ports

logging.basicConfig(filename='py_modbus.log', level=logging.DEBUG, filemode='w')
logging.debug('A DEBAG MESSAGE')

port_seek = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(port_seek):
    name_port = desc
    result_name_port = list(name_port)
    b = 0
    res = []
    for i in result_name_port:
        if b < 16:
            res.append(i)
            b += 1
    result_name_port1 = ''.join(res)
    if result_name_port1 == 'USB-SERIAL CH340':
        port_true = port
    else:
        print('Нет подходящих портов')



client = ModbusClient(framer='rtu', port=port_true, baudrate=9600, bytesize=8, parity='E', stopbits=1, timeout=1)
print(f'Мы подключились к порту! {port_true} - {client.connect()}')
connected = client.connect()
# time.sleep(3)
registr_reference = []
a = 0

def read_and_write_registr():
    global a
    if a >= 0:
        ref = client.read_holding_registers(address=4198, count=1, slave=5)
        registr_reference = ref.registers
        a += 1
        print(f'счётчик чтения {a}, значение регистра D519: {registr_reference}')
        time.sleep(0.01)
    print(registr_reference)
    return registr_reference

#read_and_write_registr()

client.close()