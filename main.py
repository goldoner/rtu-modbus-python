import easymodbus.modbusClient
import serial

import logging

logging.basicConfig(filename="modbusPython.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


modbus_client = easymodbus.modbusClient.ModbusClient('/dev/ttyUSB0')

modbus_client.baudrate = 9600
modbus_client.parity = serial.PARITY_NONE
modbus_client.stopbits = 8
modbus_client.stopbits = 2

modbus_client.is_connected()

modbus_client.connect()
register_values = modbus_client.read_holdingregisters(4001, 1)

print("Value of Register #1:" + str(register_values[0]))

logging.info("Current REGISTER 4000 : " + modbus_client.read_holdingregisters(4001, 1)[0])
logging.info("Voltage N-L REGISTER 4003 : " + modbus_client.read_holdingregisters(4004, 1)[0])
logging.info("Voltage L-L REGISTER 4006 : " + modbus_client.read_holdingregisters(4007, 1)[0])
logging.info("Real power REGISTER 4009 : " + modbus_client.read_holdingregisters(4010, 1)[0])

logging.info("Apparent power REGISTER 4012 : " + modbus_client.read_holdingregisters(4013, 1)[0])
logging.info("Reactive power REGISTER 4015 : " + modbus_client.read_holdingregisters(4016, 1)[0])
logging.info("cos(phi) REGISTER 4018 : " + modbus_client.read_holdingregisters(4019, 1)[0])
logging.info("Frequency REGISTER 4021 : " + modbus_client.read_holdingregisters(4022, 1)[0])

logging.info("Real power, Sum REGISTER 4024 : " + modbus_client.read_holdingregisters(4025, 1)[0])
logging.info("Real power EMAX REGISTER 4156 : " + modbus_client.read_holdingregisters(4157, 1)[0])
logging.info("Apparent power, Sum REGISTER 4025 : " + modbus_client.read_holdingregisters(4026, 1)[0])
logging.info("Reactive power, Sum REGISTER 4026 : " + modbus_client.read_holdingregisters(4027, 1)[0])
logging.info("cos(phi), Sum REGISTER 4027 : " + modbus_client.read_holdingregisters(4028, 1)[0])
logging.info("Current, Sum REGISTER 4028 : " + modbus_client.read_holdingregisters(4029, 1)[0])

logging.info("Total harm dist factor _U REGISTER 4150 : " + modbus_client.read_holdingregisters(4151, 1)[0])
logging.info("Total harm dist factor _I REGISTER 4153 : " + modbus_client.read_holdingregisters(4154, 1)[0])

logging.info("Partial harmonic distortion _U REGISTER 4030 : " + modbus_client.read_holdingregisters(4031, 1)[0])
logging.info("Partial harmonic distortion _I REGISTER 4090 : " + modbus_client.read_holdingregisters(4091, 1)[0])


modbus_client.close()
