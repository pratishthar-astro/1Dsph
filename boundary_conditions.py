import numpy as np

def periodic_bc(position, box_size, num_ghost_particles=0):
    original_count = len(position)
    
    # Copy particles on the left side as ghost particles on the right side
    for i in range(original_count):
        if position[i] < 0:
            position.append(position[i] + box_size)
    
    # Copy particles on the right side as ghost particles on the left side
    for i in range(original_count):
        if position[i] >= box_size:
            position.append(position[i] - box_size)
    
    # Copy particles within the valid range to handle periodic boundary conditions
    for i in range(original_count):
        if 0 <= position[i] < box_size:
            position.append(position[i])
    
    # Ensure that the total number of particles (including ghosts) is updated
    total_particles = len(position)
    
    return total_particles