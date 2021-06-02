import serial.tools.list_ports
import time

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVal = "COM" + str(val)
        print(portList[x])

serialInst.baudrate = 19200
serialInst.port = portVal
serialInst.open()

while True:
    if serialInst.in_waiting:

        # serialInst.write('AT\r')
        # serialInst.write('ATD503\r')

        packet = serialInst.readline()
        print(packet.decode('utf'))