import random
import math
import time
import numpy as np




# Constants
MAX_DENSITY_TEMP = 4  # Temperature (°C) at which water has its maximum density
PURE_WATER_DENSITY = 1000  # Density of pure water at 4°C (kg/m³)
MIN_TEMP = 0  # Minimum expected water temperature (°C)
MAX_TEMP = 30  # Maximum expected water temperature (°C)
BASE_TDS = 200  # Base Total Dissolved Solids (mg/L) - typical for drinking water
TDS_VARIANCE = 50  # Variance in TDS (mg/L)
TDS_TREND_PERIOD = 30 * 24 * 60 * 60  # Period of TDS trend (30 days in seconds)
TDS_TREND_AMPLITUDE = 50  # Amplitude of TDS trend (mg/L)


def calculate_density(temp, tds):
    # Calculate density based on temperature
    # This is a simplified model. For high precision, use more complex equations.
    temp_diff = temp - MAX_DENSITY_TEMP
    density = PURE_WATER_DENSITY * (1 - 0.000063 * (temp_diff ** 2))
    
    # Adjust density based on TDS
    # Approximation: each 100 mg/L of TDS increases density by 0.1 kg/m³
    density += 0.001 * tds
    
    return density

def get_tds(current_time):
    # Base TDS with some random variation
    base_tds = BASE_TDS + random.uniform(-TDS_VARIANCE, TDS_VARIANCE)
    
    # Add a long-term trend to simulate seasonal changes or pipe degradation
    tds_trend = TDS_TREND_AMPLITUDE * math.sin(2 * math.pi * current_time / TDS_TREND_PERIOD)
    
    # Short-term fluctuations (e.g., due to water usage patterns)
    hour_of_day = (time.time() % (24 * 60 * 60)) / (60 * 60)
    if 6 <= hour_of_day <= 9 or 17 <= hour_of_day <= 20:
        # Higher TDS during peak usage hours (morning and evening)
        short_term_tds = random.uniform(0, 50)
    else:
        short_term_tds = random.uniform(-25, 25)
    
    return max(0, base_tds + tds_trend + short_term_tds)

def get_density_value(temp):
    current_time = time.time()
    
    # Get current temperature and TDS
    
    tds = get_tds(current_time)
    
    # Calculate and return density
    density = calculate_density(temp, tds)
    return round(density, 2)

