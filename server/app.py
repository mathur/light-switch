import time

from flask import Flask, make_response, jsonify, abort
import RPi.GPIO as GPIO

from config import *

app = Flask(__name__)
pwm = None

#
# Variables used for controlling the light.
#

lightsOn = False

@app.route('/status')
def status():
    return make_response(jsonify({'lights_on': lightsOn}), 200)

@app.route('/on')
def turn_on():
    global pwm
    global lightsOn

    if lightsOn:
        abort(400)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_SIGNAL_PIN, GPIO.OUT)

    pwm = GPIO.PWM(GPIO_SIGNAL_PIN, FREQUENCY)
    pwm.start(DUTY_CYCLE_ON)
    pwm.ChangeDutyCycle(DUTY_CYCLE_ON)
    time.sleep(DELAY_BETWEEN_REQUESTS)
    pwm.stop()

    GPIO.cleanup()

    lightsOn = True

    return make_response(jsonify({'lights_on': lightsOn}), 200)

@app.route('/off')
def turn_off():
    global pwm
    global lightsOn

    if not lightsOn:
        abort(400)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_SIGNAL_PIN, GPIO.OUT)

    pwm = GPIO.PWM(GPIO_SIGNAL_PIN, FREQUENCY)
    pwm.start(DUTY_CYCLE_OFF)
    pwm.ChangeDutyCycle(DUTY_CYCLE_OFF)
    time.sleep(DELAY_BETWEEN_REQUESTS)
    pwm.stop()

    GPIO.cleanup()

    lightsOn = False

    return make_response(jsonify({'lights_on': lightsOn}), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
