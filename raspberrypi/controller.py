"""Controller for SPIKE Prime
The module runs on Raspberry PI MicroPython environment.
Using the following command to run the file:
    python pyboard.py --device /dev/ttyACM0 controller.py
"""
import json
import hub,utime

# Raspberry Pi4 
serial = hub.port.D
serial.mode(hub.port.MODE_FULL_DUPLEX)
utime.sleep(1)
serial.baud(115200)

# Motors
left = hub.port.C.motor
right = hub.port.D.motor

left.pwm(0)
right.pwm(0)

while True : 
    # Read communcition from Raspberry Pi and Decode
    data = serial.read(1000)
    # data = data.decode("UTF-8")
    # parameters = json.loads(data)
    print(data)
    # speed = parameters["speed"]
    left.pwm(data)
    right.pwm(data)

    utime.sleep_ms(100)
