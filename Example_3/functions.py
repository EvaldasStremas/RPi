import RPi.GPIO as GPIO

led_press_state = 0

def toggleOnOffLed(inp, ledPin, keyboardKey):
    global led_press_state

    if inp == keyboardKey:
        if led_press_state == 0:
            GPIO.output(ledPin, GPIO.HIGH)
            print("led: on")
            # writer.write('\r\n"led: on"\r')
            led1_press_state = 1

        elif led_press_state == 1:
            GPIO.output(ledPin, GPIO.LOW)
            print("led: off")
            # writer.write('\r\n"led: off"\r')
            led1_press_state = 0

    return led1_press_state

def setPwmLedControl(inp, pwmValue, pwm):
    if inp == '6':
        pwmValue += 5
        if pwmValue > 100:
            # print("Cannot be higher than 100")
            # writer.write('\r\n"Cannot be higher than 100"\r')
            pwmValue = 100
        else: 
            pwm.ChangeDutyCycle(pwmValue)
            # print("3 led PWM:", pwmValue)
            # writer.write('\r\n3 led pwm: ' + str(p) + '\r')

    elif inp == '3':
        pwmValue -= 5

        if pwmValue < 0:
            print("Cannot be lower than 0")
            # writer.write('\r\n"Cannot be lower than 0"\r')
            pwmValue = 0
        else: 
            pwm.ChangeDutyCycle(pwmValue)
            # print("3 led PWM:", pwmValue)
            # writer.write('\r\n3 led pwm: ' + str(p) + '\r')
    
    return pwmValue