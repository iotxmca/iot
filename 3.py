import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)

while True:
        print("LED ON")
        GPIO.output(8,GPIO.HIGH)
        time.sleep(2)
        print("LED OFF")
        GPIO.output(8,GPIO.LOW)
        time.sleep(1)
