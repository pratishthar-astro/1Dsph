# output.py
import numpy as np

def output_particles(particles, filename):
    # Save updated particle properties (including density) to a file
    data = np.column_stack((particles.position, particles.velocity, particles.mass, particles.smoothing_length, particles.internal_energy, particles.pressure, particles.density))
    np.savetxt(filename, data, header="Position Velocity Mass Smoothing_Length Internal_Energy Pressure Density", comments='')

