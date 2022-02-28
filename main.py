import easymodbus.modbusClient
import serial

import logging
import time

logging.basicConfig(filename="logFileTest.log",
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

logging.info("TIME/DATE REGISTER 3000 L1  : " + str(float(modbus_client.read_holdingregisters(3000, 3)[0])))

i = 0

while i < 360:
    logging.info("ITERATION START")

    try:
        logging.info("CURRENT REGISTER 8000-8002 (L1-L3)  : " + str((modbus_client.read_holdingregisters(8000, 3))))
        print(str((modbus_client.read_holdingregisters(8000, 3))))
    except:
        logging.info("REGISTER 8000-8002 (L1-L3) READ FAILED!")

    try:
        logging.info("CURRENT REGISTER 8157-8159 (L1-L3)  : " + str((modbus_client.read_holdingregisters(8157, 3))))
    except:
        logging.info("REGISTER 8157-8159 (L1-L3) READ FAILED!")

    try:
        logging.info("VOLTAGE REGISTER 8003-8005 (L1-L3)  : " + str((modbus_client.read_holdingregisters(8003, 3))))
    except:
        logging.info("REGISTER 8003-8005 (L1-L3) READ FAILED!")

    try:
        logging.info("VOLTAGE REGISTER 8160-8162 (L1-L3)   : " + str((modbus_client.read_holdingregisters(8160, 3))))
    except:
        logging.info("REGISTER 8160-8162 (L1-L3) READ FAILED!")

    try:
        logging.info("REAL POWER REGISTER 8009-8011 (L1-L3)   : " + str((modbus_client.read_holdingregisters(8009, 3))))
    except:
        logging.info("REGISTER 8009-8011 (L1-L3) READ FAILED!")

    try:
        logging.info("REAL POWER REGISTER 8166-8168 (L1-L3)   : " + str((modbus_client.read_holdingregisters(8166, 3))))
    except:
        logging.info("REGISTER 8166-8168 (L1-L3) READ FAILED!")

    try:
        logging.info(
            "REACTIVE POWER REGISTER 8015-8017 (L1-L3)   : " + str((modbus_client.read_holdingregisters(8015, 3))))
    except:
        logging.info("REGISTER 8015-8017  (L1-L3) READ FAILED!")

    try:
        logging.info(
            "REACTIVE POWER REGISTER 8172-8175 (L1-L3)   : " + str((modbus_client.read_holdingregisters(8172, 3))))
    except:
        logging.info("REGISTER 8172-8175 (L1-L3) READ FAILED!")

    try:
        logging.info("REAL WORK CONSUMPTION REGISTER 9000  : " + str((modbus_client.read_holdingregisters(9000, 1))))
    except:
        logging.info("REGISTER 9000 READ FAILED!")

    try:
        logging.info("REAL WORK SUPPLY REGISTER 9001  : " + str((modbus_client.read_holdingregisters(9001, 1))))
    except:
        logging.info("REGISTER 9001 READ FAILED!")

    try:
        logging.info("REACTIVE WORK CAPACITIVE REGISTER 9003  : " + str((modbus_client.read_holdingregisters(9003, 1))))
    except:
        logging.info("REGISTER 9003 READ FAILED!")

    try:
        logging.info("REACTIVE WORK INDUCTIVE REGISTER 9004  : " + str((modbus_client.read_holdingregisters(9004, 1))))
    except:
        logging.info("REGISTER 9004 READ FAILED!")

    logging.info("ITERATION END")
    logging.info(" ")
    logging.info(" ")
    logging.info(" ")

    i += 1
    time.sleep(5)

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
