import RPi.GPIO as GPIO


class Led:
    #1: led output status(0/100)
    #2: led press state (0/1)
    #3: keyboard expected input
    #4: keyboard pressed input
    #5: led pin

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
    
    def getLedOutputStatus(self):
        return self.led_light_state

    def printAll(self, led_light_state, led_press_state, keyboard_expected_input, keyboard_pressed_key, led_pin):
        print(' LED status: ', str(led_light_state), '\n',
        'LED press state: ', str(led_press_state), '\n',
        'Keyboard expexted input: ' + str(keyboard_expected_input) + '\n',
        'Keyboard pressed key: ' + str(keyboard_pressed_key) + '\n',
        'LED pin: ' + str(led_pin) + '\n')

    def simpleLedSwitch(self, keyboard_input, keyboard_pressed_key, led_press_state):
        if keyboard_input == keyboard_pressed_key:
            if led_press_state == 0:
                self.setLedOutputHigh(self.led_pin)
            elif led_press_state == 1:
                self.setLedOutputLow(self.led_pin)

    def setNewKeyboardKey(self, new_keyboard_key):
        self.keyboard_pressed_key = new_keyboard_key

    # def getLedsStatus(self, keyboard_pressed_key):
    #     if keyboard_pressed_key == 's':
    #         print("leds data")

class PwmLed:
    #1: led output status(0/100)
    #2: led press state (0/1)
    #3: keyboard pressed key
    #4: pwm up key
    #5  pwm down key
    #6: led pin

    def __init__(self, pwm_level, pwm_led_pin):
        self.pwm_level = pwm_level
        self.pwm_led_pin = pwm_led_pin

        global pwm
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pwm_led_pin, GPIO.OUT)
        pwm = GPIO.PWM(pwm_led_pin, 50)
        pwm.start(0)


    def setPwmRiseFive(self):
        self.pwm_level += 5
        pwm.ChangeDutyCycle(self.pwm_level)

        return self.pwm_level


    def setPwmDropFive(self):
        self.pwm_level -= 5
        pwm.ChangeDutyCycle(self.pwm_level)

        return self.pwm_level


    def getPwmLedOutputStatus(self):
        return self.pwm_level
    

    def getPwmStatistic(self):
        print('LED PWM duty cycle level: ', str(self.pwm_level), '\n',
        'LED pin number: ', str(self.pwm_led_pin), '\n')