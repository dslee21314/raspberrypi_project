import RPi.GPIO as GPIO
from time import sleep

outPin = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(outPin, GPIO.OUT)

p = GPIO.PWM(outPin, 50)
p.start(0)
try:
    while True:
        for dc in range(0,101,5):
            p.ChangeDutyCycle(dc)
            sleep(0.1)
        for dc in range(100,-1,-5):
            p.ChangeDutyCycle(dc)
            sleep(0.1)
except KeyboardInterrupt:
    print("exit!!")
    pass
p.stop()
GPIO.cleanup()
