import numpy as np

def get_density(position, mass, smoothing_length, num_neighbors):
    density = np.zeros_like(position)

    if len(position) > 0:
        # Calculate density only for original particles, excluding ghost particles
        for i in range(num_neighbors, len(position) - num_neighbors):
            #print("Particle ---------------------------------", i)
            density[i] = compute_density_at_particle(i, position, mass, smoothing_length)
            #print("rho_a", density[i])
    return density

def compute_density_at_particle(particle_index, position, mass, smoothing_length):
    density_sum = 0.0

    for j in range(len(position)):
        q = np.abs(position[particle_index] - position[j]) / smoothing_length[j]
        #print("Q value", q)
        density_sum += mass * cubic_spline_kernel(q)/smoothing_length[j]
        #print('contribution of', j, 'sum', density_sum)
        #print('kernel value:', cubic_spline_kernel(q))
    return density_sum

def cubic_spline_kernel(q):
    if 0 <= q < 1:
        return 2 / 3 * (1 - 1.5*(q**2) +0.75*(q**3))
    elif 1 <= q < 2:
        return 2 / 3 * ((1/4) * (2-q)**3)
    else:
        return 0

def equation_of_state(density, sound_speed):
    pressure = sound_speed**2 * density
    return pressure

def compute_gradient_q(q):
    # Compute the gradient numerically using central difference
    if 0 <= q < 1:
        return 2 / 3 * (-3*(q) +2.25*(q**2))
    elif 1 <= q < 2:
        return -2 / 3 * ((3/4) * (2-q)**2)
    else:
        return 0

def get_accel(position, pressure, density, mass, smoothing_length, num_neighbors):
    # Initialize the viscosity terms to zero
    q_ab_a = 0.0
    q_ab_b = 0.0

    n_particles = len(position)  # Use the given n_particles
    accelerations = np.zeros(n_particles)

    # Compute the acceleration for each particle using the given formula
    for i in range(n_particles):
        accel = np.zeros_like(position[i])
        pos_i = position[i]
        rho_i = density[i]
        P_i = pressure[i]
        h_i = smoothing_length[i]
        #accel = 0.0
        # Small epsilon to avoid division-by-zero IN CASE NEEDED with rho_i/rho_j
        # epsilon = 1e-8
    
        for j in range(n_particles):
            if i != j:
                pos_j = position[j]
                rho_j = density[j]
                P_j = pressure[j]
                h_j = smoothing_length[j]
                r_ij = pos_i - pos_j

                q_i = abs(r_ij) / h_i
                q_j = abs(r_ij) / h_j
                
                W_grad_i = np.sign(r_ij)*compute_gradient_q(q_i)/((h_i**2))
                W_grad_j = np.sign(r_ij)*compute_gradient_q(q_j)/((h_j**2))
                    
                term_1 = (P_i + q_ab_a) * W_grad_i/ (rho_i ** 2)
                term_2 = (P_j + q_ab_b) * W_grad_j/ (rho_j ** 2)
                    
                # Accumulate the contributions to acceleration
                accel += mass * (term_1 + term_2)
                
                #if i == 11:
                #    print('particle -----------', j)
                #    print('density a', rho_i)
                #    print('density b', rho_j)
                #    print('r_ab', r_ij)
                #    print('qa', q_i)
                #    print('qb', q_j)
                #    print('nabla_ab_a', W_grad_i)
                #    print('nabla_ab_b', W_grad_j)
                #    print('term1', term_1)
                #    print('term2', term_2)
                #    print('mass', mass)
                #    print('acc', accel)


                    
        # Assign the calculated acceleration
        accelerations[i] = -accel  # Negative due to pressure gradients
        #if i == 11:
            #print('-------------------------------------------final a', accelerations[i])
    return accelerations


