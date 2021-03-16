import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time
import random as rand
from datetime import datetime, timedelta

# pi IP: 192.168.1.58
# RUN ssh pi@192.168.1.58

# Distance
# set GPIO Pins
GPIO_TRIGGER = 22
GPIO_ECHO = 27

# Configure Beam of Death
laser_out = 5

# Servokit
kit = ServoKit(channels=16)

# Motor inputs
M1_forward = 24
M1_backward = 23
M2_forward = 26
M2_backward = 16
en1 = 25
en2 = 6
temp1 = 1



GPIO.setup(M1_forward, GPIO.OUT)
GPIO.setup(M1_backward, GPIO.OUT)
GPIO.setup(M2_forward, GPIO.OUT)
GPIO.setup(M2_backward, GPIO.OUT)
GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
forward_M1 = GPIO.PWM(M1_forward, 100)
backward_M1 = GPIO.PWM(M1_backward, 100)
forward_M2 = GPIO.PWM(M2_forward, 100)
backward_M2 = GPIO.PWM(M2_backward, 100)
p1 = GPIO.PWM(en1, 100)  # right wheel
p2 = GPIO.PWM(en2, 100)  # left wheel

p1.start(90)
p2.start(90)


def init():
    # GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # set GPIO direction (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    # Configure Beam of Death
    GPIO.setup(laser_out, GPIO.OUT)
    GPIO.output(laser_out, False)

    # Setup motor
    GPIO.setup(M1_forward, GPIO.OUT)
    GPIO.setup(M1_backward, GPIO.OUT)
    GPIO.setup(M2_forward, GPIO.OUT)
    GPIO.setup(M2_backward, GPIO.OUT)
    GPIO.setup(en1, GPIO.OUT)
    GPIO.setup(en2, GPIO.OUT)


def distance():
    # set Trigger to HIGH
    init()
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
    init()
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
    random_turn(x)


def right(x):
    print('Turning right')
    #init()
    #GPIO.output(M1_forward, False)
    #GPIO.output(M1_backward, True)
    #GPIO.output(M2_forward, True)
    #GPIO.output(M2_backward, False)
    #p1.ChangeDutyCycle(80)
    #forward_M1.ChangeDutyCycle(80)
    #forward_M2.ChangeDutyCycle(0)
    #p2.ChangeDutyCycle(80)
    #backward_M1.ChangeDutyCycle(0)
    #backward_M2.ChangeDutyCycle(80)
    #GPIO.output(en1, GPIO.HIGH)
    #GPIO.output(en2, GPIO.HIGH)
    #p2.ChangeDutyCycle(80)
    GPIO.output(M1_forward, GPIO.HIGH)
    GPIO.output(M1_backward, GPIO.LOW)
    GPIO.output(M2_forward, GPIO.LOW)
    GPIO.output(M2_backward, GPIO.HIGH)
    time.sleep(x)
    #GPIO.cleanup()


def left(x):
    print('Turning left')
    GPIO.output(M1_forward, GPIO.LOW)
    GPIO.output(M1_backward, GPIO.HIGH)
    GPIO.output(M2_forward, GPIO.HIGH)
    GPIO.output(M2_backward, GPIO.LOW)
    time.sleep(x)
    #GPIO.cleanup()


def stop():
    print("Stopping")
    GPIO.output(M1_forward, GPIO.LOW)
    GPIO.output(M1_backward, GPIO.LOW)
    GPIO.output(M2_forward, GPIO.LOW)
    GPIO.output(M2_backward, GPIO.LOW)
    #forward_M1.ChangeDutyCycle(0)
    #forward_M2.ChangeDutyCycle(0)
    #backward_M1.ChangeDutyCycle(0)
    #backward_M2.ChangeDutyCycle(0)

def check_movement(mem):
    try:
        current_distance = mem[-1]
        if mem[-1] > mem[-2] > mem[-3]:
            return 'turn'
        if mem[-1] == mem[-2] == mem[-3]:
            return 'reverse'
        else:
            return 'go straight'
    except:
        return 'go straight'


def go_up_servo(x):
    for i in range(15):
        kit.servo[1].angle = 45 - i
        time.sleep(x)
    for i in range(15):
        kit.servo[1].angle = 30 + i
        time.sleep(x)


def go_down_servo(x):
    for i in range(45):
        kit.servo[1].angle = 45 + i
        time.sleep(x)
    for i in range(45):
        kit.servo[1].angle = 75 - i
        time.sleep(x)


def go_left_servo(x):
    for i in range(30):
        kit.servo[0].angle = 90 + i
        time.sleep(x)
    for i in range(30):
        kit.servo[0].angle = 120 - i
        time.sleep(x)


def go_right_servo(x):
    for i in range(30):
        kit.servo[0].angle = 90 - i
        time.sleep(x)
    for i in range(30):
        kit.servo[0].angle = 60 + i
        time.sleep(x)


def reset_servo():
    kit.servo[0].angle = 90
    kit.servo[1].angle = 45


def random_turn(x):
    decision = rand.randint(0, 2)
    if decision == 0:
        right(x)
    if decision == 1:
        left(x)
    if decision == 2:
        reverse(x)


def deploy_treats():
    kit.servo[3].angle = 90
    time.sleep(1)
    kit.servo[3].angle = 160


def activate_lod(x):
    GPIO.output(laser_out, True)
    for i in range(6):
        direction = rand.randint(0, 3)
        if direction == 0:
            go_right_servo(x)
        if direction == 1:
            go_left_servo(x)
        if direction == 2:
            go_down_servo(x)
        if direction == 3:
            go_down_servo(x)
    GPIO.output(laser_out, False)
    reset_servo()


memory = []
direction = ''
turn_time = 1.2
reverse_time = 1.0

end_time = datetime.now() + timedelta(0, 10)
now = datetime.now()
init()

try:
    while now <= end_time:
        dist = int(sum([distance() for i in range(5)]) / 5)
        memory.append(dist)

        if check_movement(memory) == 'go straight' and dist > 25:
            direction = 'FORWARD'
            forward(0.1)
        elif check_movement(memory) == 'reverse':
            reverse(reverse_time)
            memory = []
        elif check_movement(memory) == 'turn' or dist <= 25:
            direction = 'TURNING'
            random_turn(turn_time)
        if rand.randint(0, 250) == 0:
            print('Exterminate!')
            stop()
            activate_lod(0.2)
        #   deploy_treats()
        if len(memory) > 4:
            memory = memory[-4:]
        now = datetime.now()



# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    stop()
    GPIO.cleanup()
    print("Exiting")

print('job done')
quit()