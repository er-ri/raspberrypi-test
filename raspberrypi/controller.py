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
left = hub.port.B.motor
right = hub.port.E.motor

left.pwm(0)
right.pwm(0)

while True : 
    try : 
        # Read communcition from Raspberry Pi and Decode
        line = serial.read(1000)
        line = str(line.decode("UTF-8"))
        print(line)
        
        if (line.startswith('d')) :
            # We are reading from the GUI Wheel
            left.pwm(40)
            right.pwm(40)  
            # utime.sleep_ms(3000)   

        elif (line.startswith('p')) :
            left.pwm(0)
            right.pwm(0)
      
    except: 
        pass

    utime.sleep_ms(100)
