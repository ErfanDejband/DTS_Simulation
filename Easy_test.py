import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTextEdit,QTabWidget,QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from simulator import simulate, plot_experimental
from data_generator import generate_dts_data 
import os

class DTS_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DTS Simulation GUI')
        self.setGeometry(100, 100, 1000, 600)
        # Tabs
        self.tabs = QTabWidget()
        # Tab 2
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "simulation VS Expermetn")
        self.initTab2()
        # Tab 1
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "Gereate databases")
        self.initTab1()
        

        # # Tab 3
        # self.tab3 = QWidget()
        # self.tabs.addTab(self.tab3, "Tab 3")
        # self.initTab3()

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)
#####################################################
########## set tab 1 ################################
#####################################################
    def initTab1(self):
        self.setWindowTitle('DTS Simulation GUI')
        self.setGeometry(100, 100, 1000, 600)

        # Input fields for the number of events with default value
        self.lbl_num_events_tab1 = QLabel('Number of Events:')
        self.le_num_events_tab1 = QLineEdit()
        self.le_num_events_tab1.setText('2')  # Default value: 3

        # Input field for hotspot temperatures with default value
        self.lbl_hot_temps_tab1 = QLabel('Hot Temperatures (comma-separated):')
        self.le_hot_temps_tab1 = QLineEdit()
        self.le_hot_temps_tab1.setText('45.0, 55.0, 65.0')  # Default value

        # Input field for environmental temperature with default value
        self.lbl_env_temp_tab1 = QLabel('Environmental Temperature:')
        self.le_env_temp_tab1 = QLineEdit()
        self.le_env_temp_tab1.setText('21')  # Default value: 22

        # Input field for shifts (num_shift1) with default value
        self.lbl_shift1_tab1 = QLabel('Number of Shifts (num_shift1):')
        self.le_shift1_tab1 = QLineEdit()
        self.le_shift1_tab1.setText('4')  # Default value: 4

        # Input field for number of random locations with default value
        self.lbl_num_random_locations_tab1 = QLabel('Number of Random Locations:')
        self.le_num_random_locations_tab1 = QLineEdit()
        self.le_num_random_locations_tab1.setText('1')  # Default value: 5

        # Input field for selecting the sample number to plot with default value
        self.lbl_sample_num_tab1 = QLabel('Sample Number to Plot:')
        self.le_sample_num_tab1 = QLineEdit()
        self.le_sample_num_tab1.setText('0')  # Default value: 0

        # Button to generate simulation data
        self.btn_generate_tab1 = QPushButton('Generate Data')
        self.btn_generate_tab1.clicked.connect(self.generate_dts_tab1)

        # Button to plot the selected sample
        self.btn_plot_tab1 = QPushButton('Plot Data')
        self.btn_plot_tab1.clicked.connect(self.plot_dts_sample_tab1)

        # Button to check the number of data points and approximate time
        self.btn_check_estimation = QPushButton('Check Estimation')
        self.btn_check_estimation.clicked.connect(self.check_estimation_tab1)

        # Input layout
        input_layout_tab1 = QVBoxLayout()
        input_layout_tab1.addWidget(self.lbl_num_events_tab1)
        input_layout_tab1.addWidget(self.le_num_events_tab1)
        input_layout_tab1.addWidget(self.lbl_hot_temps_tab1)
        input_layout_tab1.addWidget(self.le_hot_temps_tab1)
        input_layout_tab1.addWidget(self.lbl_env_temp_tab1)
        input_layout_tab1.addWidget(self.le_env_temp_tab1)
        input_layout_tab1.addWidget(self.lbl_shift1_tab1)
        input_layout_tab1.addWidget(self.le_shift1_tab1)
        input_layout_tab1.addWidget(self.lbl_num_random_locations_tab1)
        input_layout_tab1.addWidget(self.le_num_random_locations_tab1)
        input_layout_tab1.addWidget(self.lbl_sample_num_tab1)
        input_layout_tab1.addWidget(self.le_sample_num_tab1)
        input_layout_tab1.addWidget(self.btn_generate_tab1)
        input_layout_tab1.addWidget(self.btn_plot_tab1)
        input_layout_tab1.addWidget(self.btn_check_estimation)

        # Message display area
        self.message_display_tab1 = QTextEdit()
        self.message_display_tab1.setReadOnly(True)

        # Main left panel layout
        left_panel_layout_tab1 = QVBoxLayout()
        left_panel_layout_tab1.addLayout(input_layout_tab1)
        left_panel_layout_tab1.addWidget(self.message_display_tab1)

        # Plot layout
        self.figure_tab1 = Figure()
        self.canvas_tab1 = FigureCanvas(self.figure_tab1)
        self.toolbar_tab1 = NavigationToolbar(self.canvas_tab1, self)
        plot_layout_tab1 = QVBoxLayout()
        plot_layout_tab1.addWidget(self.toolbar_tab1)
        plot_layout_tab1.addWidget(self.canvas_tab1)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_panel_layout_tab1)
        main_layout.addLayout(plot_layout_tab1)
        self.tab1.setLayout(main_layout)

        # Instance variables to store generated data
        self.z_tab1 = None
        self.all_simulations_tab1 = None

