import gpiozero 
from time import sleep

servo = gpiozero.Servo(17)

while True:
    print("min")
    servo.min()
    sleep(1)
    print("mid")
    servo.mid()
    sleep(1)
    print("max")
    servo.max()
    sleep(1)

servo.detach()