import random
import numpy as np
import time

# Constants
PIPE_DIAMETER = 0.1  # 100mm pipe, common in residential settings
BLUFF_BODY_WIDTH = 0.02  # 20mm, typical for a 100mm pipe
STROUHAL_NUMBER = 0.25  # Typical value for vortex meters
from generate_values.water_meter.gen_velocity import MAX_VELOCITY



def velocity_to_vortex_frequency(velocity):
    # Using the Strouhal number equation: St = f * d / v
    # Rearranged to solve for f: f = St * v / d
    frequency = STROUHAL_NUMBER * velocity / BLUFF_BODY_WIDTH
    return frequency

def add_vortex_noise(frequency, velocity):
    # Noise model:
    # 1. Base noise: Always present, small
    # 2. Velocity-dependent noise: Higher velocity, higher noise
    # 3. Pipe vibration noise: Random spikes

    # Base noise (always present, very small)
    base_noise = np.random.normal(0, 0.001 * frequency)
    
    # Velocity-dependent noise (higher at higher velocities)
    velocity_noise = np.random.normal(0, 0.02 * velocity * frequency)
    
    # Pipe vibration noise (occasional spikes)
    if random.random() < 0.05:  # 5% chance
        vibration_noise = np.random.normal(0, 0.1 * frequency)
    else:
        vibration_noise = 0
    
    # Combine noise components
    total_noise = base_noise + velocity_noise + vibration_noise
    
    # Ensure frequency doesn't go negative or exceed a realistic max
    max_freq = MAX_VELOCITY * STROUHAL_NUMBER / BLUFF_BODY_WIDTH
    noisy_frequency = max(0, min(frequency + total_noise, max_freq))
    
    return noisy_frequency

def get_vortex_frequency(velocity):

    # Convert velocity to vortex frequency
    base_frequency = velocity_to_vortex_frequency(velocity)
    
    # Add realistic noise to the frequency
    noisy_frequency = add_vortex_noise(base_frequency, velocity)
    
    # Round to two decimal places for typical sensor precision
    return round(noisy_frequency, 2)

