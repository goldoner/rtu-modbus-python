import encodings

import easymodbus.modbusClient
import serial

import logging

logging.basicConfig(filename="modbusPython.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

modbus_client = easymodbus.modbusClient.ModbusClient('/dev/ttyUSB0')

# 9600/8/N/2
modbus_client.baudrate = 9600
modbus_client.parity = serial.PARITY_NONE
modbus_client.stopbits = serial.STOPBITS_ONE

modbus_client.is_connected()

modbus_client.connect()
#
# logging.info(type(modbus_client.read_holdingregisters(4001, 3)[0]))
#
# logging.info("Current REGISTER 1000 : " + str(
#     easymodbus.modbusClient.convert_registers_to_float(modbus_client.read_holdingregisters(1000, 3))))
#
#
# logging.info("Current REGISTER 8000 L1 : " + str(float(modbus_client.read_holdingregisters(8000, 3)[0] / 10)))
# logging.info("Current REGISTER 8001 L2 : " + str(float(modbus_client.read_holdingregisters(8000, 3)[1] / 10)))
# logging.info("Current REGISTER 8002 L3 : " + str(float(modbus_client.read_holdingregisters(8000, 3)[2] / 10)))
#
#
# logging.info("Voltage REGISTER 8003 L1 : " + str(float(modbus_client.read_holdingregisters(8003, 3)[0] / 10)))
# logging.info("Voltage REGISTER 8003 L2 : " + str(float(modbus_client.read_holdingregisters(8003, 3)[1] / 10)))
# logging.info("Voltage REGISTER 8003 L3 : " + str(float(modbus_client.read_holdingregisters(8003, 3)[2] / 10)))
#
#
# logging.info("Real Power SUM REGISTER 8024 : " + str(float(modbus_client.read_holdingregisters(8024, 3)[0] / 10)))
#
# logging.info("Real Power REGISTER 8009 L1 : " + str(float(modbus_client.read_holdingregisters(8009, 3)[0] / 10)))
# logging.info("Real Power REGISTER 8009 L2 : " + str(float(modbus_client.read_holdingregisters(8009, 3)[1] / 10)))
# logging.info("Real Power REGISTER 8009 L3 : " + str(float(modbus_client.read_holdingregisters(8009, 3)[2] / 10)))
#
#
# logging.info("Apparent Power REGISTER 8012 L1 : " + str(float(modbus_client.read_holdingregisters(8012, 3)[0] / 10)))
# logging.info("Apparent Power REGISTER 8012 L2 : " + str(float(modbus_client.read_holdingregisters(8012, 3)[1] / 10)))
# logging.info("Apparent Power REGISTER 8012 L3 : " + str(float(modbus_client.read_holdingregisters(8012, 3)[2] / 10)))
#
#
# logging.info("Reactive Power REGISTER 8015 L1 : " + str(float(modbus_client.read_holdingregisters(8015, 3)[0] / 10)))
# logging.info("Reactive Power REGISTER 8015 L2 : " + str(float(modbus_client.read_holdingregisters(8015, 3)[1] / 10)))
# logging.info("Reactive Power REGISTER 8015 L3 : " + str(float(modbus_client.read_holdingregisters(8015, 3)[2] / 10)))

logging.info(str.encode(str(modbus_client.read_holdingregisters(3001, 1)[0])))

logging.info("Voltage REGISTER 9100 SCALE : " + str(modbus_client.read_holdingregisters(9100, 1)))
logging.info("Voltage REGISTER 9101 SCALE : " + str(modbus_client.read_holdingregisters(9101, 1)))

logging.info("System Time REGISTER 3000 SCALE : " + str(modbus_client.read_holdingregisters(3001, 1)[0]))
logging.info("AVG Time Current REGISTER 3001 SCALE : " + str(modbus_client.read_holdingregisters(3002, 6)[0]))

# logging.info("Current REGISTER 4000 : " + str(modbus_client.read_holdingregisters(4001, 3)[1]))
# logging.info("Current REGISTER 4000 : " + str(modbus_client.read_holdingregisters(4001, 3)[2]))
#
# logging.info("Voltage N-L REGISTER 4003 : " + str(modbus_client.read_holdingregisters(4004, 1)[0]))
# logging.info("Voltage L-L REGISTER 4006 : " + str(modbus_client.read_holdingregisters(4007, 1)[0]))
# logging.info("Real power REGISTER 4009 : " + str(modbus_client.read_holdingregisters(4010, 1)[0]))
#
# logging.info("Apparent power REGISTER 4012 : " + str(modbus_client.read_holdingregisters(4013, 1)[0]))
# logging.info("Reactive power REGISTER 4015 : " + str(modbus_client.read_holdingregisters(4016, 1)[0]))
# logging.info("cos(phi) REGISTER 4018 : " + str(modbus_client.read_holdingregisters(4019, 1)[0]))
# logging.info("Frequency REGISTER 4021 : " + str(modbus_client.read_holdingregisters(4022, 1)[0]))
#
# logging.info("Real power, Sum REGISTER 4024 : " + str(modbus_client.read_holdingregisters(4025, 1)[0]))
# logging.info("Real power EMAX REGISTER 4156 : " + str(modbus_client.read_holdingregisters(4157, 1)[0]))
# logging.info("Apparent power, Sum REGISTER 4025 : " + str(modbus_client.read_holdingregisters(4026, 1)[0]))
# logging.info("Reactive power, Sum REGISTER 4026 : " + str(modbus_client.read_holdingregisters(4027, 1)[0]))
# logging.info("cos(phi), Sum REGISTER 4027 : " + str(modbus_client.read_holdingregisters(4028, 1)[0]))
# logging.info("Current, Sum REGISTER 4028 : " + str(modbus_client.read_holdingregisters(4029, 1)[0]))
#
# logging.info("Total harm dist factor _U REGISTER 4150 : " + str(modbus_client.read_holdingregisters(4151, 1)[0]))
# logging.info("Total harm dist factor _I REGISTER 4153 : " + str(modbus_client.read_holdingregisters(4154, 1)[0]))
#
# logging.info("Partial harmonic distortion _U REGISTER 4030 : " + str(modbus_client.read_holdingregisters(4031, 1)[0]))
# logging.info("Partial harmonic distortion _I REGISTER 4090 : " + str(modbus_client.read_holdingregisters(4091, 1)[0]))

modbus_client.close()
