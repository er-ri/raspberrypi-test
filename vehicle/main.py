from spike import ColorSensor, Motor
from spike.control import wait_for_seconds

leg_motor=Motor('F')
arm_motor=Motor('D')
color_sensor=ColorSensor('B')
leg_motor.set_default_speed(-40)
arm_motor.set_default_speed(-60)
# Set the legs to the starting position.
leg_motor.run_to_position(0)
arm_motor.run_to_position(0)
wait_for_seconds(1)
# Repeat arm and leg movement 10 times.
for x in range(10):
    leg_motor.start()
    arm_motor.run_for_rotations(1)
    leg_motor.stop()
    wait_for_seconds(1)