import pandas as pd
import numpy as np

class SPHParticles:
    def __init__(self, n):
        self.n = n
        self.mass = None
        self.data = pd.DataFrame(columns=['Position', 'Velocity', 'Smoothing_Length', 'Pressure', 'Density', 'Acceleration', 'Acceleration0', 'Is_Ghost'])
        #print(len(self.data))

    def setup(self, xmin, xmax, rho_0, num_neighbors, sound_speed):

        particle_spacing = (xmax - xmin) / (self.n - 2*num_neighbors)
        #print('particle spacing', particle_spacing)
        
        self.data['Position'] = pd.Series(np.linspace(xmin - num_neighbors*particle_spacing, xmax + num_neighbors*particle_spacing, self.n, endpoint=False))

        #Uncomment for debugging
        
        #print(xmin)
        #print(xmin - num_neighbors*particle_spacing)
        #print(xmax)
        #print(xmax + num_neighbors*particle_spacing)
        #print(self.n)
        #np.arange(xmin - num_neighbors*particle_spacing, xmax + num_neighbors*particle_spacing, particle_spacing)
        #print('Position', self.data['Position'])
        
        self.mass = rho_0 / (self.n - 2 * num_neighbors)
        amplitude = 1e-4 * sound_speed
        self.data['Velocity'] = amplitude * pd.Series([np.sin(2 * np.pi * x / (xmax - xmin)) for x in self.data['Position']])
        self.data['Smoothing_Length'] = 1.2 * particle_spacing * pd.Series([1] * self.n)

    
        # Set 'Is_Ghost' column: True for ghost particles, False for real particles
        self.data['Is_Ghost'] = False
        self.data.iloc[:num_neighbors-1, self.data.columns.get_loc('Is_Ghost')] = True
        self.data.iloc[-num_neighbors:, self.data.columns.get_loc('Is_Ghost')] = True
        #print('Ghost ID:', self.data['Is_Ghost'].to_string())

    def to_dataframe(self):
        return self.data


