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

ser.write(b'AT\r')
ser.write(b'ATD503\r')
s = ser.read(500) # read up to one hundred bytes
print(s)

time.sleep(5)

while True:
    keyboardInput = input("Enter key: ")

    if keyboardInput == 'x':
        break

    keyboardInput = keyboardInput + '\r'
    keyboardInputInBytes = bytes(keyboardInput, 'utf-8')
    print(keyboardInputInBytes)
    ser.write(keyboardInputInBytes)

    s = ser.read(500) # read up to one hundred bytes
    print(s)

ser.close()