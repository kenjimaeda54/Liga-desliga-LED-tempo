import RPi.GPIO as GPIO
import time

LED = 24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

while True:
 GPIO.output(LED,1)
 time.sleep (0.5)
 GPIO.output(LED,0)
 time.sleep (0.5)