#####################################################
########## set tab 2 ################################
#####################################################

    def initTab2(self):
        self.setWindowTitle('DTS Simulation GUI')
        self.setGeometry(100, 100, 1000, 600)
        # Input fields for hot spots
        self.lbl_start_points_tab2 = QLabel('Hotspot Start Points (comma-separated):')
        self.le_start_points_tab2 = QLineEdit()
        self.le_start_points_tab2.setText('11.7,15.05')

        self.lbl_stop_points_tab2 = QLabel('Hotspot Stop Points (comma-separated):')
        self.le_stop_points_tab2 = QLineEdit()
        self.le_stop_points_tab2.setText('13.2, 16.55')

        self.lbl_hot_temps_tab2 = QLabel('Hotspot Temperatures (comma-separated):')
        self.le_hot_temps_tab2 = QLineEdit()
        self.le_hot_temps_tab2.setText('47.0,80')


        # Input field for environmental temperature
        self.lbl_env_temp_tab2 = QLabel('Environmental Temperature:')
        self.le_env_temp_tab2 = QLineEdit()
        self.le_env_temp_tab2.setText('21.0')

        # Buttons
        self.btn_simulate_tab2 = QPushButton('Simulate DTS')
        self.btn_simulate_tab2.clicked.connect(self.simulate_dts_tab2)

        #CSV file
        self.lbl_csv_file = QLabel('CSV File:')
        self.btn_browse_csv = QPushButton('Browse')
        self.btn_browse_csv.clicked.connect(self.browse_csv_file)
        self.le_csv_file = QLineEdit()
        self.le_csv_file.setText('experiment.CSV')


        # Input fields for 30m section
        self.lbl_start_30m_section = QLabel('Start of 30m Section:')
        self.le_start_30m_section = QLineEdit()
        self.le_start_30m_section.setText('50')

        self.lbl_stop_30m_section = QLabel('Stop of 30m Section:')
        self.le_stop_30m_section = QLineEdit()
        self.le_stop_30m_section.setText('80')
        

        self.btn_plot_experiment = QPushButton('Plot Experiment')
        self.btn_plot_experiment.clicked.connect(self.plot_experiment_data)

        # Input layout
        input_layout_tab2 = QVBoxLayout()
        input_layout_tab2.addWidget(self.lbl_start_points_tab2)
        input_layout_tab2.addWidget(self.le_start_points_tab2)

        input_layout_tab2.addWidget(self.lbl_stop_points_tab2)
        input_layout_tab2.addWidget(self.le_stop_points_tab2)

        input_layout_tab2.addWidget(self.lbl_hot_temps_tab2)
        input_layout_tab2.addWidget(self.le_hot_temps_tab2)

        input_layout_tab2.addWidget(self.lbl_env_temp_tab2)
        input_layout_tab2.addWidget(self.le_env_temp_tab2)

        input_layout_tab2.addWidget(self.btn_simulate_tab2)

        input_layout_tab2.addWidget(self.lbl_csv_file)  # Add CSV file widgets
        input_layout_tab2.addWidget(self.le_csv_file)
        input_layout_tab2.addWidget(self.btn_browse_csv)

        input_layout_tab2.addWidget(self.lbl_start_30m_section)
        input_layout_tab2.addWidget(self.le_start_30m_section)

        input_layout_tab2.addWidget(self.lbl_stop_30m_section)
        input_layout_tab2.addWidget(self.le_stop_30m_section)

        input_layout_tab2.addWidget(self.btn_plot_experiment)

        # Message display area
        self.message_display_tab2 = QTextEdit()
        self.message_display_tab2.setReadOnly(True)

        # Main left panel layout
        left_panel_layout_tab2 = QVBoxLayout()
        left_panel_layout_tab2.addLayout(input_layout_tab2)
        left_panel_layout_tab2.addWidget(self.message_display_tab2)

        # Plot layout
        self.figure_tab2 = Figure()
        self.canvas_tab2 = FigureCanvas(self.figure_tab2)
        self.toolbar_tab2 = NavigationToolbar(self.canvas_tab2, self)
        plot_layout_tab2 = QVBoxLayout()
        plot_layout_tab2.addWidget(self.toolbar_tab2)
        plot_layout_tab2.addWidget(self.canvas_tab2)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_panel_layout_tab2, stretch = 1)
        main_layout.addLayout(plot_layout_tab2, stretch = 2)
        self.tab2.setLayout(main_layout)

