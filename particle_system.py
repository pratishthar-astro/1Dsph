# particle_system.py
import numpy as np

class SPHParticles:

    def __init__(self, n):
        self.n = n
        self.position = np.zeros(n)
        self.velocity = np.zeros(n)
        self.mass = np.zeros(n)
        self.smoothing_length = np.zeros(n)
        self.internal_energy = np.zeros(n)
        self.pressure = np.zeros(n)
        self.density = np.zeros(n)

    def setup(self, xmin, xmax, rho_0):
        self.position = np.linspace(xmin, xmax, self.n)
        particle_spacing = (xmax - xmin) / (self.n - 1)
        self.mass = (rho_0/ self.n) * np.ones(self.n)
        sound_speed = 343.0  # in m/s
        amplitude = 1e-4 * sound_speed
        self.velocity = amplitude * np.sin(2 * np.pi * self.position / (xmax - xmin))
        self.smoothing_length = 1.2 * particle_spacing * np.ones(self.n)

    def output(self, filename):
        data = np.column_stack((self.position, self.velocity, self.mass, self.smoothing_length, self.internal_energy, self.pressure))
        np.savetxt(filename, data, header="Position Velocity Mass Smoothing_Length Internal_Energy Pressure", comments='')
