
# DTS Simulation and Experiment Comparison Tool

This project provides a simple interface for comparing Distributed Temperature Sensing (DTS) experimental data with simulations. It allows users to generate and plot DTS data, configure simulation parameters, and customize settings for hot spots and environmental factors.

## Features

- Compare your experimental data with DTS simulation results.
- Use **default values** or customize simulation parameters.
- **Multiple hot spots** configuration using a 30-meter window.
- Plot simulation results and **compare with experimental data**.
- Browse and select your **CSV file** for custom experiments.
- Check an **estimation** of the generated data and simulation time before proceeding.

## Installation

To set up the project, follow these steps:

1. Install dependencies:
   If you have a `requirements.txt` file, run:
   ```bash
   pip install -r requirements.txt
   ```


## Usage

1. Open the project folder in **VSCode** or any other IDE for the best experience.
   
2. Run the main script to start the interface:
   ```bash
   python Easy_test.py
   ```

3. The interface will open, allowing you to:
   - **Select your CSV file**: Browse or use the default experimental data (`EXperimental_data_temp700.csv`).
   - **Set simulation parameters**: Define hot spots, start/stop points, environmental temperature, and more.
   - **Plot** your data: Plot the simulation results and compare them with your experiment.

4. After adjusting settings, you can:
   - **Generate data**: Use the "Generate" button to create simulation samples.
   - **Estimate the number of samples**: Use the "Check Estimation" button to preview the amount of data and approximate generation time.

### Parameters

- **Number of Events**: Define the number of hot spots (e.g., 3).
- **Hotspot Temperatures**: Input the temperature values for each hot spot (comma-separated).
- **Environmental Temperature**: Set the default environmental temperature (e.g., 22°C).
- **Number of Shifts**: Define the number of shifts (e.g., 4) for sweeping along the fiber (between 5-25 meters).
- **Random Locations**: Control how often random hot spot locations are generated.

## Plotting Example

Once the data is generated, you can plot specific samples by entering the sample number and clicking **Plot**. You can visualize the actual temperature profile and the DTS simulation.

## Customization

### Changing Default Parameters
- You can modify the default parameters by editing the **data_generator.py** or **simulator.py** files:
   - **Constance1 and Constance2** for fine-tuning the simulation behavior.
   - **Number of hot spots** and their positions can be randomized or controlled by user inputs.

### File Format Requirements
- The CSV file should match the format of the provided experimental data (`EXperimental_data_temp700.csv`). Ensure your custom data is formatted correctly before running the simulation.


## Example results:
1- Two hot in real world experiment (`EXperimental_data_temp700.csv`) occured in range of 50m-80m. In this 30m window first hot spot start,stop and temperature is 11.7, 13.2 (11.7+1.5m), and 47C respectivelly. second hot spot start,stop and temperature is 15.05, 16.55, and 80C respectively.

<img src="https://github.com/ErfanDejband/DTS_Simulation/blob/main/Images/Img1.png" alt="Img1" width="500" />

2- Two hot in real world experiment (`30C_1.1M_50C.csv`) occured in range of 25m-55m. In this 30m window first hot spot start,stop and temperature is 12.9, 14.4 (12.9+1.5m), and 30C correspondinglly. second hot spot start,stop and temperature is 15.5, 17, and 50C correspondinglly.

 <img src="https://github.com/ErfanDejband/DTS_Simulation/blob/main/Images/Img2.png" alt="Img2" width="500" />

3-Two hot in real world experiment (`30C_0.1M_50C.csv`) occured in range of 25m-55m. In this 30m window first hot spot start,stop and temperature is 12.9, 14.4 (12.9+1.5m), and 30C correspondinglly. second hot spot start,stop and temperature is 14.5 (14.4+0.1m), 16, and 50C correspondinglly.

<img src="https://github.com/ErfanDejband/DTS_Simulation/blob/main/Images/Img3.png" alt="Img3" width="500" />

## Future Work
- Improved user interface with more flexible simulation settings.
- Support for larger windows beyond the 30-meter limit.
- Automated validation of CSV file formats.

---

💻 *Feel free to contribute or suggest improvements!*



