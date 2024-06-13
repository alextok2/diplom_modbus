import math
import time
import numpy as np
import random

# Water pipe parameters
PIPE_DIAMETER = 0.2  # meters
PIPE_AREA = math.pi * (PIPE_DIAMETER / 2) ** 2  # square meters
PIPE_LENGTH = 1000  # meters
SAMPLING_INTERVAL = 5
INTERPOLATION_INTERVAL = 0.1

# Velocity parameters (adjust according to your requirements)


# Time parameters
SECONDS_PER_DAY = 24 * 60 * 60

# Instantaneous flow rate calculation
def calculate_flow_rate(velocity):
    flow_rate = velocity * PIPE_AREA  # cubic meters per hour
    return flow_rate

# Function to get instantaneous flow rate value
from datetime import datetime

def get_instantaneous_flow_rate_value(current_time):
    # Convert current_time to a datetime object
    current_time = datetime.fromtimestamp(current_time)

    # Calculate phase of the daily cycle (0 to 2pi)
    phase = (current_time.second % SECONDS_PER_DAY) / SECONDS_PER_DAY * 2 * math.pi

    # Adjust velocities based on the time of day and a random factor for appliance usage
    if 6 <= current_time.hour < 9 or 18 <= current_time.hour < 21:  # peak usage times
        MIN_VELOCITY = random.uniform(2, 3)
        MAX_VELOCITY = random.uniform(4, 6)
    else:  # off-peak times
        MIN_VELOCITY = random.uniform(1, 2)
        MAX_VELOCITY = random.uniform(2, 3)

    # Generate velocity based on the daily cycle
    velocity = MIN_VELOCITY + (MAX_VELOCITY - MIN_VELOCITY) * (math.sin(phase) + 1) / 2

    # Calculate instantaneous flow rate
    flow_rate = calculate_flow_rate(velocity)

    return flow_rate


# Function to interpolate instantaneous flow rate
def interpolate_instantaneous_flow_rate(time1, instantaneous_flow_rate1, time2, instantaneous_flow_rate2, t):
    return instantaneous_flow_rate1 + (instantaneous_flow_rate2 - instantaneous_flow_rate1) * ((t - time1) / (time2 - time1))

# Main loop
start_time = time.time()
time1 = 0
instantaneous_flow_rate1 = get_instantaneous_flow_rate_value(time1)
time2 = SAMPLING_INTERVAL
instantaneous_flow_rate2 = get_instantaneous_flow_rate_value(time2)

def get_interpolated_instantaneous_flow_rate():
    global time1, instantaneous_flow_rate1, time2, instantaneous_flow_rate2
    current_time = time.time() - start_time
    while current_time >= time2:  # It's time to sample a new instantaneous_flow_rate
        time1 = time2
        instantaneous_flow_rate1 = instantaneous_flow_rate2
        time2 += SAMPLING_INTERVAL
        instantaneous_flow_rate2 = get_instantaneous_flow_rate_value(time2)
        # print(instantaneous_flow_rate1, instantaneous_flow_rate2)
    
    # Generate interpolated instantaneous_flow_rates at each INTERPOLATION_INTERVAL
    interpolated_instantaneous_flow_rates = [interpolate_instantaneous_flow_rate(time1, instantaneous_flow_rate1, time2, instantaneous_flow_rate2, t)
                                 for t in np.arange(time1, time2, INTERPOLATION_INTERVAL)]
    
    # Find the interpolated instantaneous_flow_rate closest to the current time
    idx = min(range(len(interpolated_instantaneous_flow_rates)), key=lambda i: abs((time1 + i*INTERPOLATION_INTERVAL) - current_time))
    return round(interpolated_instantaneous_flow_rates[idx],2)



