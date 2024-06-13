import random
import math
import time
import numpy as np

# Constants
# Built-in (Water) Temperature
WATER_TEMP_WINTER_BASE = 6  # °C
WATER_TEMP_SUMMER_BASE = 15  # °C
WATER_TEMP_DAILY_RANGE = 3  # °C
WATER_TEMP_RAPID_CHANGE_THRESHOLD = 1.5  # m/s, velocity for rapid temp change

# Board Temperature
BOARD_TEMP_WINTER_MIN = 15  # °C
BOARD_TEMP_SUMMER_MAX = 35  # °C
BOARD_TEMP_DAILY_RANGE = 15  # °C
BOARD_CPU_TEMP_RISE = 5  # °C, during high activity
BOARD_SOLAR_TEMP_RISE = 10  # °C, in direct sunlight

# Time Constants
HOUR_SEC = 3600
DAY_SEC = 24 * HOUR_SEC
BASE_SAMPLING_INTERVAL = 300  # 5 minutes for base temperature
INTERPOLATION_INTERVAL = 1  # 1 second
start_time = time.time()
simulated_time = time.localtime(start_time)




def get_day_progress(timestamp):
    return (timestamp.tm_hour * 60 + timestamp.tm_min) / (24 * 60)

def seasonal_interpolation(winter_val, summer_val, month):
    if 3 <= month <= 8:  # Spring to Summer
        return winter_val + ((summer_val - winter_val) * (month - 3) / 5)
    elif 9 <= month <= 11:  # Autumn
        return summer_val - ((summer_val - winter_val) * (month - 9) / 3)
    else:  # Winter
        return winter_val

def get_simulated_time():
    global simulated_time, start_time
    current_real_time = time.time()
    simulated_seconds = int(current_real_time - start_time) + start_time
    simulated_time = time.localtime(simulated_seconds)
    return simulated_time

# Board Temperature Functions
def get_board_base_temp(month):
    winter_base = BOARD_TEMP_WINTER_MIN + 10  # Electronics add about 10°C
    summer_base = BOARD_TEMP_SUMMER_MAX - 10
    return seasonal_interpolation(winter_base, summer_base, month)

random_component = 0
last_random_time = 0

def get_board_daily_variation(day_progress):
    global random_component, last_random_time
    current_time = time.time()
    if current_time - last_random_time > 2:  # Calculate new random component every minute
        random_component = random.uniform(-2, 2)  # Random value between -2 and 2
        last_random_time = current_time
    hour_offset = (day_progress - 0.125) * 2 * math.pi
    return ((BOARD_TEMP_DAILY_RANGE / 2) * math.sin(hour_offset)) + random_component



def get_board_cpu_effect():
    if int(time.time()) % 150 < random.randint(60, 120):
        return BOARD_CPU_TEMP_RISE
    return 0

def get_board_solar_effect():
    hour = time.localtime().tm_hour
    if 11 <= hour < 15 and random.random() < 0.7:  # 70% chance of direct sun
        return BOARD_SOLAR_TEMP_RISE
    return 0

def calculate_board_temperature():
    current_time = get_simulated_time()
    day_progress = get_day_progress(current_time)
    month = current_time.tm_mon

    base_temp = get_board_base_temp(month)
    daily_variation = get_board_daily_variation(day_progress)
    cpu_effect = get_board_cpu_effect()
    solar_effect = get_board_solar_effect()
    
    board_temp = base_temp + daily_variation + cpu_effect + solar_effect
    return round(max(10, min(50, board_temp)), 1)  # Range: 10-50°C

# Constants
INTERVAL = 2  # Two minutes

# Initialize variables
start_time = time.time()
start_temp = calculate_board_temperature()
end_time = start_time + INTERVAL
end_temp = start_temp

def get_board_temperature():
    global start_time, start_temp, end_time, end_temp
    current_time = time.time()
    
    # If we've reached the end of the current interval
    if current_time >= end_time:
        # The end temperature of the current interval becomes the start temperature of the next interval
        start_temp = end_temp
        start_time = end_time
        # Calculate the end temperature of the next interval
        end_time = start_time + INTERVAL
        end_temp = calculate_board_temperature()  # This is your original get_board_temperature function
    
    # Interpolate the temperature for the current time
    ratio = (current_time - start_time) / INTERVAL
    board_temp = start_temp + ratio * (end_temp - start_temp)
    
    return round(board_temp, 1)  # Range: 10-50°C



def interpolate(start_value, end_value, start_time, end_time, current_time):
    # Calculate the ratio of the difference between the current time and the start time
    # to the total time difference
    ratio = (current_time - start_time) / (end_time - start_time)
    # Calculate the interpolated value
    interpolated_value = start_value + ratio * (end_value - start_value)
    return interpolated_value



