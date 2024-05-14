import pandas as pd

def periodic_bc(particles, num_neighbors):
    n_particles = len(particles)
    box_size = particles['Position'].max() - particles['Position'].min()

    # Debug statements
    #print("Before copying:")
    #print(particles)

    # Copy properties from last num_neighbors particles to the beginning
    for i in range(num_neighbors):
        for prop in particles.columns:
            if prop != 'Position':
                particles.loc[i, prop] = particles.loc[n_particles - 2*num_neighbors + i, prop]

    # Copy properties from first num_neighbors particles to the end
    for i in range(num_neighbors):
        for prop in particles.columns:
            if prop != 'Position':
                particles.loc[n_particles - num_neighbors + i, prop] = particles.loc[num_neighbors + i, prop]

    # Debug statements
    #print("After copying:")
    #print(particles)

    return particles
