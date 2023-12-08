import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

# Definiere die GPIO-Pins für die LEDs
led_pins = [17, 27, 22, 23, 24, 6, 12, 13, 16, 20,]

# Definiere den GPIO-Pin für den Knopf
button_pin = 18

# Konfiguriere die GPIO-Pins
GPIO.setup(led_pins, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

# Funktion zum Aktivieren des Wasserlichts
def activate_water_light(channel):
    for led_pin in led_pins:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(led_pin, GPIO.LOW)

# Weise die Funktion dem Knopfdruck-Ereignis zu
GPIO.add_event_detect(button_pin, GPIO.RISING, callback=activate_water_light, bouncetime=200)

try:
    # Warte auf das Programmende
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # Bei Abbruch durch den Benutzer GPIO aufräumen
    GPIO.cleanup()