from time import sleep

import easymodbus.modbusClient
import serial

# ser = serial.Serial('/dev/ttyUSB0')  # open serial port
# print(ser.name)

seri = serial.Serial()
seri.baudrate = 9600
seri.port = '/dev/ttyUSB0'
seri.parity = serial.PARITY_NONE
seri.stopbits = 1

if seri.isOpen():
    seri.close()
seri.open()
print(seri.is_open)
print(seri.is_open)
print(seri.is_open)


print(seri.readlines())
sleep(2)
print(seri.readlines())
sleep(2)
print(seri.readlines())
sleep(2)
print(seri.readlines())

modbus_client = easymodbus.modbusClient.ModbusClient('/dev/ttyUSB0')
#modbus_client = easymodbus.modbusClient.ModbusClient('/dev/ttyUSB0', seri)

modbus_client.is_connected()

# 3600 36.6 25.5

modbus_client.connect()
#
# System.out.println("V1 L1: " + (float)
# modbusClient.ReadHoldingRegisters(3530, 1)[0] / 10);
#
# The first argument is the starting registers, the second argument is the quantity.
register_values = modbus_client.read_holdingregisters(4001, 1)

print("Value of Register #1:" + str(register_values[0]))

#
# input_registers = modbus_client.read_inputregisters(0, 10)	#Read input registers 1 to 10 from server
# holding_registers = modbus_client.read_holdingregisters(0, 5)	#Read holding registers 1 to 5 from server

modbus_client.close()
