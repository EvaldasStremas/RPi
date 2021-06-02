import serial
import time

ser = serial.Serial(
        port='COM5',
        baudrate=19200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

# print(ser.is_open)
# mystring = "AT\r"
# mystring = "ATD503\r"
# mystring = "y\r"
# inbytes = bytes(mystring, 'utf-8')

# ser.open()

# ser.write(b'ATD503\r')
# ser.write(b'y\r')



ser.write(b'ATD503\r')
s = ser.read(500) # read up to one hundred bytes
print(s)
# data = ser.readline()
# print(data)

time.sleep(5)

ser.write(b'1\r')
s = ser.read(500) # read up to one hundred bytes
print(s)

time.sleep(1)

ser.write(b'1\r')
# s = ser.read(500) # read up to one hundred bytes
# print(s)

time.sleep(1)

ser.write(b'1\r')
# s = ser.read(500) # read up to one hundred bytes
# print(s)

# data = ser.readline()
# print(data)

ser.write(b'+\r')
# s = ser.read(500) # read up to one hundred bytes
# print(s)
# data = ser.readline()
# print(data)

ser.close()
