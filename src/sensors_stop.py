# IRLineSensor1.py

from raspisim import *
#from raspibrick import *

RobotContext.useBackground("sprites/circle.gif")

robot = Robot()
gear = Gear()
#gear.setSpeed(30)
ir_left = InfraredSensor(IR_LINE_LEFT)
ir_right = InfraredSensor(IR_LINE_RIGHT)
gear.forward()

while not isEscapeHit():
    v1 = ir_left.getValue()
    v2 = ir_right.getValue()
    if v1 == 0 or v2 == 0:
        gear.backward(1200)
        gear.left(550)
        gear.forward()
robot.exit()