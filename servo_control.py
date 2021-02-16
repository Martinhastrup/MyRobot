from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)


kit.servo[0].angle = 45
time.sleep(1)
kit.servo[0].angle = 0
time.sleep(1)
kit.servo[0].angle = 90
time.sleep(1)
kit.servo[0].angle = 45
time.sleep(1)

kit.servo[1].angle = 0
time.sleep(1)
kit.servo[1].angle = 45
time.sleep(1)
kit.servo[1].angle = 0
time.sleep(1)
kit.servo[1].angle = 45
time.sleep(1)
