# equation_of_state.py
import numpy as np

def equation_of_state(density, sound_speed):
    pressure = sound_speed**2 * density
    return pressure