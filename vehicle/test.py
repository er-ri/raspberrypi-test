from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.hubs import EV3Brick

# Initialize the hub.
hub = EV3Brick()

print(hub)

# hub.display.char('a')
# hub.light.off()
hub.light.on(Color.RED)