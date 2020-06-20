import robot.AlphaBot2
import RPi.GPIO as GPIO
import time

if __name__ == "__main__":
    # create an instance of our robot
    robot_obj = robot.AlphaBot2()
    
    # robot starts moving forward
    robot_obj.forward()
    
    # robot keeps moving forward until the program gets interrupted
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
