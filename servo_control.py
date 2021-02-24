from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import random as rand
import time

kit = ServoKit(channels=16)
laser_out = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(laser_out, GPIO.OUT)


def go_up_servo():
    for i in range(30):
        kit.servo[1].angle = 45 - i
        time.sleep(0.05)
    for i in range(30):
        kit.servo[1].angle = 15 + i
        time.sleep(0.05)


def go_down_servo():
    for i in range(30):
        kit.servo[1].angle = 45 + i
        time.sleep(0.05)
    for i in range(30):
        kit.servo[1].angle = 75 - i
        time.sleep(0.05)


def go_left_servo():
    for i in range(30):
        kit.servo[0].angle = 90 + i
        time.sleep(0.05)
    for i in range(30):
        kit.servo[0].angle = 120 - i
        time.sleep(0.05)


def go_right_servo():
    for i in range(30):
        kit.servo[0].angle = 90 - i
        time.sleep(0.05)
    for i in range(30):
        kit.servo[0].angle = 60 + i
        time.sleep(0.05)


def reset_servo():
    kit.servo[0].angle = 90
    kit.servo[1].angle = 45

def activate_LOD():
    GPIO.output(laser_out, True)
    for i in range(15):
        direction = rand.randint(0, 3)
        if direction == 0:
            go_right_servo()
        if direction == 1:
            go_left_servo()
        if direction == 2:
            go_up_servo()
        if direction == 3:
            go_down_servo()
    GPIO.output(laser_out, False)
    reset_servo()


activate_LOD()