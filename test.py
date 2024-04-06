import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from simulator import simulate
# Read the Excel file
df = pd.read_excel('Experimental_data_temp700.xlsx')
# Test case
H_start = 10
H_stop = 11.5
H_temperature = 30

# Call the simulate function
distance, actual_T, DDTS = simulate(H_start=H_start, H_stop=H_stop, H_temperature=H_temperature)

# Plot DDTS
plt.figure(figsize=(10, 6))
plt.plot(distance,actual_T, label='Actual Temperature')
plt.plot(distance,DDTS, marker = 's', label='DDTS')
distance, actual_T, DDTS = simulate(H_start=H_start, H_stop=H_stop, H_temperature=H_temperature,num_points=100)
plt.plot(distance,actual_T, label='Actual Temperature')
plt.plot(distance,DDTS, marker = 'o', label='DDTS')

plt.xlabel('Distance')
plt.ylabel('Temperature')
plt.title('Actual Temperature vs DDT_simulation')
plt.legend()
plt.grid(True)
plt.show()