#####################################################
########## set tab 3 ################################
#####################################################

    # def initTab3(self):
    #     self.setWindowTitle('DTS Simulation GUI')
    #     self.setGeometry(100, 100, 1000, 600)

    #     # Input fields for hot spots
    #     self.lbl_start_points = QLabel('3333:')
    #     self.le_start_points = QLineEdit()

    #     self.lbl_stop_points = QLabel('333 Points (comma-separated):')
    #     self.le_stop_points = QLineEdit()

    #     self.lbl_hot_temps = QLabel('Hot erwer (comma-separated):')
    #     self.le_hot_temps = QLineEdit()

    #     # Input field for environmental temperature
    #     self.lbl_env_temp = QLabel('33 Temperature:')
    #     self.le_env_temp = QLineEdit()

    #     # Button to trigger simulation
    #     self.btn_simulate = QPushButton('Simulate')
    #     self.btn_simulate.clicked.connect(self.simulate_dts)

    #     # Input layout
    #     input_layout = QVBoxLayout()
    #     input_layout.addWidget(self.lbl_start_points)
    #     input_layout.addWidget(self.le_start_points)
    #     input_layout.addWidget(self.lbl_stop_points)
    #     input_layout.addWidget(self.le_stop_points)
    #     input_layout.addWidget(self.lbl_hot_temps)
    #     input_layout.addWidget(self.le_hot_temps)
    #     input_layout.addWidget(self.lbl_env_temp) 
    #     input_layout.addWidget(self.le_env_temp) 
    #     input_layout.addWidget(self.btn_simulate)  

    #     # Message display area
    #     self.message_display = QTextEdit()
    #     self.message_display.setReadOnly(True)

    #     # Main left panel layout
    #     left_panel_layout = QVBoxLayout()
    #     left_panel_layout.addLayout(input_layout)
    #     left_panel_layout.addWidget(self.message_display)

    #     # Plot layout
    #     self.figure = Figure()
    #     self.canvas = FigureCanvas(self.figure)
    #     self.toolbar = NavigationToolbar(self.canvas, self)
    #     plot_layout = QVBoxLayout()
    #     plot_layout.addWidget(self.toolbar)
    #     plot_layout.addWidget(self.canvas)

    #     # Main layout
    #     main_layout = QHBoxLayout()
    #     main_layout.addLayout(left_panel_layout)
    #     main_layout.addLayout(plot_layout)
    #     self.tab3.setLayout(main_layout)

