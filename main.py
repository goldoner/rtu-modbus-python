import easymodbus.modbusClient
import serial

import logging

logging.basicConfig(filename="logFileTestlog",
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

logging.info("ITERATION START")

logging.info("CURRENT REGISTER 8000 L1  : " + str(float(modbus_client.read_holdingregisters(8000, 3)[0])))
logging.info("CURRENT REGISTER 8000 L2  : " + str(float(modbus_client.read_holdingregisters(8000, 3)[1])))
logging.info("CURRENT REGISTER 8000 L3  : " + str(float(modbus_client.read_holdingregisters(8000, 3)[2])))

logging.info("CURRENT REGISTER 8003 L1  : " + str(float(modbus_client.read_holdingregisters(8003, 3)[0])))
logging.info("CURRENT REGISTER 8003 L2  : " + str(float(modbus_client.read_holdingregisters(8003, 3)[1])))
logging.info("CURRENT REGISTER 8003 L3  : " + str(float(modbus_client.read_holdingregisters(8003, 3)[2])))

logging.info("CURRENT REGISTER 8157 L1 : " + str(float(modbus_client.read_holdingregisters(8157, 3)[0])))
logging.info("CURRENT REGISTER 8157 L2  : " + str(float(modbus_client.read_holdingregisters(8157, 3)[1])))
logging.info("CURRENT REGISTER 8157 L3  : " + str(float(modbus_client.read_holdingregisters(8157, 3)[2])))

logging.info("CURRENT REGISTER 8160 L1  : " + str(float(modbus_client.read_holdingregisters(8160, 3)[0])))
logging.info("CURRENT REGISTER 8160 L2  : " + str(float(modbus_client.read_holdingregisters(8160, 3)[1])))
logging.info("CURRENT REGISTER 8160 L3  : " + str(float(modbus_client.read_holdingregisters(8160, 3)[2])))

logging.info("REAL POWER REGISTER 8009 L1  : " + str(float(modbus_client.read_holdingregisters(8009, 3)[0])))
logging.info("REAL POWER REGISTER 8009 L2  : " + str(float(modbus_client.read_holdingregisters(8009, 3)[1])))
logging.info("REAL POWER REGISTER 8009 L3  : " + str(float(modbus_client.read_holdingregisters(8009, 3)[2])))

logging.info("REAL POWER REGISTER 8166 L1  : " + str(float(modbus_client.read_holdingregisters(8166, 3)[0])))
logging.info("REAL POWER REGISTER 8166 L2  : " + str(float(modbus_client.read_holdingregisters(8166, 3)[1])))
logging.info("REAL POWER REGISTER 8166 L3  : " + str(float(modbus_client.read_holdingregisters(8166, 3)[2])))

logging.info("REACTIVE POWER REGISTER 8015 L1  : " + str(float(modbus_client.read_holdingregisters(8015, 3)[0])))
logging.info("REACTIVE POWER REGISTER 8015 L2  : " + str(float(modbus_client.read_holdingregisters(8015, 3)[1])))
logging.info("REACTIVE POWER REGISTER 8015 L3  : " + str(float(modbus_client.read_holdingregisters(8015, 3)[2])))

logging.info("REACTIVE POWER REGISTER 8172 L1  : " + str(float(modbus_client.read_holdingregisters(8172, 3)[0])))
logging.info("REACTIVE POWER REGISTER 8172 L2  : " + str(float(modbus_client.read_holdingregisters(8172, 3)[1])))
logging.info("REACTIVE POWER REGISTER 8172 L3  : " + str(float(modbus_client.read_holdingregisters(8172, 3)[2])))

logging.info("REAL WORK CONSUMPTION REGISTER 9000  : " + str(float(modbus_client.read_holdingregisters(9000, 3)[0])))
logging.info("REAL WORK SUPPLY REGISTER 9001  : " + str(float(modbus_client.read_holdingregisters(9001, 3)[0])))

logging.info("REACTIVE WORK CAPACITIVE REGISTER 9003  : " + str(float(modbus_client.read_holdingregisters(9003, 3)[0])))
logging.info("REACTIVE WORK INDUCTIVE REGISTER 9004  : " + str(float(modbus_client.read_holdingregisters(9004, 3)[0])))

logging.info("ITERATION END")

# logging.info("Current REGISTER 1000 : " + str(
#     easymodbus.modbusClient.convert_registers_to_float(modbus_client.read_holdingregisters(1000, 3))))
#
#
# logging.info("Current REGISTER 8000 L1 : " + str(float(modbus_client.read_holdingregisters(8000, 3)[0] / 10)))
# logging.info("Current REGISTER 8001 L2 : " + str(float(modbus_client.read_holdingregisters(8000, 3)[1] / 10)))
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
#
#
#
# logging.info("Voltage REGISTER 9100 SCALE : " + str(modbus_client.read_holdingregisters(9100, 1)))
# logging.info("Voltage REGISTER 9101 SCALE : " + str(modbus_client.read_holdingregisters(9101, 1)))
#
# logging.info("System Time REGISTER 3000 SCALE : " + str(modbus_client.read_holdingregisters(3001, 1)[0]))
# logging.info("AVG Time Current REGISTER 3001 SCALE : " + str(modbus_client.read_holdingregisters(3002, 6)[0]))


modbus_client.close()
