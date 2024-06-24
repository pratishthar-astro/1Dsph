
def compute_cfl_time_step(C, h, vmax, csmax):
    """
    Compute the CFL time step based on given parameters.

    Parameters:
    - C: Dimensionless constant (typically 0.2 to 0.3)
    - h: Smoothing length or kernel radius
    - vmax: Maximum velocity in the simulation domain
    - csmax: Maximum sound speed in the simulation domain

    Returns:
    - CFL time step (float)
    """
    return C * h / max(vmax, csmax)
