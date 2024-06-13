import random
import time
import numpy as np

# Define the normal pressure range
NORMAL_PRESSURE_RANGE = (40, 50)  # psi
SAMPLING_INTERVAL = 5
INTERPOLATION_INTERVAL = 0.1

# Define time-based pressure patterns
TIME_PATTERNS = {
    "morning": (-5, 5),    # Lower pressure in the morning
    "afternoon": (0, 10),  # Higher pressure in the afternoon
    "evening": (-10, 0)    # Lower pressure in the evening
}

# Define a function to generate a pressure reading
def generate_pressure_reading(base_pressure, time_of_day):
    pressure_offset = TIME_PATTERNS.get(time_of_day, (0, 0))
    random_offset = random.randint(*pressure_offset)
    pressure = base_pressure + random_offset
    return max(NORMAL_PRESSURE_RANGE[0], min(pressure, NORMAL_PRESSURE_RANGE[1]))

# Main loop to generate and print pressure readings
def get_pressure_value(current_time):
    hour = current_time.tm_hour

    if 6 <= hour < 12:
        time_of_day = "morning"
    elif 12 <= hour < 18:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"

    base_pressure = random.randint(*NORMAL_PRESSURE_RANGE)
    pressure_reading = generate_pressure_reading(base_pressure, time_of_day)

    return pressure_reading

def interpolate_pressure(time1, pressure1, time2, pressure2, current_time):
    # Calculate the interpolated pressure
    interpolated_pressure = pressure1 + (pressure2 - pressure1) * ((current_time - time1) / (time2 - time1))

    return interpolated_pressure

# Example usage
start_time = time.time()
time1 = 0
pressure1 = get_pressure_value(time.localtime(time1))
time2 = SAMPLING_INTERVAL
pressure2 = get_pressure_value(time.localtime(time2))

def get_interpolated_pressure():
    global time1, pressure1, time2, pressure2
    current_time = time.time() - start_time
    while current_time >= time2:  # It's time to sample a new pressure
        time1 = time2
        pressure1 = pressure2
        time2 += SAMPLING_INTERVAL
        pressure2 = get_pressure_value(time.localtime(time2))
    
    # Generate interpolated pressures at each INTERPOLATION_INTERVAL
    interpolated_pressures = [interpolate_pressure(time1, pressure1, time2, pressure2, t)
                                 for t in np.arange(time1, time2, INTERPOLATION_INTERVAL)]
    
    # Find the interpolated pressure closest to the current time
    idx = min(range(len(interpolated_pressures)), key=lambda i: abs((time1 + i*INTERPOLATION_INTERVAL) - current_time))
    return round(interpolated_pressures[idx],2)



