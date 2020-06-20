import RPi.GPIO as GPIO
import time

CS = 5
Clock = 25
Address = 24
DataOut = 23


class InfraredSensor(object):
    def __init__(self, sensorsCount=5):
        self.sensorsCount = sensorsCount
        self.calibratedMin = [0] * self.sensorsCount
        self.calibratedMax = [1023] * self.sensorsCount
        self.last_value = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(Clock, GPIO.OUT)
        GPIO.setup(Address, GPIO.OUT)
        GPIO.setup(CS, GPIO.OUT)
        GPIO.setup(DataOut, GPIO.IN, GPIO.PUD_UP)


    """
    Reads the sensor values into an array. There *MUST* be space
    for as many values as there were sensors specified in the constructor.
    Example usage:
    unsigned int sensor_values[8];
    sensors.read(sensor_values);
    The values returned are a measure of the reflectance in abstract units,
    with higher values corresponding to lower reflectance (e.g. a black
    surface or a void).
    """
    def AnalogRead(self):
        value = [0]*(self.sensorsCount + 1)
        #Read Channel0~channel6 AD value
        for j in range(0,self.sensorsCount + 1):
            GPIO.output(CS, GPIO.LOW)
            for i in range(0,4):
                #sent 4-bit Address
                if(((j) >> (3 - i)) & 0x01):
                    GPIO.output(Address,GPIO.HIGH)
                else:
                    GPIO.output(Address,GPIO.LOW)
                #read MSB 4-bit data
                value[j] <<= 1
                if(GPIO.input(DataOut)):
                    value[j] |= 0x01
                GPIO.output(Clock,GPIO.HIGH)
                GPIO.output(Clock,GPIO.LOW)
            for i in range(0,6):
                #read LSB 8-bit data
                value[j] <<= 1
                if(GPIO.input(DataOut)):
                    value[j] |= 0x01
                GPIO.output(Clock,GPIO.HIGH)
                GPIO.output(Clock,GPIO.LOW)
        #no mean ,just delay
    #			for i in range(0,6):
    #				GPIO.output(Clock,GPIO.HIGH)
    #				GPIO.output(Clock,GPIO.LOW)
            time.sleep(0.0001)
            GPIO.output(CS,GPIO.HIGH)
        return value[:]
