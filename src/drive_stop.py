import robot.AlphaBot2
import robot.InfraredSensor

if __name__ == "__main__":
    # create all objects on which our code depends
    robot_obj = robot.AlphaBot2()
    sensor_obj = robot.InfraredSensor()
    
    # robot starts moving forward
    robot_obj.forward()

    
    while True:
        # read data from the sensors
        sensor_data = sensor_obj.AnalogRead()
        # determine how many sensors are on the line
        sensors_on_line = sum(map(lambda s: s <= 260, sensor_data[1:]))
        # if a sensor has captured the line we stop
        if sensors_on_line > 0:
            robot_obj.stop()
            break
