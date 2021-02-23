import RPi.GPIO as GPIO
import time


laser_out = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(laser_out, GPIO.OUT)

try:
    while True:
        GPIO.output(laser_out, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(laser_out, GPIO.LOW)
        time.sleep(2)
# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting")