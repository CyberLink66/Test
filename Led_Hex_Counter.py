import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin1 = 18
pin2 = 19
x = False
y = 0

LOW = GPIO.LOW
HIGH = GPIO.HIGH

GPIO.setup(pin1, GPIO.IN)
GPIO.setup(pin2, GPIO.OUT)

def turnon():
    GPIO.output(pin2, HIGH)
    print(f"Status: {y} / {x}")

def turnoff():
    GPIO.output(pin2, LOW)
    print(f"Status {y} / {x}")

try:
    while True:
        y = GPIO.input(pin1)

        if y == 1 and not x:
            x = True
            turnon()
            time.sleep(0.2)

        elif y == 1 and x:
            x = False
            turnoff()
            time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()