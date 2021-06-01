import asyncio, telnetlib3
import RPi.GPIO as GPIO
from functions import Led

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

Led = Led()

@asyncio.coroutine
def shell(reader, writer):

    writer.write('\r\n*RPI LED CONTROL*')

    while True:

        keyboardInput = yield from reader.read(1)

        Led.toggleOnOffLed(keyboardInput, ledPin=13, keyboardKey='1', led_number=0)
        Led.toggleOnOffLed(keyboardInput, ledPin=19, keyboardKey='2', led_number=1)
        Led.setPwmLedControl(keyboardInput, pwmUpKey='6', pwmDownKey='3', led_number=2)
        Led.getLedsState(keyboardInput)

        if keyboardInput == '+':
            break

    if keyboardInput:
        writer.echo(keyboardInput)
        writer.write('\r\n*Program closed*\r\n')
        yield from writer.drain()
    writer.close()

loop = asyncio.get_event_loop()
coro = telnetlib3.create_server(port=7777, shell=shell)
server = loop.run_until_complete(coro)
loop.run_until_complete(server.wait_closed())