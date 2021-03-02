# pi IP: 192.168.1.58
# RUN ssh pi@192.168.1.58

import RPi.GPIO as GPIO
from time import sleep


def forward(x):
    print("Moving Forward")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    sleep(x)


def reverse(x):
    print("Moving Backward")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    sleep(x)


def right(x):
    print('Turning right')
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    sleep(x)


def left(x):
    print('Turning left')
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    sleep(x)


def stop():
    print("Stopping")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

if __name__ == "__main__":
    in1 = 23
    in2 = 24
    in3 = 16
    in4 = 26
    en1 = 25
    en2 = 6
    temp1 = 1

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)
    GPIO.setup(en1, GPIO.OUT)
    GPIO.setup(en2, GPIO.OUT)
    p1 = GPIO.PWM(en1, 100)
    p2 = GPIO.PWM(en2, 100)

    p1.start(90)
    p2.start(90)
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
    print("\n")

    forward(1)
    right(1.75)
    reverse(1)
    left(1.75)
    stop()



