import RPi.GPIO as GPIO
from time import sleep
relay_ch=21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_ch,GPIO.OUT)
try:
    while(True):
        print("Turning on .... ")
        GPIO.output(relay_ch,GPIO.HIGH)
        sleep(2)
        print("Turning off .... ")
        GPIO.output(relay_ch,GPIO.LOW)
        sleep(2)
finally:
    GPIO.cleanup()
