import easymodbus.modbusClient

modbus_client = easymodbus.modbusClient.ModbusClient('/dev/tty.usbserial-14120')
modbus_client.baudrate = 600

# 3600 36.6 25.5

modbus_client.connect()
#
# System.out.println("V1 L1: " + (float)
# modbusClient.ReadHoldingRegisters(3530, 1)[0] / 10);
#
#The first argument is the starting registers, the second argument is the quantity.
register_values = modbus_client.read_holdingregisters(4000, 1)

print("Value of Register #1:" + str(register_values[0]))

#
# input_registers = modbus_client.read_inputregisters(0, 10)	#Read input registers 1 to 10 from server
# holding_registers = modbus_client.read_holdingregisters(0, 5)	#Read holding registers 1 to 5 from server

modbus_client.close()