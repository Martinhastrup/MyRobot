import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time
import random as rand

# Servokit
kit = ServoKit(channels=16)

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set GPIO Pins
GPIO_TRIGGER = 22
GPIO_ECHO = 27
# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Motor inputs
M1_forward = 23
M1_backward = 24
M2_forward = 16
M2_backward = 26
en1 = 25
en2 = 6
temp1 = 1

# Configure Beam of Death
laser_out = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(laser_out, GPIO.OUT)


# Setup motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(M1_forward, GPIO.OUT)
GPIO.setup(M1_backward, GPIO.OUT)
GPIO.setup(M2_forward, GPIO.OUT)
GPIO.setup(M2_backward, GPIO.OUT)
GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
p1 = GPIO.PWM(en1, 58) # left wheel
p2 = GPIO.PWM(en2, 51) # right wheel

p1.start(58)
p2.start(51)


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    startTime = time.time()
    stopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        startTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        stopTime = time.time()

    # time difference between start and arrival
    timeElapsed = stopTime - startTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    dist = (timeElapsed * 34300) / 2

    return dist


def forward(x):
    print("Moving Forward")
    GPIO.output(M1_forward, GPIO.HIGH)
    GPIO.output(M1_backward, GPIO.LOW)
    GPIO.output(M2_forward, GPIO.HIGH)
    GPIO.output(M2_backward, GPIO.LOW)
    time.sleep(x)


def reverse(x):
    print("Moving Backward")
    GPIO.output(M1_forward, GPIO.LOW)
    GPIO.output(M1_backward, GPIO.HIGH)
    GPIO.output(M2_forward, GPIO.LOW)
    GPIO.output(M2_backward, GPIO.HIGH)
    time.sleep(x)


def right(x):
    print('Turning right')
    GPIO.output(M1_forward, GPIO.HIGH)
    GPIO.output(M1_backward, GPIO.LOW)
    GPIO.output(M2_forward, GPIO.LOW)
    GPIO.output(M2_backward, GPIO.HIGH)
    time.sleep(x)


def left(x):
    print('Turning left')
    GPIO.output(M1_forward, GPIO.LOW)
    GPIO.output(M1_backward, GPIO.HIGH)
    GPIO.output(M2_forward, GPIO.HIGH)
    GPIO.output(M2_backward, GPIO.LOW)
    time.sleep(x)


def stop():
    print("Stopping")
    GPIO.output(M1_forward, GPIO.LOW)
    GPIO.output(M1_backward, GPIO.LOW)
    GPIO.output(M2_forward, GPIO.LOW)
    GPIO.output(M2_backward, GPIO.LOW)


def check_movement(mem):
    #sorted_mem = sorted(mem, reverse=True)
    #if mem != sorted_mem:
    #    print(mem)
    try:
        current_distance = mem[-1]
        if mem[-1] > mem[-2] > mem[3]:
            return 'turn'
        if int(mem[-1]) == int(mem[-2]) == int(mem[-3]):
            return 'reverse'
        else:
            return 'go straight'
    except:
        return 'go straight'


def random_turn(x):
    if rand.randint(0, 1) == 0:
        right(x)
    else:
        left(x)


def deploy_treats():
    kit.servo[3].angle = 90
    time.sleep(1)
    kit.servo[3].angle = 160


memory = []
direction = ''
# Your code to control the robot goes below this line
try:
    while True:
        dist = distance()
        memory.append(dist)
        if check_movement(memory) == 'go straight' and dist > 25:
            direction = 'FORWARD'
            forward(0.1)
        elif check_movement(memory) == 'reverse':
            reverse(1.50)
            random_turn(0.80)
            memory = []
        elif check_movement(memory) == 'turn' or dist <= 25:
            print(dist)
            direction = 'TURNING'
            random_turn(0.80)
            memory = []
        #if rand.randint(0, 20) == 0:
        #    deploy_treats()
        if len(memory) > 10:
            memory = memory[-10:]
# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    stop()
    GPIO.cleanup()
    print("Exiting")