# RPi GPIO
import RPi.GPIO as GPIO
# Flask dependencies
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
rpi_api = Api(app)
GPIO.setmode(GPIO.BCM)


def str2bool(v):
	return v.lower() in ("true", "1")


@app.route('/gpio/led/<int:gpioPin>/<string:status>', methods=['POST'])
def setPinLevel(gpioPin, status):
	GPIO.setup(gpioPin, GPIO.OUT)
	GPIO.output(gpioPin, str2bool(status))
	return {'status': "OK"}


@app.route('/status')
def get():
	return {'status': 'OK'}


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
