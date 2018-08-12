import time

from flask import Flask
import RPi.GPIO as GPIO

#
# Variables used for the Flask framework.
#

app = Flask(__name__)

#
# Variables used to control the GPIO pins.
#

GPIO_SIGNAL_PIN = 12
# left
#DUTY_CYCLE_ON = 5.5
#DUTY_CYCLE_OFF = 10

# right
DUTY_CYCLE_ON = 10
DUTY_CYCLE_OFF = 5.5
pwm = None

#
# Variables used for controlling the light.
#

lightsOn = False

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/on')
def turn_on():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_SIGNAL_PIN, GPIO.OUT)
    pwm = GPIO.PWM(GPIO_SIGNAL_PIN, 50)
    pwm.start(DUTY_CYCLE_ON)
    pwm.ChangeDutyCycle(DUTY_CYCLE_ON)
    time.sleep(0.5)
    pwm.stop()
    GPIO.cleanup()
    return 'Turned on!'

@app.route('/off')
def turn_off():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_SIGNAL_PIN, GPIO.OUT)
    pwm = GPIO.PWM(GPIO_SIGNAL_PIN, 50)
    pwm.start(DUTY_CYCLE_OFF)
    pwm.ChangeDutyCycle(DUTY_CYCLE_OFF)
    time.sleep(0.5)
    pwm.stop()
    GPIO.cleanup()
    return 'Turned off!'

@app.route('/cleanup')
def cleanup():
    GPIO.cleanup()
    return 'Cleaned up!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
