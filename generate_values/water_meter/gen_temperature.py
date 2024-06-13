import random
import math
import time
import numpy as np


def get_season(month):
    if 3 <= month <= 5:
        return 'spring'
    elif 6 <= month <= 8:
        return 'summer'
    elif 9 <= month <= 11:
        return 'autumn'
    else:
        return 'winter'

# from celsius to fahrenheit
def celsius_to_fahrenheit(temp):
    return temp * 9 / 5 + 32

def generate_temperature():
    month = time.gmtime().tm_mon
    season = get_season(month)

    if season == 'winter':
        temp = random.uniform(-5, 10)
    elif season == 'spring':
        temp = random.uniform(5, 15)
    elif season == 'summer':
        temp = random.uniform(15, 20)
    else: # autumn
        temp = random.uniform(5, 15)
    return temp


# Constants
BASELINE_TEMPERATURE = generate_temperature()
SAMPLING_INTERVAL = 5  # Seconds between temperature readings
INTERPOLATION_INTERVAL = 0.1  # Seconds between interpolated readings
DIURNAL_AMPLITUDE = 1   # Amplitude of the diurnal temperature variation (in degrees)
DIURNAL_PERIOD = 24 * 60 * 60  # Period of the diurnal cycle (24 hours in seconds)
RANDOM_NOISE_AMPLITUDE = 1  # Amplitude of the random noise
TEMPERATURE_RANGE = (10, 30)  # Expected minimum and maximum temperatures

# Main loop to generate and print temperature readings
def generate_temperature_reading(current_time):
    # Calculate the diurnal temperature variation
    diurnal_variation = DIURNAL_AMPLITUDE * math.sin(2 * math.pi * current_time / DIURNAL_PERIOD)

    # Add random noise
    random_noise = random.uniform(-RANDOM_NOISE_AMPLITUDE, RANDOM_NOISE_AMPLITUDE)

    # Calculate the temperature reading
    temperature = BASELINE_TEMPERATURE + diurnal_variation + random_noise

    # Ensure the temperature is within the expected range
    temperature = max(TEMPERATURE_RANGE[0], min(TEMPERATURE_RANGE[1], temperature))

    return temperature

# Function to interpolate temperature
def interpolate_temperature(time1, temp1, time2, temp2, current_time):
    # Calculate the interpolated temperature
    interpolated_temperature = temp1 + (temp2 - temp1) * ((current_time - time1) / (time2 - time1))

    return interpolated_temperature

# Example usage
start_time = time.time()
time1 = 0
temp1 = generate_temperature_reading(time1)
time2 = SAMPLING_INTERVAL
temp2 = generate_temperature_reading(time2)


# Function to get temperature value
def get_temperature_value():
    global time1, temp1, time2, temp2
    current_time = time.time() - start_time
    while current_time >= time2:  # It's time to sample a new temperature
        time1 = time2
        temp1 = temp2
        time2 += SAMPLING_INTERVAL
        # Update the BASELINE_TEMPERATURE according to the current season
        global BASELINE_TEMPERATURE
        BASELINE_TEMPERATURE = generate_temperature()
        temp2 = generate_temperature_reading(time2)
        print(temp1, temp2)
    
    # Generate interpolated temperatures at each INTERPOLATION_INTERVAL
    interpolated_temperatures = [interpolate_temperature(time1, temp1, time2, temp2, t)
                                 for t in np.arange(time1, time2, INTERPOLATION_INTERVAL)]
    
    # Find the interpolated temperature closest to the current time
    idx = min(range(len(interpolated_temperatures)), key=lambda i: abs((time1 + i*INTERPOLATION_INTERVAL) - current_time))
    return round(interpolated_temperatures[idx], 2)

