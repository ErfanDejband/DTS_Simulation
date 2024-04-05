
import numpy as np
import matplotlib.pyplot as plt
from simulator import simulate
# Test case

H_start = 14
H_stop = 15.5
H_temperature = 50

# Call the simulate function
z,actual_T, DDTS = simulate(H_start=H_start, H_stop=H_stop, H_temperature=H_temperature)

# Plot DDTS
plt.figure(figsize=(10, 6))
plt.plot(z,actual_T, label='Actual Temperature')
plt.plot(z,DDTS, label='DDTS')
plt.xlabel('Distance')
plt.ylabel('Temperature')
plt.title('Actual Temperature vs DDTS')
plt.legend()
plt.grid(True)
plt.show()