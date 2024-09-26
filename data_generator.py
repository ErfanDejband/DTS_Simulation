import numpy as np
from simulator import simulate
import random

def generate_dts_data(num_events=2, env_temp=22, hotspot_temperatures=None, num_shift1=10, Number_of_random_location=5):
    """
    Generate DTS data for a specified number of events with random starts and shifts.
    
    Parameters:
        num_events (int): Number of events (default is 2).
        env_temp (float): Environmental temperature.
        hotspot_temperatures (list of float): Array of hotspot temperatures for the last event.
        num_shift1 (int): Number of shift points for the last event.
        Number_of_random_location (int): Number of times to generate new random H_starts for the first N-1 events.
    
    Returns:
        Tuple containing the z array and a list of dictionaries with the format:
        [{X = (actual_T, DDTS), Y = (H_starts, H_stops)}]
    """
    if hotspot_temperatures is None:
        hotspot_temperatures = [50.0, 60.0, 70.0]  # Default hotspot temperatures if not provided
    
    all_simulations = []
    z = None

    # Outer loop: Generate new random H_starts locations multiple times
    for _ in range(Number_of_random_location):
        # Generate new random values for the first N-1 events (H_starts between 5 and 25)
        H_starts_random = sorted([random.uniform(5, 25) for _ in range(num_events - 1)])
        H_temperatures_random = [random.uniform(env_temp, 100) for _ in range(num_events - 1)]
        
        # Loop over hotspot temperatures for the last event
        for temp in hotspot_temperatures:
            # Inner loop: Iterate over shift1 to adjust the last event's position
            for shift1 in np.linspace(5, 25, num_shift1):
                # Create the full H_starts list: random values + current shift1
                H_starts = H_starts_random + [shift1]
                H_stops = [start + 1.5 for start in H_starts]

                # Full list of temperatures: random temperatures + current hotspot temperature
                H_temperatures = H_temperatures_random + [temp]

                # Generate simulation data
                z, actual_T, DDTS = simulate(
                    start=0,
                    stop=30,  # Always set stop to 30
                    H_starts=H_starts,
                    H_stops=H_stops,
                    env_temp=env_temp,
                    H_temperatures=H_temperatures
                )

                # Store the results as a pair of (actual_T, DDTS) and (H_starts, H_stops)
                all_simulations.append({
                    "X": (actual_T, DDTS),
                    "Y": (H_starts, H_stops)
                })
    
    return z, all_simulations
