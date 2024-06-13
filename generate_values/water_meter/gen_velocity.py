import random
import math
import time
import numpy as np

# Constants
BASELINE_VELOCITY_MIN = 0.05  # m/s, minimum base flow rate
BASELINE_VELOCITY_MAX = 0.3   # m/s, maximum base flow rate
MAX_VELOCITY = 3.0  # m/s, maximum velocity in pipes
PEAK_VELOCITY = 2.0  # m/s, typical peak hour velocity
MEDIUM_VELOCITY = 1.0  # m/s, medium events like shower
SMALL_VELOCITY = 0.5  # m/s, small events like faucet
MICRO_VELOCITY_MIN = 0.1  # m/s, min for micro-events
MICRO_VELOCITY_MAX = 0.4  # m/s, max for micro-events
BASE_SAMPLING_INTERVAL = 300  # 5 minutes for base velocity
EVENT_CHECK_INTERVAL = 30  # Check for events every 30 seconds
INTERPOLATION_INTERVAL = 1  # 1 second

def get_time_of_day_factor(timestamp):
    hour = timestamp.tm_hour + timestamp.tm_min / 60
    if 6 <= hour < 9 or 17 <= hour < 20:
        return np.random.normal(0.9, 0.2)  # Morning/Evening peak
    elif 23 <= hour or hour < 5:
        return np.random.normal(0.3, 0.1)  # Night lull
    else:
        return np.random.normal(0.6, 0.2)  # Normal daytime

def get_day_of_week_factor(day):
    if day in [5, 6]:  # Saturday and Sunday
        return np.random.normal(0.8, 0.3)  # More variability on weekends
    else:
        return np.random.normal(1.0, 0.2)

def get_seasonal_factor(month):
    if 6 <= month <= 8:  # Summer months
        return np.random.normal(1.3, 0.3)
    elif 12 <= month or month <= 2:  # Winter months
        return np.random.normal(0.7, 0.2)  # Lower in winter
    else:  # Spring and Autumn
        return np.random.normal(1.1, 0.2)

def generate_base_velocity(timestamp):
    hour = timestamp.tm_hour
    day = timestamp.tm_wday
    month = timestamp.tm_mon

    time_factor = get_time_of_day_factor(timestamp)
    day_factor = get_day_of_week_factor(day)
    season_factor = get_seasonal_factor(month)

    base_factor = time_factor * day_factor * season_factor
    
    # Add a natural sine wave oscillation based on time
    minutes = timestamp.tm_hour * 60 + timestamp.tm_min
    day_progress = minutes / (24 * 60)
    oscillation = 0.1 * math.sin(2 * math.pi * day_progress) + 0.05 * math.sin(4 * math.pi * day_progress)
    
    base_velocity = max(BASELINE_VELOCITY_MIN, min(BASELINE_VELOCITY_MAX, 
                      BASELINE_VELOCITY_MIN + (BASELINE_VELOCITY_MAX - BASELINE_VELOCITY_MIN) * (base_factor + oscillation)))
    return base_velocity

def add_random_events(base_velocity, duration):
    velocities = []
    time_left = duration

    while time_left > 0:
        r = random.random()
        if r < 0.05 and time_left > 300:  # High-velocity events, 5% chance
            event_velocity = random.uniform(PEAK_VELOCITY, MAX_VELOCITY)
            event_duration = min(random.randint(60, 300), time_left)
        elif r < 0.15 and time_left > 120:  # Medium-velocity events, 10% chance
            event_velocity = random.uniform(MEDIUM_VELOCITY, PEAK_VELOCITY)
            event_duration = min(random.randint(120, 600), time_left)
        elif r < 0.4 and time_left > 60:  # Small-velocity events, 25% chance
            event_velocity = random.uniform(SMALL_VELOCITY, MEDIUM_VELOCITY)
            event_duration = min(random.randint(30, 120), time_left)
        else:  # Micro-events or base flow
            if random.random() < 0.6:  # 60% chance of micro-event
                event_velocity = random.uniform(MICRO_VELOCITY_MIN, MICRO_VELOCITY_MAX)
                event_duration = min(random.randint(5, 30), time_left)
            else:
                event_velocity = base_velocity
                event_duration = min(random.randint(10, 60), time_left)
        
        ramp_up = np.linspace(base_velocity, event_velocity, num=max(2, event_duration//5))
        stable = [event_velocity] * (max(0, event_duration - 2*len(ramp_up)))
        ramp_down = np.linspace(event_velocity, base_velocity, num=max(2, event_duration//5))
        
        velocities.extend(ramp_up)
        velocities.extend(stable)
        velocities.extend(ramp_down)
        time_left -= event_duration
    
    return velocities[:duration]

def add_noise(velocity):
    base_noise = np.random.normal(0, 0.03)  # Increased base noise
    velocity_noise = np.random.normal(0, 0.1 * velocity)  # 10% velocity-dependent noise, up from 5%
    noisy_velocity = max(BASELINE_VELOCITY_MIN, velocity + base_noise + velocity_noise)
    return min(noisy_velocity, MAX_VELOCITY)

# Main function to get velocity value
def get_velocity_value():
    global start_time, last_base_time, last_base_velocity, last_event_time, velocities

    current_time = int(time.time() - start_time)
    now = time.localtime(time.time())

    # Update base velocity every 5 minutes
    if current_time >= last_base_time + BASE_SAMPLING_INTERVAL:
        last_base_time = current_time
        last_base_velocity = generate_base_velocity(now)

    # Check for new events every 30 seconds
    if current_time >= last_event_time + EVENT_CHECK_INTERVAL or not velocities:
        last_event_time = current_time
        new_velocities = add_random_events(last_base_velocity, EVENT_CHECK_INTERVAL)
        velocities.extend(new_velocities)

    # Get the current velocity and apply noise
    base_velocity = velocities.pop(0) if velocities else last_base_velocity
    current_velocity = add_noise(base_velocity)

    return round(current_velocity, 2)

# Initialize variables
start_time = int(time.time())
last_base_time = -BASE_SAMPLING_INTERVAL
last_base_velocity = BASELINE_VELOCITY_MIN
last_event_time = -EVENT_CHECK_INTERVAL
velocities = []

