from vpython import *

# Constants
G = 6.67e-11  # universal gravitational constant
M = 5.97e24     # mass of the Earth
R = 6.37e6      # radius of the Earth

# Earth attributes
earth = sphere(pos=vector(0, 0, 0), radius=R, color=color.blue)

# Satellite attributes
satellite = sphere(pos=vector(9e6, 0, 0), radius=1e6, color=color.red, make_trail=True) # the size is much too big, but is set so the satellite can actually be seen
satellite.mass = 1e3  # mass of the satellite
satellite.velocity = vector(0, 7e3, 0)  # initial velocity

# Simulation loop
# making an assumption here that earth mass >> satellite mass, therefore
# earth's position is not changing in any necessary-to-account-for amount
dt = 10
while True:
    rate(100) # controls how quickly the simulation runs, otherwise the trail goes wild
    r = satellite.pos - earth.pos
    Force_gravity = -G * M * satellite.mass / mag2(r) * norm(r) # mag2 computes the magnitude of a vector squared, norm computes the unit vector (direction)
    satellite.velocity += Force_gravity / satellite.mass * dt
    satellite.pos += satellite.velocity * dt
