
import minimalmodbus

rs232 = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
rs232.serial.baudrate = 600
rs232.serial.bytesize = 8
rs232.serial.parity = minimalmodbus.serial.PARITY_NONE
rs232.serial.stopbits = 2
rs232.serial.timeout = 1
rs232.debug = False
rs232.mode = minimalmodbus.MODE_RTU
print(rs232.serial.is_open)
print(rs232)

HV_A_Phase_Spannung = rs232.read_float(0, functioncode=4, number_of_registers=2)
print(str(f'{HV_A_Phase_Spannung :.2f}') + "V -Phase A")
