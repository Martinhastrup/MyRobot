import numpy as np

# pi IP: 192.168.1.58
# RUN ssh pi@192.168.1.58

import RPi.GPIO as GPIO
from time import sleep


def forward(x):
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving Forward")
    sleep(2)
    GPIO.output(Forward, GPIO.LOW)


def reverse(x):
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving Backward")
    sleep(2)
    GPIO.output(Backward, GPIO.LOW)


if __name__ == "__main__":

    in1 = 24
    in2 = 23
    in3 = 26
    in4 = 16
    en1 = 25
    en2  = 6
    temp1 = 1

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)
    GPIO.setup(en1, GPIO.OUT)
    GPIO.setup(en2, GPIO.OUT)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    p1 = GPIO.PWM(en1, 100)
    p2 = GPIO.PWM(en2, 100)

    p1.start(25)
    p2.start(25)
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
    print("\n")

    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)

    sleep(5)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    """
    mode = GPIO.getmode()

    Forward = 24
    Backward = 23

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Forward, GPIO.OUT)
    GPIO.setup(Backward, GPIO.OUT)

    while 1:
        forward(5)
        reverse(5)
        GPIO.cleanup()
    """


