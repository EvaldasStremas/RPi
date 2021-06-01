import RPi.GPIO as GPIO


class Led:
    def __init__(self, led_light_state, led_press_state, keyboard_expected_input, keyboard_pressed_key, led_pin):
        self.led_light_state = led_light_state
        self.led_press_state = led_press_state
        self.keyboard_input = keyboard_expected_input
        self.keyboard_pressed_key = keyboard_pressed_key
        self.led_pin = led_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led_pin, GPIO.OUT)

    def setLedOutputHigh(self, led_pin):
        GPIO.output(led_pin, GPIO.HIGH)
        self.led_light_state = 100
        self.led_press_state = 1

    def setLedOutputLow(self, led_pin):
        GPIO.output(led_pin, GPIO.LOW)
        self.led_light_state = 0
        self.led_press_state = 0

    def printAll(self, led_light_state, led_press_state, keyboard_expected_input, keyboard_pressed_key, led_pin):
        print(led_light_state, led_press_state, keyboard_expected_input, keyboard_pressed_key, led_pin)

    def simpleLedSwitch(self, keyboard_input, keyboard_pressed_key, led_press_state):
        if keyboard_input == keyboard_pressed_key:
            if led_press_state == 0:
                self.setLedOutputHigh(self.led_pin)
            elif led_press_state == 1:
                self.setLedOutputLow(self.led_pin)

    def setNewKeyboardKey(self, new_keyboard_key):
        self.keyboard_pressed_key = new_keyboard_key

    def getLedsStatus(self, keyboard_pressed_key):
        if keyboard_pressed_key == 's':
            print("leds data")


    
            
# led1 = Led('1', 0, 'g', 'g', 13)

# led1.simpleLedSwitch(led1.keyboard_input, led1.keyboard_pressed_key, led1.led_press_state)
# led1.printAll(led1.led_light_state, led1.led_press_state, led1.keyboard_input, led1.keyboard_pressed_key, led1.led_pin)

# time.sleep(1)

# led1.simpleLedSwitch(led1.keyboard_input, led1.keyboard_pressed_key, led1.led_press_state)
# led1.printAll(led1.led_light_state, led1.led_press_state, led1.keyboard_input, led1.keyboard_pressed_key, led1.led_pin)





# time.sleep(1)
# led1.setLedOutputHigh(led1.led_pin)
# print(led1.led_light_state)
# time.sleep(1)
# led1.setLedOutputLow(led1.led_pin)
# print(led1.led_light_state)
# time.sleep(1)
# led1.setLedOutputHigh(led1.led_pin)
# print(led1.led_light_state)
# time.sleep(1)
# led1.setLedOutputLow(led1.led_pin)
# print(led1.led_light_state)


# led1.toggleOnOffLed(led1.keyboard_input, led1.keyboard_key)

# led1.setStateOff()
# print(led1.led_state, led1.led_press_state ,led1.keyboard_input, led1.keyboard_key, led1.led_pin)