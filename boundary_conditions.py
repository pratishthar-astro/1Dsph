# boundary_conditions.py
import numpy as np

def periodic_bc(position, box_size, num_ghost_particles=0):
    original_count = len(position)
    
    for i in range(original_count):
        if position[i] < 0:
            position[i] += box_size
        elif position[i] >= box_size:
            position[i] -= box_size
    
    for i in range(original_count, original_count + num_ghost_particles):
        if position[i - original_count] < 0:
            position[i] = position[i - original_count] + box_size
        elif position[i - original_count] >= box_size:
            position[i] = position[i - original_count] - box_size