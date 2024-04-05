<h1>DTS Simulation Library</h1>

<p>The DTS Simulation Library is a Python package designed to simulate Distributed Temperature Sensing (DTS) data. It provides functions to generate simulated DTS data based on specified parameters such as heating temperature, environmental temperature, and spatial resolution. Additionally, it allows users to compare simulated data with experimental data.</p>

<h2>Installation</h2>

<p>You can install the DTS Simulation Library using pip:</p>

<pre><code>pip install DTS-simulation
</code></pre>

<h2>Usage</h2>

<p>To simulate DTS data, import the <code>simulate</code> function from the library:</p>

<pre><code>from DTS_simulation.simulator import simulate
</code></pre>

<p>You can then use the <code>simulate</code> function to generate simulated DTS data. Here's an example:</p>

<pre><code>distance, actual_T, DDTS = simulate(H_start=10, H_stop=15, H_temperature=79, env_temp=21)
</code></pre>

<p>This will simulate DTS data with a heating event from 10 to 15 meters, with a heating temperature of 79°C and an environmental temperature of 21°C. It returns the distance array, actual temperature array, and DTS signal array.</p>

<p>To compare simulated data with experimental data, you can plot them together. Here's an example using matplotlib:</p>

<pre><code>import matplotlib.pyplot as plt

# Plot experimental data
plt.plot(experimental_distance, experimental_temperature, label='Experimental Data')

# Plot simulated data
plt.plot(distance, actual_T, label='Actual Temperature')
plt.plot(distance, DDTS, label='DDTS')

plt.xlabel('Distance')
plt.ylabel('Temperature')
plt.title('Comparison of Experimental Data with DTS Simulation')
plt.legend()
plt.grid(True)
plt.show()
</code></pre>

<h2>Contributing</h2>

<p>If you'd like to contribute to the DTS Simulation Library, feel free to submit pull requests or open issues on the GitHub repository.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
