import RPi.GPIO as GPIO

led_list = [0, 0, 0]
led_press_state = 0
pwmValue = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

pwm = GPIO.PWM(26, 50) # Initialize PWM on pwmPin 100Hz frequency
pwm.start(pwmValue) # duty cycle (0-100) for PWM pin

class Led:
    def __init__(self):
        pass


    def toggleOnOffLed(self, keyboardInput, ledPin, keyboardKey, led_number):
        global led_press_state

        if keyboardInput == keyboardKey:
            if led_press_state == 0:
                GPIO.output(ledPin, GPIO.HIGH)
                print(ledPin, "led: on")
                led_list[led_number] = 100
                # writer.write('\r\n"led: on"\r')
                led_press_state = 1

            elif led_press_state == 1:
                GPIO.output(ledPin, GPIO.LOW)
                print(ledPin, "pin led: off")
                led_list[led_number] = 0
                # writer.write('\r\n"led: off"\r')
                led_press_state = 0

        return led_press_state


    def setPwmLedControl(self, keyboardInput, pwmUpKey, pwmDownKey, led_number):
        global pwmValue
    
        if keyboardInput == pwmUpKey:
            pwmValue += 5
            if pwmValue > 100:
                # print("Cannot be higher than 100")
                # writer.write('\r\n"Cannot be higher than 100"\r')
                pwmValue = 100
            else: 
                pwm.ChangeDutyCycle(pwmValue)
                led_list[led_number] = pwmValue
                # print("3 led PWM:", pwmValue)
                # writer.write('\r\n3 led pwm: ' + str(p) + '\r')

        elif keyboardInput == pwmDownKey:
            pwmValue -= 5

            if pwmValue < 0:
                # print("Cannot be lower than 0")
                # writer.write('\r\n"Cannot be lower than 0"\r')
                pwmValue = 0
            else: 
                pwm.ChangeDutyCycle(pwmValue)
                led_list[led_number] = pwmValue
                # print("3 led PWM:", pwmValue)
                # writer.write('\r\n3 led pwm: ' + str(p) + '\r')
        
        return pwmValue


    def getLedsState(self, keyboardInput):
        global led_press_state

        if 's' == keyboardInput:
            print(led_list)

        return None