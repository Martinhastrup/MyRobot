from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)


def go_up():
    for i in range(18):
        kit.servo[1].angle = 45 - (i*2)
        time.sleep(0.05)


def go_down():
    for i in range(18):
        kit.servo[1].angle = 45 + (i*2)
        time.sleep(0.05)


def go_left():
    for i in range(18):
        kit.servo[0].angle = 45 + (i*2)
        time.sleep(0.05)


def go_right():
    for i in range(18):
        kit.servo[0].angle = 45 - (i*2)
        time.sleep(0.05)

def reset():
    kit.servo[0].angle = 90
    kit.servo[1].angle = 45

#kit.servo[0].angle = 90
#time.sleep(1)
#kit.servo[0].angle = 0
#time.sleep(1)
#kit.servo[0].angle = 150
#time.sleep(1)
#kit.servo[0].angle = 60
#time.sleep(1)

go_left()
go_right()
go_up()
go_down()
reset()