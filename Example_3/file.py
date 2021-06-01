import asyncio, telnetlib3
import RPi.GPIO as GPIO
from functions import Led

led1 = Led('1', 0, '1', '0', 26)
led2 = Led('1', 0, '2', '0', 13)

@asyncio.coroutine
def shell(reader, writer):

    writer.write('\r\n*RPI LED CONTROL*')

    while True:

        keyboardInput = yield from reader.read(1)

        led1.setNewKeyboardKey(keyboardInput)
        led1.simpleLedSwitch(led1.keyboard_input, led1.keyboard_pressed_key, led1.led_press_state)
        led1.printAll(led1.led_light_state, led1.led_press_state, led1.keyboard_input, led1.keyboard_pressed_key, led1.led_pin)

        led2.setNewKeyboardKey(keyboardInput)
        led2.simpleLedSwitch(led2.keyboard_input, led2.keyboard_pressed_key, led2.led_press_state)
        led2.printAll(led2.led_light_state, led2.led_press_state, led2.keyboard_input, led2.keyboard_pressed_key, led2.led_pin)

        led1.getLedsStatus(led1.keyboard_pressed_key)

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