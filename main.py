import hub, time

serial = hub.port.C
serial.mode(hub.port.MODE_FULL_DUPLEX)
time.sleep(1)
serial.baud(115200)

serial.read(1000)
serial.write("\n testing \n\n")
serial.read(1000)