import numpy as np

# pi IP: 192.168.1.58
# RUN ssh pi@192.168.1.58

import RPi.GPIO as GPIO
from time import sleep

if __name__ == "__main__":
    in1 = 24
    in2 = 23
    en = 25
    temp1 = 1

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(en, GPIO.OUT)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    p = GPIO.PWM(en, 100)

    p.start(25)
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
    print("\n")

    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)

    sleep(2)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
