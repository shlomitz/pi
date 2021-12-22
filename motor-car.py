import RPi.GPIO as GPIO  # import RPi.GPIO module
import time

forword_pin = 23
backwards_pin = 24

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
GPIO.setup(forword_pin, GPIO.OUT)  # set a port/pin as an output
GPIO.setup(backwards_pin, GPIO.OUT)
GPIO.output(forword_pin, 1)  # set port/pin value to 1/GPIO.HIGH/True
time.sleep(3)
GPIO.output(forword_pin, 0)
GPIO.output(backwards_pin, 1)
time.sleep(3)
GPIO.output(backwards_pin, 0)
