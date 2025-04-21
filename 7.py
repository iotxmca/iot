import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText

# Set your Gmail details here
EMAIL_ADDRESS = "iotxmca@gmail.com"
EMAIL_PASSWORD = "hezr rgch bffu ioyl"
TO_EMAIL = "amanxamn@gmail.com"

# Setup
GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

def send_email():
    msg = MIMEText("Intruder detected!")
    msg["Subject"] = "⚠️ Intruder Alert!"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Email sent!")
    except Exception as e:
        print("Failed to send email:", e)

print("Monitoring for intruders...")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Intruder detected!")
            send_email()
            time.sleep(10)  # wait 10 seconds before next detection
        time.sleep(1)
except KeyboardInterrupt:
    print("Program stopped")
finally:
    GPIO.cleanup()
