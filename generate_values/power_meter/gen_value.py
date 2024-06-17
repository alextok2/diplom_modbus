import random
import math
import time
import numpy as np

def generate_value(RANGE):
    value = random.uniform(*RANGE)
    return value

# Constants
INTERPOLATION_INTERVAL = 1  # Seconds between interpolated readings
DIURNAL_AMPLITUDE = 1   # Amplitude of the diurnal value variation (in degrees)
DIURNAL_PERIOD = 24 * 60 * 60  # Period of the diurnal cycle (24 hours in seconds)
RANDOM_NOISE_AMPLITUDE = 1  # Amplitude of the random noise

time1 = 0
value1 = 0
time2 = 0
value2 = 0

# Function to generate value reading
def generate_value_reading(current_time, RANGE, BASELINE_VALUE):
    # Calculate the diurnal value variation
    diurnal_variation = DIURNAL_AMPLITUDE * math.sin(2 * math.pi * current_time / DIURNAL_PERIOD)

    # Add random noise
    random_noise = random.uniform(-RANDOM_NOISE_AMPLITUDE, RANDOM_NOISE_AMPLITUDE)

    # Calculate the value reading
    value = BASELINE_VALUE + diurnal_variation + random_noise

    # Ensure the value is within the expected range
    value = max(RANGE[0], min(RANGE[1], value))

    return value

# Function to interpolate value
def interpolate_value(time1, value1, time2, value2, current_time):
    # Calculate the interpolated value
    interpolated_value = value1 + (value2 - value1) * ((current_time - time1) / (time2 - time1))

    return interpolated_value

# Function to get value 
def get_value(start_time, RANGE, SAMPLING_INTERVAL):
    global time1, value1, time2, value2
    current_time = time.time() - start_time
    BASELINE_VALUE = generate_value(RANGE)

    if current_time >= time2:  # It's time to sample a new value
        time1 = time2
        value1 = value2
        time2 += SAMPLING_INTERVAL
        value2 = generate_value_reading(time2, RANGE, BASELINE_VALUE)
        # print(value1, value2)

    # Generate interpolated values at each INTERPOLATION_INTERVAL
    interpolated_values = [interpolate_value(time1, value1, time2, value2, t)
                           for t in np.arange(time1, time2, INTERPOLATION_INTERVAL)]

    # Find the interpolated value closest to the current time
    idx = min(range(len(interpolated_values)), key=lambda i: abs((time1 + i * INTERPOLATION_INTERVAL) - current_time))
    return round(interpolated_values[idx], 2)

start_time = time.time()
