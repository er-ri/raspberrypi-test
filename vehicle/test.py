from pybricks.hubs import PrimeHub
from pybricks.parameters import Color

# Initialize the hub.
hub = PrimeHub()

print(hub)

hub.display.char('a')
# hub.light.off()
hub.light.on(Color.BLUE)