from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.hubs import EV3Brick

# Initialize the hub.
hub = EV3Brick()

print(hub)

# hub.display.char('a')
# hub.light.off()
hub.light.on(Color.RED)

# Raspberry Pi4 
serial = hub.port.C
serial.mode(hub.port.MODE_FULL_DUPLEX)
serial.baud(115200)

# Initialize serial port connected to LEGO SPIKE PRIME
serialPort = serial.Serial(
    port='/dev/ttyAMA1',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

