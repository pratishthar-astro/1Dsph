
import numpy as np
from density_pandas import get_density
from equation_of_state_pandas import equation_of_state
from boundary_conditions_pandas import periodic_bc
from density_pandas import get_accel

def derivs(particles, mass, num_neighbors, sound_speed):
    # Calculate density
    density = get_density(particles.data['Position'], mass, particles.data['Smoothing_Length'], num_neighbors)
    particles.data['Density'] = density
    #print('after dens')
    #print(particles.data)
    # Apply boundary conditions after density calculation
    particles.data = periodic_bc(particles.data, num_neighbors)

    # Calculate pressure using equation of state
    particles.data['Pressure'] = equation_of_state(particles.data['Density'], sound_speed)
    
    # Calculate acceleration
    particles.data['Acceleration'] = get_accel(
        particles.data['Position'], 
        particles.data['Pressure'], 
        particles.data['Density'], 
        mass, 
        particles.data['Smoothing_Length'], 
        num_neighbors
    )
    #print('after acc')
    #print(particles.data)
    # Apply boundary conditions again after acceleration calculation
    particles.data = periodic_bc(particles.data, num_neighbors)
    #print(particles.data)
    return particles
