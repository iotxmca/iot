import RPi.GPIO as GPIO
from flask import Flask, render_template
led_pin = 15
app = Flask( name )
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led_pin, GPIO.OUT, initial=0)
@app.route('/')
def index():
return render_template('index.html')
@app.route('/ledon')
def ledon():
GPIO.output(led_pin, GPIO.HIGH)
return render_template('index.html')
@app.route('/ledoff')
def ledoff():
GPIO.output(led_pin, GPIO.LOW)
return render_template('index.html')
if name == " main ":
app.run(debug=False, port=4000, host='0.0.0.0')
