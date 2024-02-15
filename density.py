# density.py
import numpy as np

def cubic_spline_kernel(q):
    if 0 <= q < 1:
        return 2 / 3 * ((1/4) * (2-q)**3 - (1-q)**3)
    elif 1 <= q < 2:
        return 2 / 3 * ((1/4) * (2-q)**3)
    else:
        return 0

def get_density(position, mass, smoothing_length):
    density = np.zeros_like(position)

    for i in range(len(position)):
        density[i] = compute_density_at_particle(i, position, mass, smoothing_length)

    return density

def compute_density_at_particle(particle_index, position, mass, smoothing_length):
    density_sum = 0.0

    for j in range(len(position)):
        q = np.abs(position[particle_index] - position[j]) / smoothing_length[particle_index]
        density_sum += mass[j] * cubic_spline_kernel(q)

    return density_sum
