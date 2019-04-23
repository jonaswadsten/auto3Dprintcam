from gpiozero import LightSensor
from subprocess import Popen
import time
from time import gmtime, strftime

# Sensorpin for rpiz
ldr = LightSensor(4)
# Status for camera, 0 is off, 1 is on
camera_status = 0

try:
    while True:
        if ldr.value == 0 and camera_status == 0:
            print('On ', ldr.value)
            print('Cam started at ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
            process = Popen (['bash', '/home/pi/Documents/startcam.sh'])
            camera_status = 1
            time.sleep(5)
        else:
            if ldr.value != 0 and camera_status == 1:
                print('Off ', ldr.value)
                print('Cam stopped  at ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
                process = Popen (['bash', '/home/pi/Documents/stopcam.sh'])
                camera_status = 0
            time.sleep(5)
except KeyboardInterrupt:
    pass
