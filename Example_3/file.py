import asyncio, telnetlib3
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

dc = 50 # duty cycle (0-100) for PWM pin
pwm = GPIO.PWM(26, 50)  # Initialize PWM on pwmPin 100Hz frequency
pwm.start(dc)

@asyncio.coroutine
def shell(reader, writer):

    writer.write('\r\nWould you like to play a game? ')

    led1_press_state = 0
    p = 20

    while True:

        inp = yield from reader.read(1)

        if inp == '1':
            if led1_press_state == 0:
                GPIO.output(13, GPIO.HIGH)
                print("1 led: on")
                led1_press_state = 1

            elif led1_press_state == 1:
                GPIO.output(13, GPIO.LOW)
                print("1 led: off")
                led1_press_state = 0

        if inp == '5':
            GPIO.output(19, GPIO.HIGH)
            print("2 led: on")

        elif inp == '2':
            GPIO.output(19, GPIO.LOW)
            print("2 led: off")

        elif inp == '6':
            p += 5
            if p > 100:
                print("Cannot be higher than 100")
                p = 100
            else: 
                pwm.ChangeDutyCycle(p)
                print("3 led: pwm",p)

        elif inp == '3':
            p -= 5

            if p < 0:
                print("Cannot be lower than 0")
                p = 0
            else: 
                pwm.ChangeDutyCycle(p)
                print("3 led: pwm",p)

        elif inp == '+':
            break

    if inp:
        writer.echo(inp)
        writer.write('\r\nThey say the only way to win '
                    'is to not play at all.\r\n')
        yield from writer.drain()
    writer.close()

loop = asyncio.get_event_loop()
coro = telnetlib3.create_server(port=7777, shell=shell)
server = loop.run_until_complete(coro)
loop.run_until_complete(server.wait_closed())