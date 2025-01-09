import RPi.GPIO as GPIO
from time import sleep

cont = 'y'

outPin = 11
numOfBlink = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(outPin, GPIO.OUT)

while True:
    GPIO.output(outPin, True)
    sleep(0.2)
    GPIO.output(outPin, False)
    sleep(0.2)
    GPIO.output(outPin, True)
    sleep(0.2)
    GPIO.output(outPin, False)
    sleep(0.2)
    GPIO.output(outPin, True)
    sleep(0.2)
    GPIO.output(outPin, False)
    sleep(0.5)
    
    GPIO.output(outPin, True)
    sleep(0.5)
    GPIO.output(outPin, False)
    sleep(0.5)
    GPIO.output(outPin, True)
    sleep(0.5)
    GPIO.output(outPin, False)
    sleep(0.5)
    GPIO.output(outPin, True)
    sleep(0.5)
    GPIO.output(outPin, False)
    sleep(0.5)
    
    GPIO.output(outPin, True)
    sleep(0.2)
    GPIO.output(outPin, False)
    sleep(0.2)
    GPIO.output(outPin, True)
    sleep(0.2)
    GPIO.output(outPin, False)
    sleep(0.2)
    GPIO.output(outPin, True)
    sleep(0.2)
    GPIO.output(outPin, False)
    sleep(1)
    
GPIO.cleanup()