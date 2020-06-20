import robot.AlphaBot2
import robot.InfraredSensor
import time

def get_rotation(sensors_on_line_count_dict):
    angle = 0
    # count_greater_three = sum(sensors_on_line_count[count] for count in sensors_on_line_count if count >= 3)
    if  sensors_on_line_count_dict[5] > 0:
        angle = 180
    elif sensors_on_line_count_dict[3] >= 2 or sensors_on_line_count_dict[4] > 0:
        angle = 150
    elif sensors_on_line_count_dict[3] >= 1 and sensors_on_line_count_dict[2] >= 2:
        angle = 120
    elif sensors_on_line_count_dict[2] >= 3 or (sensors_on_line_count_dict[2] >= 2 and sensors_on_line_count_dict[1] >= 3):
        angle = 90
    elif sensors_on_line_count_dict[1] >= 5:
        angle = 60

    if angle is not 0:
        file_log("rotate {}\n".format(angle))
    return angle

def get_direction(sensor_data):
    rotate_direction = "none"

    # when the 2 leftmost sensors have captured the line we want to rotate right
    if sum(map(lambda s: s <= 260, sensor_data[1:3])) > 0:
        rotate_direction = "right"
    # when the 2 rightmost sensors have captured the line we want to rotate left
    elif sum(map(lambda s: s <= 260, sensor_data[4:])) > 0: 
        rotate_direction = "left"
        
    # we log whatever we have decided
    file_log("will rotate {}\n".format(rotate_direction))
    return rotate_direction

def file_log(message):
    with open("./../res/billard.log.txt", "a") as file_obj:
        file_obj.write(message)


if __name__ == "__main__":
    # time.sleep(5)
    # create all objects on which our code depends
    robot_obj = robot.AlphaBot2()
    sensor_obj = robot.InfraredSensor()
    # use a dictionary to keep track of our sensors
    sensors_on_line_count = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
    }
    direction_known = False
    # keep track of time for logging purposes
    t0 = time.time()
    # robot starts moving forward and we start log
    robot_obj.forward()
    file_log("------------New Drive------------\n")
    
    while True:
        # read data from the sensors
        sensor_data = sensor_obj.AnalogRead()
        # determine how many sensors are on the line
        sensors_on_line = sum(map(lambda s: s <= 260, sensor_data[1:]))
        # if there are any we will analyze them
        if sensors_on_line > 0:
            # get direction on first iteration
            # since only then we see the point where the robot enters the line
            if direction_known is not True:
                rotate_direction = get_direction(sensor_data)
                direction_known = True

            # first save the information we got from the sensors
            sensors_on_line_count[sensors_on_line] += 1
            # and write the values those sensors could read to a file
            elapsed_time = time.time() - t0
            current_sensor_values = " ".join([str(i) for i in sensor_data[1:]])
            file_log("{elapsed:.5f} sec: {sensor_values}\n".format(elapsed=elapsed_time, sensor_values=current_sensor_values))

            # then we get the angle between the robot's direction and the line
            angle = get_rotation(sensors_on_line_count)
            # if this was not possible we do not go any further and continue reading data
            if angle is 0: continue

            # we check if by any chanced we missed the direction
            if rotate_direction is "none": break

            # given we have the angle and the direction, the robot rotates
            robot_obj.rotate(angle, rotate_direction)
        else:
            # always start with a clean slate
            direction_known = False
            sensors_on_line_count = {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            }
        # we want to read new data only about 30 times per second so we wait a little bit before reading again
        time.sleep(0.0333)
    # if something happens and we break out of the loop we want to stop
    robot_obj.stop()
