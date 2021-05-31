import asyncio, telnetlib3
import RPi.GPIO as GPIO
from functions import setPwmLedControl, toggleOnOffLed

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

dc = 50 # duty cycle (0-100) for PWM pin
pwm = GPIO.PWM(26, 50)  # Initialize PWM on pwmPin 100Hz frequency
pwm.start(dc)

@asyncio.coroutine
def shell(reader, writer):

    writer.write('\r\n*RPI LED CONTROL*')

    pwmValue = 0

    while True:

        inp = yield from reader.read(1)

        toggleOnOffLed(inp, ledPin=13, keyboardKey='1')
        toggleOnOffLed(inp, ledPin=19, keyboardKey='2')


        pwmValue = setPwmLedControl(inp, pwmValue, pwm)
        print(pwmValue)
        writer.write('\r\n' + str(pwmValue) + '\r')

        if inp == '+':
            break

    if inp:
        writer.echo(inp)
        writer.write('\r\n*Program closed*\r\n')
        yield from writer.drain()
    writer.close()

loop = asyncio.get_event_loop()
coro = telnetlib3.create_server(port=7777, shell=shell)
server = loop.run_until_complete(coro)
loop.run_until_complete(server.wait_closed())