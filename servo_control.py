from adafruit_servokit import ServoKit

from board import SCL, SDA
import busio

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

kit = ServoKit(channels=16)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)
pca.frequency = 50

#import adafruit_motor.servo
#servo = adafruit_motor.servo.Servo(servo_channel)

kit.servo[0].angle = 0

kit.servo[0].angle = 90

"""
# Import the PCA9685 module.
import Adafruit_PCA9685
import time

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096


# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000  # 1,000,000 us per second
    pulse_length //= 60  # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096  # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)


# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

pwm.set_pwm(0, 0, 275)
pwm.set_pwm(0, 0, 375)
print('aaand back')
pwm.set_pwm(1, 0, 275)
pwm.set_pwm(1, 0, 375)
"""
