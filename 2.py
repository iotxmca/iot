import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led=4
buttonPin=17
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buttonPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
try:
  while True:
        GPIO.output(led,not GPIO.input(buttonPin))
        time.sleep(1)
finally:
    GPIO.cleanup()
