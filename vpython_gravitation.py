from vpython import sphere, vector, color, rate, mag2, norm
# mag computes the magnitude of a vector squared, norm computes the unit vector (direction)


# Constants
G = 6.67e-11  # universal gravitational constant
M = 5.97e24     # mass of the Earth
R = 6.37e6      # radius of the Earth

# Earth
earth = sphere(pos=vector(0, 0, 0), radius=R, color=color.blue)

# Satellite
satellite = sphere(pos=vector(9e6, 0, 0), radius=1e6, color=color.red, make_trail=True)
satellite.mass = 1e3  # mass of the satellite
satellite.velocity = vector(0, 7e3, 0)  # initial velocity

# Simulation loop
# making an assumption here that earth mass >> satellite mass, therefore
# earth's position is not changing in any necessary-to-account-for amount
dt = 10
while True:
    rate(100)
    r = satellite.pos - earth.pos
    F_gravity = -G * M * satellite.mass / mag2(r) * norm(r)
    satellite.velocity += F_gravity / satellite.mass * dt
    satellite.pos += satellite.velocity * dt
