import asyncio, telnetlib3
import RPi.GPIO as GPIO
from functions import Led, PwmLed

#############################
#1: led output status(0/100)
#2: led press state (0/1)
#3: keyboard expected input
#4: keyboard pressed input
#5: led pin
#############################

led1 = Led('0', 0, '1', '0', 26)
led2 = Led('0', 0, '2', '0', 13)

#############################
#1: led output status(0/100)
#3: keyboard pressed key
#4: pwm up key
#5  pwm down key
#6: led pin
#############################

led3 = PwmLed(0, 19)

# pwm_value = 0

@asyncio.coroutine
def shell(reader, writer):

    writer.write('\r\n*RPI LED CONTROL*')

    while True:

        keyboardInput = yield from reader.read(1)

        led1.setNewKeyboardKey(keyboardInput)
        led1.simpleLedSwitch(led1.keyboard_input, led1.keyboard_pressed_key, led1.led_press_state)
        # led1.printAll(led1.led_light_state, led1.led_press_state, led1.keyboard_input, led1.keyboard_pressed_key, led1.led_pin)

        led2.setNewKeyboardKey(keyboardInput)
        led2.simpleLedSwitch(led2.keyboard_input, led2.keyboard_pressed_key, led2.led_press_state)
        # led2.printAll(led2.led_light_state, led2.led_press_state, led2.keyboard_input, led2.keyboard_pressed_key, led2.led_pin)

        # led1.getLedsStatus(led1.keyboard_pressed_key)

        #SIMPLE LED

        if keyboardInput == 'y':
            
            print(led1.getLedOutputStatus())
            print(led2.getLedOutputStatus())
            print(led3.getPwmLedOutputStatus())
            writer.write('\r\n' + str(led1.getLedOutputStatus()) + '\r')
            writer.write('\r\n' + str(led2.getLedOutputStatus()) + '\r')
            writer.write('\r\n' + str(led3.getPwmLedOutputStatus()) + '\r')

        #PWM LED

        if keyboardInput == '9':
            pwmlvl = led3.setPwmRiseFive()
            print(pwmlvl)

        if keyboardInput == '6':
            pwmlvl = led3.setPwmDropFive()
            print(pwmlvl)

        if keyboardInput == 'get_statistic':
            led3.getPwmStatistic()

        #EXIT

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