from derivs import derivs

def leapfrog_integration(particles, dt, mass, num_neighbors, sound_speed):
    # Update positions
    particles.data['Position'] += dt * particles.data['Velocity'] + 0.5 * (dt ** 2) * particles.data['Acceleration']
    
    # Compute intermediate velocity
    #print('before')
    #print(particles.data)
    
    particles.data['Velocity_step'] = particles.data['Velocity'] + dt * particles.data['Acceleration']
    particles.data['Acceleration0'] = particles.data['Acceleration']
    #print('medium')
    #print(particles.data)
    
    # Call derivs to compute density, pressure, and acceleration with updated positions
    particles = derivs(particles, mass, num_neighbors, sound_speed)
    #print('after')
    #print(particles.data)
    
    # Update velocities with new accelerations
    particles.data['Velocity'] = particles.data['Velocity_step'] + 0.5 * dt * (particles.data['Acceleration'] - particles.data['Acceleration0'])



