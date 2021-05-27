import serial
import time

ser = serial.Serial(
        port='COM5',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while True:
        print(ser.is_open)
        mystring = "AT\r"
        inbytes = bytes(mystring, 'utf-8')
        ser.write(inbytes)

        data = ser.readline()
        print(data)

        time.sleep(1)