#####################################################
########## simulate_dts_tab1 ########################
#####################################################
    # Function to check how many simulations will be generated and approximate time
    def check_estimation_tab1(self):
        try:
            # Retrieve inputs, or use default if empty
            num_events = 2 if not self.le_num_events_tab1.text().strip() else int(self.le_num_events_tab1.text())
            hotspot_temperatures = [45.0, 55.0, 65.0] if not self.le_hot_temps_tab1.text().strip() else [float(temp) for temp in self.le_hot_temps_tab1.text().split(',')]
            num_shift1 = 4 if not self.le_shift1_tab1.text().strip() else int(self.le_shift1_tab1.text())
            num_random_locations = 1 if not self.le_num_random_locations_tab1.text().strip() else int(self.le_num_random_locations_tab1.text())

            # Calculate the number of simulations
            num_simulations = num_random_locations * len(hotspot_temperatures) * num_shift1

            # Approximate time per simulation (this is just an assumption, can be adjusted)
            time_per_simulation = 0.5  # Assume 0.05 seconds per simulation

            # Approximate total time
            total_time = num_simulations * time_per_simulation

            # Display the estimation results
            self.message_display_tab1.append(f"Estimated number of simulations: {num_simulations}")
            self.message_display_tab1.append(f"Estimated time for generation: {total_time:.2f} seconds")

        except ValueError as e:
            self.message_display_tab1.append(f"Estimation Error: {str(e)}")
            
    # Function to generate DTS data based on user input
    def generate_dts_tab1(self):
        try:
            # Retrieve inputs, or use default if empty
            num_events = 2 if not self.le_num_events_tab1.text().strip() else int(self.le_num_events_tab1.text())
            hotspot_temperatures = [45.0, 55.0, 65.0] if not self.le_hot_temps_tab1.text().strip() else [float(temp) for temp in self.le_hot_temps_tab1.text().split(',')]
            env_temp = 21 if not self.le_env_temp_tab1.text().strip() else float(self.le_env_temp_tab1.text())
            num_shift1 = 4 if not self.le_shift1_tab1.text().strip() else int(self.le_shift1_tab1.text())
            num_random_locations = 1 if not self.le_num_random_locations_tab1.text().strip() else int(self.le_num_random_locations_tab1.text())

            # Generate the DTS simulation data
            self.z_tab1, self.all_simulations_tab1 = generate_dts_data(
                num_events=num_events,
                env_temp=env_temp,
                hotspot_temperatures=hotspot_temperatures,
                num_shift1=num_shift1,
                Number_of_random_location=num_random_locations
            )
            self.message_display_tab1.append("Data generated successfully!")

        except ValueError as e:
            self.message_display_tab1.append(f"Input Error: {str(e)}")

    # Function to plot a specific sample
    def plot_dts_sample_tab1(self):
        try:
            # Retrieve the sample number or use default
            sample_num = 0 if not self.le_sample_num_tab1.text().strip() else int(self.le_sample_num_tab1.text())

            # Check if data has been generated and sample number is valid
            if self.all_simulations_tab1 is None:
                self.message_display_tab1.append("Error: Please generate data first!")
                return
            
            if sample_num < 0 or sample_num >= len(self.all_simulations_tab1):
                self.message_display_tab1.append(f"Error: Invalid sample number. Valid range: 0 to {len(self.all_simulations_tab1) - 1}")
                return

            # Select the desired sample
            simulation = self.all_simulations_tab1[sample_num]
            actual_T, DDTS = simulation["X"]
            H_starts, H_stops = simulation["Y"]

            # Clear the previous plot
            self.figure_tab1.clear()

            # Plotting the results
            ax = self.figure_tab1.add_subplot(111)

            # Plot the actual temperature profile
            ax.plot(self.z_tab1, actual_T, label='Actual Temperature', color='orange')

            # Plot the DTS simulation results
            ax.plot(self.z_tab1, DDTS, label='DTS Simulation', color='green')

            # Mark the H_starts and H_stops points
            ax.scatter(H_starts, [22] * len(H_starts), color='blue', marker='o', label='H_starts')
            ax.scatter(H_stops, [22] * len(H_stops), color='red', marker='x', label='H_stops')

            # Annotate the start and stop points
            for i, (start, stop) in enumerate(zip(H_starts, H_stops)):
                ax.text(start, 22, f'Start {i+1}', ha='right', color='blue')
                ax.text(stop, 22, f'Stop {i+1}', ha='left', color='red')

            # Finalize the plot
            ax.set_xlabel('Distance')
            ax.set_ylabel('Temperature')
            ax.set_title('DTS Simulation and Actual Temperature Profile with Hotspot Points')
            ax.legend()
            ax.grid(True)
            self.canvas_tab1.draw()

        except ValueError as e:
            self.message_display_tab1.append(f"Plot Error: {str(e)}")

    def simulate_dts_tab2(self):
        # Get user input for start points, stop points, and hot temperatures
        try:
            # Check for and handle empty inputs before conversion
            start_points_text = self.le_start_points_tab2.text().strip()
            stop_points_text = self.le_stop_points_tab2.text().strip()
            hot_temps_text = self.le_hot_temps_tab2.text().strip()
            env_temp_text = self.le_env_temp_tab2.text().strip()

            # Default values if input is missing or invalid
            start_points = np.array([11.7,15.05]) if not start_points_text else np.array([float(x.strip()) for x in start_points_text.split(',')])
            stop_points = np.array([13.2, 16.55]) if not stop_points_text else np.array([float(x.strip()) for x in stop_points_text.split(',')])
            hot_temps = np.array([47.0,80]) if not hot_temps_text else np.array([float(x.strip()) for x in hot_temps_text.split(',')])
            env_temp = 21.0 if not env_temp_text else float(env_temp_text)

        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter all valid numerics values for start points, stop points, and hot temperatures.')
            return

        # Validate input lengths
        if len(start_points) != len(stop_points) or len(start_points) != len(hot_temps):
            QMessageBox.warning(self, 'Input Error', 'The number of start points, stop points, and hot temperatures must be the same.')
            return

        # Simulate DTS data
        distance_tab2, actual_T_tab2, DDTS_tab2 = simulate(start=0, stop=30, H_starts=start_points, H_stops=stop_points, H_temperatures=hot_temps, env_temp=env_temp)


        # Plot DTS simulation results
        # print(f"self.ax_tab2 = {hasattr(self, 'ax_tab2')}")
        if hasattr(self, 'ax_tab2') == False:
            self.ax_tab2_sim = self.figure_tab2.add_subplot(111)
        elif (hasattr(self, 'ax_tab2') == True) and (hasattr(self, 'ax_tab2_sim') == True):
            self.ax_tab2_sim.clear()
            self.figure_tab2.clear()
            self.ax_tab2 = self.figure_tab2.add_subplot(111)
            self.ax_tab2.plot(self.distance_30m_section, self.temperature_30m_section, label='Experiment', color='purple')
            self.ax_tab2_sim = self.ax_tab2
        elif (hasattr(self, 'ax_tab2') == True) and (hasattr(self, 'ax_tab2_sim') == False): 
            self.ax_tab2_sim = self.ax_tab2
            
        self.ax_tab2_sim.plot(distance_tab2, actual_T_tab2, label='Actual Temperature', color='orange')
        self.ax_tab2_sim.plot(distance_tab2, DDTS_tab2, label='DTS_Simulate', color='green')

        # Finalize plot
        self.ax_tab2_sim.set_xlabel('Distance')
        self.ax_tab2_sim.set_ylabel('Temperature')
        self.ax_tab2_sim.set_title('Actual Temperature vs DTS_simulation vs DTS')
        self.ax_tab2_sim.legend()
        self.ax_tab2_sim.grid(True)
        self.canvas_tab2.draw()

        # Display success message
        self.message_display_tab2.clear()
        self.message_display_tab2.append(f'Simulation for {len(start_points)} Hotspot successful!')
    
    def browse_csv_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)", options=options)
        if file_name:
            self.le_csv_file.setText(file_name)

    def plot_experiment_data(self):
        # Default values if input is missing or invalid
        default_csv_file = 'EXperimental_data_temp700.csv'
        # Get user input for start points, stop points, and hot temperatures
        try:
            # Check for and handle empty inputs before conversion
            csv_file = self.le_csv_file.text().strip()
            start_30m_section = self.le_start_30m_section.text().strip()
            stop_30m_section = self.le_stop_30m_section.text().strip()

            # Check if the file exists in the current directory
            csv_file = default_csv_file if os.path.exists(default_csv_file) else self.le_csv_file.text()
            start_30m_section = 50 if not start_30m_section else  float(self.le_start_30m_section.text())
            stop_30m_section = 80 if not stop_30m_section else float(self.le_stop_30m_section.text())


        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter all valid numerics values for start points, stop points, and hot temperatures.')
            return
        # # Get user input for CSV file and 30m section parameters
        # csv_file = self.le_csv_file.text()
        # start_30m_section = float(self.le_start_30m_section.text())
        # stop_30m_section = float(self.le_stop_30m_section.text())

        # Call compare_sim_with_experimental with user input
        num_data_points,self.distance_30m_section,self.temperature_30m_section = plot_experimental(csv_file, start_30m_section, stop_30m_section)

        # Plot experiment results
        # Clear previous plot
        self.figure_tab2.clear()
        self.ax_tab2 = self.figure_tab2.add_subplot(111)
        self.ax_tab2.plot(self.distance_30m_section, self.temperature_30m_section, label='Experiment', color='purple')
        # ax_tab1.plot(distance_tab1, DDTS_tab1, label='DDT_Simulate', color='green')

        # Finalize plot
        self.ax_tab2.set_xlabel('Distance')
        self.ax_tab2.set_ylabel('Temperature')
        self.ax_tab2.set_title('Experimental data')
        self.ax_tab2.legend()
        self.ax_tab2.grid(True)
        self.canvas_tab2.draw()

        # Display success message
        self.message_display_tab2.clear()
        self.message_display_tab2.append(f'from {start_30m_section} to {stop_30m_section} section of experimental data ploted')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DTS_GUI()
    window.show()
    sys.exit(app.exec_())
