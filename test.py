import time
import serial,time


ser = serial.Serial('/dev/ttyAMA1',115200)

while True:
    if ser.in_waiting: #if data, read until \n
        x=ser.readline()
        print(x)
        ser.write(b'read: %s\n' % x)