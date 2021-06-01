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

class PwmLed:
    def __init__(self, led_light_state, led_press_state, keyboard_pressed_key, pwm_up_key, pwm_down_key, led_pin):
        self.led_light_state = led_light_state
        self.led_press_state = led_press_state
        self.keyboard_pressed_key = keyboard_pressed_key
        self.pwm_up_key = pwm_up_key
        self.pwm_down_key = pwm_down_key
        self.led_pin = led_pin

    def risePwmLevel(self, pwm_up_key, keyboard_pressed_key):
        if pwm_up_key == keyboard_pressed_key:
            pass

    def downPwmLevel(self, pwm_down_key, keyboard_pressed_key):
        if pwm_down_key == keyboard_pressed_key:
            pass