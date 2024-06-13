import random
import math
import time
import numpy as np
import pandas as pd
from generate_values.water_meter.gen_temperature import get_temperature_value, celsius_to_fahrenheit
from generate_values.water_meter.gen_pressure import get_interpolated_pressure

# Steam table data (simplified for this example)
# Format: [Temperature (°C), Pressure (bar), Enthalpy (kJ/kg)]
steam_table_data = [
    [0, 1, 0.02],
    [50, 1, 209.3],
    [100, 1, 419.1],
    [150, 5, 632.1],
    [200, 15, 855.7],
    [250, 40, 1085.4],
    [300, 85, 1345.0]
]

# Create a DataFrame for easier interpolation
steam_table = pd.DataFrame(steam_table_data, columns=['Temperature', 'Pressure', 'Enthalpy'])

def interpolate_enthalpy(temp, pressure):
    """Interpolate enthalpy from steam table data."""
    # Ensure temperature and pressure are within table bounds
    temp = max(steam_table['Temperature'].min(), min(steam_table['Temperature'].max(), temp))
    pressure = max(steam_table['Pressure'].min(), min(steam_table['Pressure'].max(), pressure))
    
    # Create interpolation functions
    temp_interp = np.interp(temp, steam_table['Temperature'], steam_table['Enthalpy'])
    pressure_interp = np.interp(pressure, steam_table['Pressure'], steam_table['Enthalpy'])
    
    # Average the interpolations (this is a simplification; real steam tables are more complex)
    return (temp_interp + pressure_interp) / 2

def generate_pressure():
    """Generate a realistic pressure value."""
    base_pressure = 5  # Base pressure in bar
    variation = random.uniform(-1, 1)  # Random variation
    daily_cycle = 2 * math.sin(2 * math.pi * time.time() / (24 * 60 * 60))  # Daily cycle
    
    pressure = base_pressure + variation + daily_cycle
    return max(1, pressure)  # Ensure pressure is at least 1 bar

def get_enthalpy_value(temperature, pressure):
    # Calculate enthalpy
    enthalpy = interpolate_enthalpy(temperature, pressure)
    
    # Add some noise to make it more realistic
    noise = random.uniform(-5, 5)
    enthalpy += noise
    
    return round(enthalpy, 2)
